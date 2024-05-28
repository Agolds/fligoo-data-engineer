import requests
import pandas as pd
from pandas import json_normalize


class APIRequests:
    # Constructor de la clase
    def __init__(self, base_url, flights_api_filters):
        self.base_url = base_url
        self.flights_api_filters = flights_api_filters

    # Método de la clase
    def getFlightsData(self):
        """

        :return:
        """
        offset = 0
        total_records = None
        all_data_df = pd.DataFrame()
        filters = self.flights_api_filters
        while True:
            response = requests.get(self.base_url, filters).json()
            if response.get('error'):
                print(response)
                # TODO: add continue so that this error is notified
                break

            limit = response.get('pagination', {}).get('limit', 100)
            if total_records is None:
                total_records = response.get('pagination', {}).get('total', 0)

            data = response.get('data')
            if data:
                df = json_normalize(data, sep='_')
                all_data_df = pd.concat([all_data_df, df], ignore_index=True)

            offset += limit + 1
            filters['offset'] = offset

            if offset >= total_records:
                break

        return all_data_df

    def testAPI(self):
        data = requests.get(self.base_url, self.flights_api_filters).json()
        return json_normalize(data['data'], sep='_')
