from kafka import KafkaProducer
import json
import data
import time 

def json_serializer(data):
    return json.dumps(data).encode('utf-8')

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=json_serializer
                         )

if __name__ =='__main__':
    while True:
        registered_user = data.get_registered_user()
        producer.send('msgtopic1', value=registered_user) # DATA WILL BE SEND TO THE PARTICULAR KAFKA TOPIC 
        print(registered_user)
        time.sleep(3)