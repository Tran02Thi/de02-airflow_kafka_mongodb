import os
import configparser
from mongo_connector import MongoDBConnector
from airflow import DAG
from consumer_wrapper_mongodb import KafkaConsumerWrapperMongoDB
from datetime import timedelta
from datetime import datetime
from airflow.operators.python_operator import PythonOperator
from dotenv import load_dotenv
import json
from kafka import KafkaConsumer, TopicPartition

config = configparser.ConfigParser()
config.read('/opt/airflow/config.ini')
load_dotenv('/opt/airflow/.env')

mongo_username = os.getenv('MONGO_INITDB_ROOT_USERNAME')
mongo_password = os.getenv('MONGO_INITDB_ROOT_PASSWORD')
mongo_uri_template  = config.get('mongodb', 'uri')

KAFKA_HOST_IP = os.getenv('KAFKA_HOST_IP').split(',')

nationalities = ["US", "UA", "CH", "AU"]

def kafka_consumer_mongodb_main(**kwargs):
    mongo_uri = mongo_uri_template.format(MONGO_INITDB_ROOT_USERNAME=mongo_username, MONGO_INITDB_ROOT_PASSWORD=mongo_password)
    mongodb_connector = MongoDBConnector(mongo_uri, kwargs["database"], kwargs["collection"])
    mongodb_connector.create_collection()

    try:
        consumer = KafkaConsumer(
            bootstrap_servers=KAFKA_HOST_IP,
            group_id='users',
            auto_offset_reset='earliest',  
            value_deserializer=lambda x: json.loads(x.decode('utf-8')),
            enable_auto_commit=True
        )
        topics = 'random_users'
        partition = TopicPartition(f'{topics}', kwargs["partition"])
        consumer.assign([partition])

        kafka_consumer = KafkaConsumerWrapperMongoDB(consumer, topics, kwargs["partition"], mongodb_connector)
        kafka_consumer.consume_and_insert_messages()
        
    except Exception as e:
        print(f"Failed to consume message from Kafka: {e}")
        raise e

with DAG(
    dag_id="consumer_users",
    start_date=datetime(2024, 8, 31),
    schedule_interval=None,
    template_searchpath='/opt/airflow/sensor-data',
    catchup=True
) as dag:

    for idx, value in enumerate(nationalities):
        data_stream_task = PythonOperator(
            task_id=f'consumer_random_users_national_{value}',
            python_callable=kafka_consumer_mongodb_main,
            op_kwargs={
                "database" : 'users',
                "collection" : value,
                "partition" : idx
            }
        )