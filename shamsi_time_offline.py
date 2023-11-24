import jdatetime

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
    persian_months = [
        "فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور",
        "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"
    ]

    current_month = jdatetime.date.today().month
    return persian_months[current_month - 1]

def get_persian_day_name():
    days = ["یک‌شنبه", "دوشنبه", "سه‌شنبه", "چهارشنبه", "پنج‌شنبه", "جمعه", "شنبه"]
    return days[jdatetime.date.today().weekday() - 1]

def convert_to_persian_number(num):
    # Mapping of digits to their Persian equivalents
    persian_digits = {
        '0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '۴',
        '5': '۵', '6': '۶', '7': '۷', '8': '۸', '9': '۹'
    }

    # Convert the number to a string
    num_str = str(num)

    # Add leading zero if number is less than 10
    if num < 10:
        num_str = '0' + num_str

    # Replace each digit with its Persian equivalent
    persian_num_str = ''.join(persian_digits[digit] for digit in num_str)

    return persian_num_str