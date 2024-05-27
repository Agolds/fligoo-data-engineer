from utils.api_requests import APIRequests
# from utils import database


if __name__ == '__main__':
    # Crear una instancia de la clase
    api_requests = APIRequests("BASE_URL", "FLIGHTS_API_ACCESS_KEY_FILTERS")
    flights_raw_data = api_requests.getFlightsData()

    print(flights_raw_data)


