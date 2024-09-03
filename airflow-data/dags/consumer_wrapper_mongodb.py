from pymongo import MongoClient
import time
import logging
from kafka import KafkaConsumer, TopicPartition


class KafkaConsumerWrapperMongoDB:
    def __init__(self, consumer, topics, partition, mongodb_connector):
        self.consumer = consumer
        self.partition = TopicPartition(f'{topics}', partition)
        self.consumer.assign([self.partition])
        self.mongodb_connector = mongodb_connector

    def consume_and_insert_messages(self):
        try:
            for msg in self.consumer:
                self.mongodb_connector.insert_data(msg.value)
        except KeyboardInterrupt:
            logging.info("Received KeyboardInterrupt. Closing consumer.")

    def close(self):
        self.consumer.close()