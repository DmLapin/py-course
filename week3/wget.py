import sys
import requests


url = sys.argv[1]

try:
    response = requests.get(url, timeout=30)
    response.raise_for_status()
except requests.Timeout:
    print("timeout err, url:", url)
except requests.HTTPError as err:
    code = err.response.status_code
    print("http err for url {0}, code {1}".format(url, code))
except requests.RequestException:
    print("base request exception")
else:
    print(response.content)
