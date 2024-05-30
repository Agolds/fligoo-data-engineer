# !pip install pandas psycopg2-binary sqlalchemy

import pandas as pd
from sqlalchemy import create_engine

# Define the connection parameters
db_config = {
    'dbname': 'testfligoo',
    'user': 'airflow',
    'password': 'airflow',
    'host': 'localhost',  # Use 'postgres' if running inside Docker network
    'port': 5432
}

# Defining display options
pd.set_option("max_columns", None)
pd.set_option('max_colwidth', None)
pd.set_option("expand_frame_repr", False)

# Connection string
connection_string = f"postgresql+psycopg2://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['dbname']}"

# QLAlchemy engine
engine = create_engine(connection_string)

# Query the testdata table
general_query = "SELECT * FROM testdata"
print(pd.read_sql(general_query, engine).head())

# Average Flight Duration (in hours)
avg_flight_duration = "SELECT AVG(flight_duration) AS avg_flight_duration_hours FROM testdata"
print(pd.read_sql(avg_flight_duration, engine))

# Average Flight Duration per Airline (in hours)
avg_flight_duration_airline = """SELECT airline_name, AVG(flight_duration) AS avg_flight_duration_hours
                                FROM testdata
                                GROUP BY airline_name
                                ORDER BY avg_flight_duration_hours DESC"""
print(pd.read_sql(avg_flight_duration_airline, engine))

# Count of Flights by Airline
flight_counts = """SELECT airline_name, COUNT(*) AS flight_count
                    FROM testdata
                    GROUP BY airline_name
                    ORDER BY flight_count DESC"""
print(pd.read_sql(flight_counts, engine))

# Average Delay Time (Actual vs Scheduled) for Departures (in minutes)
avg_delay_time_departures = """SELECT AVG(TIMESTAMPDIFF(MINUTE, departure_scheduled, departure_actual)) AS avg_departure_delay_minutes
                                FROM testdata
                                WHERE departure_actual IS NOT NULL 
                                AND departure_scheduled IS NOT NULL"""
print(pd.read_sql(avg_delay_time_departures, engine))
