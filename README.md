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



## Architecture


## Usage

<p align="center">
  <a>
    <img src="https://imagizer.imageshack.com/img924/7605/S12yu5.png"> 
  </a>
</p>

<p align="center">
  <a>
    <img src="https://i.ibb.co/nfL71vx/Dags.png"> 
  </a>
</p>


<p align="center">
  <a>
    <img src="https://i.ibb.co/TvgYbW6/Dag-consumer.png"> 
  </a>
</p>


<p align="center">
  <a>
    <img src="https://i.ibb.co/C1QFfGh/Dag-procuder.png"> 
  </a>
</p>


<p align="center">
  <a>
    <img src="https://i.ibb.co/3hYBkd2/consumer-running.png"> 
  </a>
</p>

<p align="center">
  <a>
    <img src="https://i.ibb.co/NFYNVZH/Dag-procuder-2.png"> 
  </a>
</p>

<p align="center">
  <a>
    <img src="https://i.ibb.co/F4cHqVc/procuder-running.png"> 
  </a>
</p>


## Storage
<p align="center">
  <a>
    <img src="https://i.ibb.co/CbXjCVP/Mongodb-2.png"> 
  </a>
</p>