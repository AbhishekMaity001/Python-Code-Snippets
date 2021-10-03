    def write_to_kafka(self,data):
        topic_name1 = settings.KAFKA_PROP['topic_name']
        kafkaObj1 = kafka_writer(settings.KAFKA_PROP['host'])
        for index,row in data.iterrows():
            for column in data.columns:
                if not pd.isnull(row[column]) and column!='time_stamp' and column!='asset_no':
                    current_ts = calendar.timegm(time.gmtime())*1000
                    message1 = str(row['asset_no']) + ',' + str(int(row['time_stamp'])) + ',' + str(column) + ',' + str(row[column]) + ',NA,LOG,'+str(current_ts)
                    # message2 = str(row['asset_no']) + ',' + str(int(row['time_stamp'])) + ',' + str(column) + ',' + str(row[column]) + ',NA,LOG,-1,DELEK,LOG'
                    # print (message1)
                    kafkaObj1.send(row['asset_no'], message1, topic_name1)
            kafkaObj1.flush()



def main():
    while(True):
        use_cols = []
        asset_no = 'BSR-01'
        labels = []
        window_size = 1
        stride = 1

        model = Model(use_cols, labels, window_size, stride)
        output_df1,output_df2,output_df3 = model.predict(pd.DataFrame(),{})
        model.write_to_kafka(output_df1)
        model.write_to_kafka(output_df2)
        model.write_to_kafka(output_df3)
        time.sleep(300)

if __name__ == '__main__':
	main()