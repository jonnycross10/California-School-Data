import requests
from requests.structures import CaseInsensitiveDict

url = "https://api.caschooldashboard.org/LocalIndicators/31669280000000/7/Reports/1-2-3-6-7-9-10"

headers = CaseInsensitiveDict()
headers["Connection"] = "keep-alive"
headers["sec-ch-ua"] = "' Not;A Brand';v='99', 'Google Chrome';v='97', 'Chromium';v='97'"
headers["Accept"] = "application/json, text/plain, */*"
headers["Content-Type"] = "application/json"
headers["sec-ch-ua-mobile"] = "?0"
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
headers["sec-ch-ua-platform"] = "'Windows'"
headers["Origin"] = "https://www.caschooldashboard.org"
headers["Sec-Fetch-Site"] = "same-site"
headers["Sec-Fetch-Mode"] = "cors"
headers["Sec-Fetch-Dest"] = "empty"
headers["Referer"] = "https://www.caschooldashboard.org/"
headers["Accept-Language"] = "en-US,en;q=0.9,ja-JP;q=0.8,ja;q=0.7"


resp = requests.get(url, headers=headers)

print(resp.status_code)

