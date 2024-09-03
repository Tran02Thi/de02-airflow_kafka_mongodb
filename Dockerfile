FROM apache/airflow:2.3.2

USER root
# Install OpenJDK-8
RUN apt-get update && \
    apt-get install -y openjdk-11-jdk && \
    apt-get clean

ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64/
RUN export JAVA_HOME

USER airflow
RUN pip install --user --upgrade pip

COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir --user -r /requirements.txt