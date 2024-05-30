import requests
import pandas as pd
from pandas import json_normalize
import logging


class APIRequests:
    def __init__(self, base_url, flights_api_filters):
        self.base_url = base_url
        self.flights_api_filters = flights_api_filters

    def getFlightsData(self):
        """
        Retrieves data from API in loop based on total records and 100 records limit
        :return pd.Dataframe: API response:
        """
        # Set up logging
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)
        offset = 0
        total_records = None
        all_data_df = pd.DataFrame()
        filters = self.flights_api_filters
        while True:
            response = requests.get(self.base_url, filters).json()
            if response.get('error'):
                logger.error(response)
                break

            # Returns limitation of API - Default: 100
            limit = response.get('pagination', {}).get('limit', 100)
            if total_records is None:
                total_records = response.get('pagination', {}).get('total', 0)

            # Expands columns under father tags to the same level joining with '_' for the name
            data = response.get('data')
            if data:
                df = json_normalize(data, sep='_')
                # Concatenates with general Dataframe to get all active flights
                all_data_df = pd.concat([all_data_df, df], ignore_index=True)

            offset += limit + 1
            filters['offset'] = offset
            if offset >= total_records:
                break

        return all_data_df

    def testAPI(self):
        """
        Single call to just return the minimum constraint records (100)
        :return pd.Dataframe: API response
        """
        data = requests.get(self.base_url, self.flights_api_filters).json()
        return json_normalize(data['data'], sep='_')
