import pandas as pd
import datetime
pd.options.mode.chained_assignment = None


def selectColumns(df, columns):
    """
    Filters columns in dataframe based parameter columns
    :param df: Pandas series
    :param columns: List of columns
    :return pd.Series: Pandas series with filtered columns
    """
    try:
        return df[columns]
    except Exception as e:
        print(e)
        return None


def replaceCharInColumnDF(row, char_to_replace, new_char):
    """
    Replace string type char to a new one
    :param row:
    :param char_to_replace:
    :param new_char:
    :return: Replaced value of column
    """
    try:
        return row.replace(char_to_replace, new_char)
    except Exception as e:
        print(e)
        return row


def convertToLocalTimezone(row, column, timezone):
    """
    Extracts timezone from datetime and converts it in local tz
    :param timezone: desired timezone
    :param row: pandas series, data
    :param column: string, desired timezone
    :return String: Timezone vs UTC (positive or negative)
    """
    try:
        tz_hour = int(pd.Timestamp(str(row[column]).replace('+00:00', '')).tz_localize(row[timezone]).strftime('%z')) / 100
        return f'+{tz_hour}' if tz_hour > 0 else str(tz_hour)
    except Exception as e:
        print(e)
        return None


def calculateFlightDuration(row, departure_col, arrival_col):
    """
    Gets difference between date times
    :param row: pandas series, data.
    :param departure_col: Departure column name
    :param arrival_col: Arrival column name
    :return String: referencing hours
    """
    try:
        return pd.Timedelta(pd.to_datetime(row[departure_col]) - pd.to_datetime(row[arrival_col])).seconds / 3600
    except Exception as e:
        print(e)
        return None


def addLoadedTimestamp():
    """
    Returns current date time
    :return Timestamp: Current timestamp
    """
    try:
        return datetime.datetime.now()
    except Exception as e:
        print(e)
        return None
