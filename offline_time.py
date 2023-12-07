import jdatetime
from persian_converter import convert_to_persian_number, get_persian_month_from_index, get_persian_day_from_index

def get_shamsi_time_info_offline():
    jd = jdatetime.date.today()

    year_index = convert_to_persian_number(jd.year)
    month_index = convert_to_persian_number(jd.month)
    day_index = convert_to_persian_number(jd.day)
    name_of_the_month = get_persian_month_name()
    name_of_the_day = get_persian_day_name()

    return {
        "year": year_index,
        "month": month_index,
        "day": day_index,
        "name_of_the_month": name_of_the_month,
        "name_of_the_day": name_of_the_day
    }

def get_persian_month_name():
    current_month_index = jdatetime.date.today().month
    month_name = get_persian_month_from_index(current_month_index - 1)
    return month_name

def get_persian_day_name():
    current_day_index = jdatetime.date.today().weekday()
    day_name = get_persian_day_from_index(current_day_index - 1)
    return day_name