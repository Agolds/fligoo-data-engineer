# Use the official Airflow image as the base image
FROM apache/airflow:2.5.1

RUN export PYTHONPATH=$PYTHONPATH:/opt/airflow/scripts
RUN echo $PYTHONPATH
# Install additional Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


