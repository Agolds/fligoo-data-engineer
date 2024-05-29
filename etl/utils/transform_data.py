import pandas as pd


def selectColumns(df, columns):
    """
    Filters columns in dataframe based parameter columns
    :param df: Pandas series
    :param columns: List of columns
    :return: Pandas series with filtered columns
    """
    return df[columns]


def replaceCharInColumnDF(row, char_to_replace, new_char):
    """
    Replace string type char to a new one
    :param row:
    :param char_to_replace:
    :param new_char:
    :return:
    """
    return row.replace(char_to_replace, new_char)


def convertTolocalTimezone(row, column, timezone):
    """
    Each datetime converted into desired timezone
    :param timezone: desired timezone
    :param row: pandas series, data
    :param column: string, desired timezone
    :return: datetime column
    """
    return pd.Timestamp(str(row[column]).replace('+00:00', '')).tz_localize(timezone)


def calculateFlightDuration(row, departure_col, arrival_col):
    """
    Gets difference between datetimes
    :param row: pandas series, data.
    :param departure_col: Departure column name
    :param arrival_col: Arrival column name
    :return: string referencing hours
    """
    return pd.Timedelta(pd.to_datetime(row[departure_col]) - pd.to_datetime(row[arrival_col])).seconds / 3600
