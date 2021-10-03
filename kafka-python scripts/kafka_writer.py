from kafka import KafkaProducer
class kafka_writer:
	def __init__(self,kafka_host):
		self.kafka_producer = KafkaProducer(bootstrap_servers=kafka_host, api_version=(0, 10, 1))
	
	def send(self, key, msg, topic):
		# self.kafka_producer.send(topic, msg.encode('utf-8'))
		self.kafka_producer.send(topic, key=key.encode('utf-8'), value=msg.encode('utf-8'))
   
	def close(self):
		self.kafka_producer.close()
   
	def flush(self):
		self.kafka_producer.flush()




# class kafkaWriter:
#     def __init__(self):
#         self.kafka_producer = KafkaProducer(bootstrap_servers=settings.KAFKA_PROP['host'], api_version=(0, 10, 1))

#     def send(self, key, msg):
#         self.kafka_producer.flush()
#         self.kafka_producer.send(settings.KAFKA_PROP['topic_name'], key=key.encode('utf-8'), value=msg.encode('utf-8'))

#     def close(self):
#         self.kafka_producer.close()