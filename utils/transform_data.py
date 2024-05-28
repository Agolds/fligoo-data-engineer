import pandas as pd
import pytz
from datetime import timedelta


def selectColumns(df, columns):
    """

    :param df:
    :param columns:
    :return:
    """
    return df[columns]


def replaceCharInColumnDF(row, char_to_replace, new_char):
    """

    :param row:
    :param char_to_replace:
    :param new_char:
    :return:
    """
    return row.replace(char_to_replace, new_char)


def convertTolocalTimezone(row, target_timezone):
    """

    :param row:
    :param timezone:
    :return:
    """
    # Parse source and desired(target) timezone
    source_timezone = row['arrival_timezone']
    source_tz = pytz.timezone(source_timezone)
    target_tz = pytz.timezone(target_timezone)

    scheduled_time = pd.to_datetime(row['arrival_scheduled'])
    scheduled_time_target = scheduled_time.replace(tzinfo=None)

    scheduled_time_departure = pd.to_datetime(row['departure_actual'])
    scheduled_time_origin = scheduled_time_departure.replace(tzinfo=None)

    # Parse string timezones (e.g. America/New York) to pytz format using desired timezone (e.g. Argentina)
    datewith_tz_source = target_tz.localize(scheduled_time_origin)
    datewith_tz_target = target_tz.localize(scheduled_time_target)

    # Get difference of both timezones
    difference = int(datewith_tz_source.strftime('%z'))
    difference2 = int(datewith_tz_target.strftime('%z'))
    diff = abs(difference - difference2) / 100

    scheduled_time_in_local = scheduled_time + timedelta(hours=diff)
    return scheduled_time_in_local
