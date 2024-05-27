import requests
import pandas as pd
from config.constants import CONSTANTS


class APIRequests:
    # Constructor de la clase
    def __init__(self, base_url, flights_api_filters):
        self.base_url = CONSTANTS.get(base_url)
        self.flights_api_filters = CONSTANTS.get(flights_api_filters)

    # Método de la clase
    def getFlightsData(self):
        """

        :return:
        """
        offset = 0
        total_records = None
        all_data = pd.DataFrame()
        filters = self.flights_api_filters
        while True:
            response = requests.get(self.base_url, filters).json()
            if response.get('error'):
                print(response)
                break

            limit = response.get('pagination', {}).get('limit', 100)
            if total_records is None:
                total_records = response.get('pagination', {}).get('total', 0)

            data = response.get('data')
            if data:
                df = pd.DataFrame(data)
                all_data = pd.concat([all_data, df], ignore_index=True)

            offset += limit + 1
            filters['offset'] = offset

            if offset >= total_records:
                break

        return all_data
