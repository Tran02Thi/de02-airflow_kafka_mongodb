from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from stream_to_kafka import start_streaming


nationalities = ["US", "UA", "CH", "AU"]

with DAG(
    dag_id="random_people_names",
    start_date=datetime(2024, 8, 31),
    schedule_interval='*/10 * * * *',
    template_searchpath='/opt/airflow/sensor-data',
    catchup=True
) as dag:

    for idx, value in enumerate(nationalities):
        data_stream_task = PythonOperator(
            task_id=f'procuder_random_users_national_{value}',
            python_callable=start_streaming,
            op_kwargs={
                "nat" : value,
                "partition" : idx
            }
        )
        