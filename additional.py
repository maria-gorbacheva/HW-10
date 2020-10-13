import requests
import time
from datetime import datetime

def q_2_days():
    now = datetime.now()
    time_utc = int(time.mktime(now.timetuple()))
    time_dif = time_utc - 2*60

    has_more = True
    j = 1
    while has_more is True:
        params = {
            'tagged': 'Python',
            'fromdate': time_dif, 'todate': time_utc,
            'page': j,
            'sort': 'creation',
            'pagesize': '100',
            'site': 'stackoverflow'
        }
        response = requests.get('https://api.stackexchange.com/2.2/questions', params=params)


        data = response.json()['items']
        j += 1
        with open('result.txt', 'w', encoding='utf-8') as f:
            for item in data:
                #print(item['title'])
                f.write(item['title'])
                f.write('\n')
                #print()
        has_more = response.json()['has_more']

q_2_days()