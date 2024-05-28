from pandas import json_normalize

from config.constants import CONSTANTS
from utils.api_requests import APIRequests
from utils.transform_data import selectColumns, replaceCharInColumnDF, convertTolocalTimezone


if __name__ == '__main__':
    base_url = CONSTANTS.get("BASE_URL")
    flights_api_filters = CONSTANTS.get("FLIGHTS_API_ACCESS_KEY_FILTERS")
    columns = CONSTANTS.get("COLUMNS")
    transformations = CONSTANTS.get("TRANSFORMATIONS")

    api_requests = APIRequests(base_url, flights_api_filters)

    # flights_raw_data = api_requests.getFlightsData()
    flights_raw_data = api_requests.testAPI()

    df = selectColumns(flights_raw_data, columns)


    if transformations:
        for transformation, values in transformations.items():
            if "convertTolocalTimezone" in transformation:
                desired_time_zone = values
                df['local_timezone'] = df.apply(convertTolocalTimezone, args=(desired_time_zone,), axis=1)

            elif "replaceCharInColumnDF" in transformation:
                for col in values:
                    col_name = col.split('###')[0]
                    params = col.split('###')[1]
                    df[col_name] = df[col_name].apply(replaceCharInColumnDF, args=(params[0], params[1]))

    print(df)
