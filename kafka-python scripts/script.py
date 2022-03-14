import json
from datetime import datetime
import os
from apscheduler.schedulers.background import BackgroundScheduler
import time
import confluent_kafka.admin, pprint
from kafka import KafkaProducer
import pandas as pd


with open("config.json") as fp:
    config_data = json.load(fp)


def check_for_new_json_files(source_path):
    todays_date = datetime.now().strftime("%Y-%m-%d")
    if todays_date not in os.listdir(source_path):
        print(f"\n'{todays_date}' date folder not found in source directory")
        return

    updated_path = os.path.join(source_path, todays_date)
    current_hour = str(datetime.now().hour).zfill(2)
    if current_hour not in os.listdir(updated_path):
        print(f"\n'{current_hour}' hour folder not found in '{todays_date}' directory")
        return

    updated_path = os.path.join(updated_path, current_hour)
    non_flatten_json_files = []
    directory_files = os.listdir(updated_path)
    for i in directory_files:
        if not i.endswith(".json"):
            continue
        if config_data["flatten_json_filename_additional_tag"] in i:
            continue
        if (
            i.replace(
                ".json", f'{config_data["flatten_json_filename_additional_tag"]}.json'
            )
            in directory_files
        ):
            continue
        non_flatten_json_files.append(i)

    if not non_flatten_json_files:
        return

    for i in non_flatten_json_files:
        new_filename = i.replace(
            ".json", f'{config_data["flatten_json_filename_additional_tag"]}.json'
        )
        generate_flatten_json(updated_path, i, new_filename)
        try:
            write_to_kafka(filename=os.path.join(updated_path, new_filename))
        except Exception as e:
            print("Exception Occured during writing data to kafka ", str(e))


def generate_flatten_json(source_path, original_filename, new_filename):
    with open(os.path.join(source_path, original_filename)) as fp:
        source_data = json.load(fp)

    generated_output = []

    timestamp = source_data["timestamp"]
    for index, i in enumerate(source_data["services"]):
        # print(f"{index + 1}) {i['name']}")
        for datatype in config_data["service_data_mapping"]:
            if i[datatype["key"]]:
                for j in i[datatype["key"]]:
                    flatten_data = {
                        "timestamp": timestamp,
                        "type": datatype["custom_output_field_name"],
                        "name": i["name"],
                    }
                    flatten_data.update(j)
                    generated_output.append(flatten_data)

    if not generated_output:
        return

    with open(os.path.join(source_path, new_filename), "w") as fp:
        json.dump(generated_output, fp)

    print(f"\nFlattened '{original_filename}' to '{new_filename}'")


def write_to_kafka(filename):
    """Function to write the data to kafka in a proper format"""
    try:
        rewrite_timestamp = config_data["rewrite_timestamp"]
        data = pd.read_json(filename, convert_dates=False)

        # Taking current timestamp in epoch if enabled!
        if rewrite_timestamp.lower() == 'enable':
            data['timestamp'] = int(datetime.now().timestamp()) * 1000

        topic_name = config_data["topic_name"]
        kafka_host = config_data["kafka_host"]
        conf = {'bootstrap.servers': kafka_host}
        kafka_admin = confluent_kafka.admin.AdminClient(conf)

        kafkaobj = KafkaProducer(bootstrap_servers=kafka_host, api_version=(0, 10, 1))
        topic_list = kafka_admin.list_topics().topics  # LIST OUT ALL THE TOPICS
        if topic_name in list(topic_list.keys()):
            pass
        else:
            # If the topic is not created then it will create for 1st time
            new_topic = confluent_kafka.admin.NewTopic(topic_name, 1, 1)  # partitions=1, replicas=1
            kafka_admin.create_topics([new_topic, ])

        for idx in range(data.shape[0]):
            prepare_message = str(data.iloc[idx, :].values.tolist())
            kafkaobj.send(topic_name, value=prepare_message.encode('utf-8'))
            # print(prepare_message)
        # print(topic_name, kafka_host)

    except Exception as e:
        print("Error while writing data to kafka!  ", str(e))


def job():
    check_for_new_json_files(config_data["source_folder_full_path"])


if __name__ == "__main__":
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        job, "interval", seconds=config_data["cron_job_interval_in_seconds"]
    )
    scheduler.start()
    print("\nJob Started and scheduled, Press Ctrl+C to exit")

    try:
        while True:
            time.sleep(5)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
