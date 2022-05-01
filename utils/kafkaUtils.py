from kafka import KafkaConsumer
import sys

# Define server with port
#bootstrap_servers = ['localhost:9092']

def get_kafka_topics(bootstrap_servers):
	consumer = KafkaConsumer(group_id='test-1', bootstrap_servers=bootstrap_servers)
	kafka_topics = consumer.topics()
	if kafka_topics:
		return str(kafka_topics)
	else:
		return str(())


def get_messages_from_topic(bootstrap_servers, topic_name):
	consumer = KafkaConsumer (topic_name, group_id=None,bootstrap_servers=bootstrap_servers,consumer_timeout_ms=1000,auto_offset_reset='earliest',enable_auto_commit=True)
	list_messages = []

	print("Here")
	# Read and print message from consumer
	print(type(consumer))
	for msg in consumer:
		print("Topic Name=%s,Message=%s"%(msg.topic,msg.value))
		print(msg.value)
		list_messages.append(msg.value)

	return list_messages





















