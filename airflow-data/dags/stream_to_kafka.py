"""
Gets the random user API data and writes the data to a Kafka topic every 10 seconds
"""
import requests
import json
import time
from kafka import KafkaProducer
import os 
from dotenv import load_dotenv
import configparser

config = configparser.ConfigParser()

config.read('/opt/airflow/config.ini')

load_dotenv('/opt/airflow/.env')
KAFKA_HOST_IP = os.getenv('KAFKA_HOST_IP').split(',')

def create_response_dict(url: str="https://randomuser.me/api/", nat: str='') -> dict:
    """
    Creates the results JSON from the random user API call
    """
    query_params = {
        "password" : "upper,16-32",
        "nat" : nat
    }
    response = requests.get(url, params=query_params)
    data = response.json()
    results = data["results"][0]
    return results


def create_final_json(results: dict) -> dict:
    """
    Creates the final JSON to be sent to Kafka topic only with necessary keys
    """
    kafka_data = {}

    kafka_data["full_name"] = f"{results['name']['title']}. {results['name']['first']} {results['name']['last']}"
    kafka_data["gender"] = results["gender"]
    kafka_data["location"] = f"{results['location']['street']['number']}, {results['location']['street']['name']}"
    kafka_data["city"] = results['location']['city']
    kafka_data["country"] = results['location']['country']
    kafka_data["postcode"] = results['location']['postcode']
    kafka_data["latitude"] = results['location']['coordinates']['latitude']
    kafka_data["longitude"] = results['location']['coordinates']['longitude']
    kafka_data["email"] = results["email"]
    kafka_data["national"] = results["nat"]

    return kafka_data


def create_kafka_producer():
    """
    Creates the Kafka producer object
    """
    return KafkaProducer(
                bootstrap_servers=KAFKA_HOST_IP,
                acks='all',
                retries=3,
                max_request_size=10485760,
                key_serializer=lambda k: k.encode('utf-8'),
                value_serializer=lambda m: json.dumps(m).encode('utf-8')
            )

def start_streaming(**kwargs):
    """
    Writes the API data every 10 seconds to Kafka topic random_names
    """

    end_time = time.time() + 120 # the script will run for 2 minutes
    while True:
        
        producer = create_kafka_producer()
        results = create_response_dict(nat=kwargs["nat"])
        kafka_data = create_final_json(results)

        if time.time() > end_time:
            break

        key = f'{kwargs["nat"]}'
        producer.send("random_users", key=key, value=kafka_data, partition=kwargs["partition"])
        time.sleep(5)

if __name__ == "__main__":
    start_streaming()