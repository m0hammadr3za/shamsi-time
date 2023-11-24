import requests
from bs4 import BeautifulSoup

def get_shamsi_time_info_online_impl():
    url = 'https://time.ir'
    response = requests.get(url, timeout=3)

    soup = BeautifulSoup(response.content, 'html.parser')

    # Extracting the Shamsi date and time
    shamsi_time_soup = soup.find('div', {'class': 'today-shamsi'})
    shamsi_time_spans = shamsi_time_soup.find_all('span')

    date_text_elements = shamsi_time_spans[1].text.split('/')
    year_index = date_text_elements[0]
    month_index = date_text_elements[1]
    day_index = date_text_elements[2]

    descriptive_date_elements = shamsi_time_spans[2].text.split(' ')
    name_of_the_month = descriptive_date_elements[3]
    name_of_the_day = descriptive_date_elements[0]

    time_info = {
        "year": year_index,
        "month": month_index,
        "day": day_index,
        "name_of_the_month": name_of_the_month,
        "name_of_the_day": name_of_the_day
    }

    # Extracting the month occasions
    occasions_soup = soup.find('div', {'class': 'eventsCurrentMonthWrapper'}).find_all('li')

    month_occasions = {}
    for occasion in occasions_soup:
        text_elements = [text.strip() for text in occasion.text.split("\n")]
        date_in_month = text_elements[1].split(' ')[0]
        date_in_month = date_in_month if len(date_in_month) != 1 else f"۰{date_in_month}"

        occasion_description = text_elements[2]

        is_holiday = 'eventHoliday' in occasion.get('class', [])

        if date_in_month in list(month_occasions.keys()):
            previous_description = month_occasions[date_in_month]['occasion']
            month_occasions[date_in_month]['occasion'] = f"{occasion_description}, {previous_description}"
            if is_holiday:
                month_occasions[date_in_month]['is_holiday'] = is_holiday
        else:
            month_occasions[date_in_month] = {
                "occasion": occasion_description,
                "is_holiday": is_holiday
            }

    # Add occasion info if there is any accasions
    if day_index in list(month_occasions.keys()):
        day_occasion = month_occasions[day_index]
        time_info["occasion"] = day_occasion["occasion"]
        time_info["is_holiday"] = day_occasion["is_holiday"]
    
    return time_info
    
def get_shamsi_time_info_online():
    try:
        shamsi_time_info = get_shamsi_time_info_online_impl()
        return shamsi_time_info
    except Exception as e:
        print(f"something went wrong in get_shamsi_time_info_online_impl: {e}")
        return None