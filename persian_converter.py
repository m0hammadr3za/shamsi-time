persian_months = [
        "فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور",
        "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"
    ]

persian_english_week_days_map = {
    "یکشنبه": "sunday", 
    "دوشنبه": "monday", 
    "سه شنبه": "tuesday", 
    "چهارشنبه": "wednesday", 
    "پنج شنبه": "thursday", 
    "جمعه": "friday", 
    "شنبه": "saturday"
}

persian_days = list(persian_english_week_days_map.keys())

def find_persian_month_name_in_text(text):
    for month_name in persian_months:
        if month_name in text:
            return month_name
        
    return None

def find_persian_day_name_in_text(text):
    for day_name in persian_days:
        if day_name in text:
            return day_name
    
    return None

def convert_to_persian_number(num):
    persian_digits = {
        '0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '۴',
        '5': '۵', '6': '۶', '7': '۷', '8': '۸', '9': '۹'
    }

    num_str = str(num)

    # Add leading zero if number is less than 10
    if num < 10:
        num_str = '0' + num_str

    # Replace each digit with its Persian equivalent
    persian_num_str = ''.join(persian_digits[digit] for digit in num_str)

    return persian_num_str

def get_persian_month_from_index(month_index):
    return persian_months[month_index]

def get_persian_day_from_index(day_index):
    return persian_days[day_index]

def get_persian_english_week_days_map():
    return persian_english_week_days_map