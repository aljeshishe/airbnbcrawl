import email
import json
from pathlib import Path

import requests
import re
url = 'https://www.airbnb.ru/s/Antalya/homes?tab_id=home_tab&refinement_paths[]=%2Fhomes&date_picker_type=calendar&checkin=2022-12-01&checkout=2022-12-31&adults=1&source=structured_search_input_header&search_type=filter_change&price_filter_num_nights=30&query=Antalya&price_max=96&price_min=1&flexible_trip_lengths[]=one_month&flexible_trip_dates[]=november&drawer_open=false'

headers_str = '''accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
accept-encoding: gzip, deflate, br
accept-language: en-US,en;q=0.9,ru;q=0.8
cache-control: max-age=0
device-memory: 8
dpr: 2
ect: 3g
referer: https://www.airbnb.com/s/Antalya/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&date_picker_type=calendar&checkin=2022-12-01&checkout=2022-12-31&adults=1&source=structured_search_input_header&search_type=filter_change&price_filter_num_nights=30&query=Antalya&flexible_trip_lengths%5B%5D=one_month&flexible_trip_dates%5B%5D=november&drawer_open=false&locale=en&_set_bev_on_new_domain=1666033968_YmE4Mzk5Yjc2MzBj&display_currency=USD
sec-ch-ua: "Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "macOS"
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: same-origin
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36
viewport-width: 1792z'''

headers = email.message_from_string(headers_str)
response = requests.get(url=url, headers=headers)
response.raise_for_status()
Path('dump.html').write_bytes(response.content)

found = re.search('<script id="data-state" data-state="true" type="application/json">(.+?)</script>', response.text).groups()[0]
Path('data.json').write_text(found)
data = json.loads(found)
print(data)


