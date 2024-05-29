from etl.config.constants import CONSTANTS
from etl.utils.api_requests import APIRequests
from etl.utils.database import DatabaseConnections
from etl.utils.transform_data import replaceCharInColumnDF, \
    convertToLocalTimezone, selectColumns, calculateFlightDuration, addLoadedTimestamp


if __name__ == '__main__':
    # Constants - App configs
    base_url = CONSTANTS.get("BASE_URL")
    flights_api_filters = CONSTANTS.get("FLIGHTS_API_ACCESS_KEY_FILTERS")
    columns = CONSTANTS.get("COLUMNS")
    transformations = CONSTANTS.get("TRANSFORMATIONS")
    db_config = CONSTANTS.get("DATABASE_CONFIG")

    # Classes Instances
    api_requests = APIRequests(base_url, flights_api_filters)
    db_connect = DatabaseConnections(db_config)

    # Get data from API
    try:
        # flights_raw_data = api_requests.testAPI()
        flights_raw_data = api_requests.getFlightsData()
        df = selectColumns(flights_raw_data, columns)
    except Exception as e:
        print(e)

    # Execute transformations
    if transformations:
        for transformation, values in transformations.items():
            if "convertToLocalTimezone" in transformation:
                for col in values:
                    col_name = col.split('###')[0]
                    local_timezone = col.split('###')[1]
                    new_col_name = col_name + '_local_tz'
                    df[new_col_name] = df.apply(convertToLocalTimezone, args=(col_name, local_timezone), axis=1)

            elif "replaceCharInColumnDF" in transformation:
                for col in values:
                    col_name = col.split('###')[0]
                    params = col.split('###')[1]
                    df[col_name] = df[col_name].apply(replaceCharInColumnDF, args=(params[0], params[1]))

            elif "calculateFlightDuration" in transformation:
                df['flight_duration'] = df.apply(calculateFlightDuration, args=(values[0], values[1]), axis=1)

            elif "addLoadedTimestamp" in transformation:
                df['timestamp_loaded'] = addLoadedTimestamp()

        # Load data into database
        db_connect.saveDataDB(df)
    else:
        print("Transformations were not declared. Unable to load data.")
