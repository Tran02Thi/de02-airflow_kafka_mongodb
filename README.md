![Alt text](https://svgshare.com/i/19yL.svg)

<h1 align="center">ELT Realtime Pipeline with Airflow, Kafka and MongoDB </h1>


<p align="center">
  <a href="#introduction">Introduction</a> •
  <a href="#scenario">Scenario</a> •
  <a href="#base-concepts">Base Concepts</a> •
  <a href="#prerequisites">Prerequisites</a> •
  <a href="#set-up">Set-up</a> •
  <a href="#installation">Installation</a> •
  <a href="#airflow-interface">Airflow Interface</a> •
  <a href="#pipeline-task-by-task">Pipeline Task by Task</a> •
  <a href="#shut-down-and-restart-airflow">Shut Down and Restart Airflow</a> •
  <a href="#learning-resources">Learning Resources</a>
</p>

---


## Introduction
### Overview

- This project implements a real-time ELT (Extract, Load, Transform) pipeline that leverages the Random User API to generate and send user data to Kafka and orchestrated be used Airflow. The data is then consumed and stored in MongoDB. Apache Airflow orchestrates the entire process, automating the pipeline to run every 10 minutes. The setup ensures efficient data flow from source to storage with minimal latency, making it suitable for real-time data processing and analytics.

### The goal of this project

Potential Analyses from the Data:
- Demographics: Analyze the distribution of users based on gender, age, and location (e.g., country, city, state).

- Geolocation: Map users by their geographical coordinates, allowing for regional analysis and understanding of user density.

- Time Zone Analysis: Explore user activity based on their time zone, useful for understanding when users are most active.
### Prerequisites

<p align="center">
  <a>
    <img src="https://skillicons.dev/icons?i=docker,kafka,mongodb,py" alt="Skills" /> 
  </a>
  <img src="https://svgshare.com/i/19wF.svg" alt="Alt text" width="40" height="40" style="vertical-align: 2px; margin-left: 10px;">
</p>

    Before you continue, ensure you meet the following requirements:

        * You have installed Python.
        * You have a basic understanding of Docker (docker-compose, docker network, docker images,...). 
        * You have a basic understanding of Airflow orchestrated (DAG, PythonOperator, CronTab, ...).
        * You understand the basics of Kafka (procuder, consumer, topic, broker, partition, ...)
        * You have a basic understanding of NoSQL (MongoDB)
        * Knowledge of data lake, data warehouse

### Data Source
A free, open-source API for generating random user data. Like Lorem Ipsum, but for people.
- The API be used: 

  > **Random Users:**
  > 
  > Link website: https://randomuser.me/

## Usage
Download / pull the repo to your desired location.

Start the installation with:

    docker-compose up -d

This command will pull and create Docker images and containers for Airflow, Kafka, MongoDB according to the instructions in the docker-compose.yml file:


After everything has been installed, you can check the status of your containers (if they are healthy) with:

    docker ps

Note: it might take up to 30 seconds for the containers to have the healthy flag after starting.

<p align="center">
  <a>
    <img src="https://imagizer.imageshack.com/img923/1527/robTAM.png"> 
  </a>
</p>

### Airflow Interface
You can now access the Airflow web interface by going to http://localhost:8080/. If you have not changed them in the docker-compose.yml file, the default user is **airflow** and password is **airflow**:

<p align="center">
  <img src=https://user-images.githubusercontent.com/19210522/114421290-d5060d80-9bbd-11eb-842e-13a244996200.png>
</p>

After signing in, the Airflow home page is the DAGs list page. Here you will see all your DAGs and the Airflow example DAGs, sorted alphabetically. 

Any DAG python script saved in the directory [**dags/**](https://github.com/Tran02Thi/de02-airflow_kafka_mongodb/tree/main/airflow-data/dags), will show up on the DAGs page (e.g. the first DAG, `random_people_names`, is the one built for this project).

<p align="center">
  <img src=https://imagizer.imageshack.com/img924/9761/ScSW1G.png>
</p>

And with dags:

<p align="center">
  <img src=https://imagizer.imageshack.com/img922/5092/7ROXPw.png>
</p>

<br>

<p align="center">
  <img src=https://imagizer.imageshack.com/img924/5214/VRi2wg.png>
</p>


### Kafka Interface
You can now access the Kafdrop web interface by going to http://localhost:9123/. You can see UI the following:

<p align="center">
  <img src=https://imagizer.imageshack.com/img922/4268/I15n7b.png>
</p>


And now you can create topic with name is **random_users** and 4 partition
<p align="center">
  <img src="https://imagizer.imageshack.com/img924/4694/QajhsX.png"> 
</p>

<br>

<p align="center">
  <img src="https://imagizer.imageshack.com/img924/7605/S12yu5.png"> 
</p>


### MongoDB

If you want to use mongoDB of your, you will have to enter the mongoDB connection string (or environment variable or file with the string) in the .env file:
    
    # MongoDB 
    MONGO_INITDB_ROOT_USERNAME=${USER}
    MONGO_INITDB_ROOT_PASSWORD=${PASSWORD}

First you need to run dag **random_people_names** to send messages to kafka continuously every 10 minutes.

<p align="center">
  <img src="https://imagizer.imageshack.com/img924/3647/AvIzW1.png"> 
</p>

Next you will run dag **consumer_users** to get data in the partition and send it to MongoDB with database as users and collection as 4 predetermined countries (you can view and change arbitrarily in the source code).

<p align="center">
  <img src="https://imagizer.imageshack.com/img923/1346/UaVomY.png"> 
</p>

<br>
We will use Kafdrop to check healthy the streaming
<br> </br>
<p align="center">
  <img src="https://imagizer.imageshack.com/img924/5829/9EyhaA.png"> 
</p>

The data will then be continuously written to mongoDB ::))


## Storage
<p align="center">
  <a>
    <img src="https://i.ibb.co/CbXjCVP/Mongodb-2.png"> 
  </a>
</p>