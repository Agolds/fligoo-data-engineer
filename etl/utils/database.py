import psycopg2
from sqlalchemy import create_engine


class DatabaseConnections:
    def __init__(self, db_config):
        self.user = db_config['user']
        self.password = db_config['password']
        self.host = db_config['host']
        self.port = db_config['port']
        self.dbname = db_config['dbname']
        self.tname = db_config['tname']

    def saveDataDB(self, df):
        # Connection string
        connection_string = f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.dbname}"

        # SQLAlchemy engine
        engine = create_engine(connection_string)

        # Load the DataFrame into PostgreSQL table
        try:
            print(f"Loading {len(df.index)} records.")
            df.to_sql(self.tname, engine, if_exists='replace', index=False)
            print("Successfuly loaded data")
        except Exception as e:
            print("Error loading data")
            print(e)
