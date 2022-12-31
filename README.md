# py-proxy-checker


This is a simple python script to check if a proxy is working or not and to check the speed of the proxy.

## Installation

```bash
pip install py-proxy-checker
```

## Usage

```python
from checkerproxy import CheckerProxy

P = CheckerProxy()

# this will return a dictionary of working proxies with timeout
print(P.check("proxies.txt"))

# this will return a dictionary of the proxy information or a list of dictionaries of the proxy information
print(P.info(ip="178.33.198.181", proxy_list=optional)

```

## Output

```python
{1: {'proxy': '65.2.41.162:80', 'Timeout': 657}, 2: {'proxy': '77.109.178.218:80', 'Timeout': 529}, 3: {'proxy': '34.23.45.223:80', 'Timeout': 1114}, 4: {'proxy': '210.245.124.131:5239', 'Timeout': 906}}

{'ip': '210.245.124.131', 'network': '210.245.112.0/20', 'version': 'IPv4', 'city': 'Ho Chi Minh City', 'region': 'Ho Chi Minh', 'region_code': 'SG', 'country': 'VN', 'country_name': 'Vietnam', 'country_code': 'VN', 'country_code_iso3': 'VNM', 'country_capital': 'Hanoi', 'country_tld': '.vn', 'continent_code': 'AS', 'in_eu': False, 'postal': None, 'latitude': 10.8326, 'longitude': 106.6581, 'timezone': 'Asia/Ho_Chi_Minh', 'utc_offset': '+0700', 'country_calling_code': '+84', 'currency': 'VND', 'currency_name': 'Dong', 'languages': 'vi,en,fr,zh,km', 'country_area': 329560.0, 'country_population': 95540395, 'asn': 'AS18403', 'org': 'FPT Telecom Company'}
```



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


