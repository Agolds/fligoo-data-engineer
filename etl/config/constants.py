CONSTANTS = \
    {
        "BASE_URL": "http://api.aviationstack.com/v1/flights",
        "FLIGHTS_API_ACCESS_KEY_FILTERS": {
            'access_key': 'bc90ab9b2a1581327d4340701bef8682',
            'flight_status': 'active'
        },
        "COLUMNS": [
            'flight_date',
            'flight_status',
            'departure_airport',
            'departure_timezone',
            'departure_iata',
            'departure_scheduled',
            'departure_actual',
            'arrival_airport',
            'arrival_timezone',
            'arrival_iata',
            'arrival_scheduled',
            'arrival_estimated',
            'airline_name',
            'airline_iata',
            'flight_number',
            'flight_iata'
        ],
        "TRANSFORMATIONS": {
            'convertTolocalTimezone': ['departure_actual###America/Argentina/Buenos_Aires',
                                       'arrival_estimated###America/Argentina/Buenos_Aires'],
            'replaceCharInColumnDF': ['departure_timezone###/-', 'arrival_timezone###/-'],
            'calculateFlightDuration': ['departure_actual', 'arrival_estimated']
        }
    }
