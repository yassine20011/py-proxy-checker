# py-proxy-checker
<img src="https://img.shields.io/pypi/dm/py-proxy-checker?logo=pypi&logoColor=white">

This is a simple python script to check if a proxy is working or not and to check the speed of the proxy.

## Installation

```bash
pip install py-proxy-checker
```

## Usage

```python
from proxychecker import Checker
checker = Checker()

#Check the proxies in the file "proxies.txt"
proxies = checker.check("proxies.txt")
print(proxies)

    {
    ...
    2: {
    'proxy': '77.109.178.218:80',
    'Timeout': 529},
    ...
    }

#Get the information of the proxy
print(checker.info(proxies[2]['proxy']))

    {
        'ip': '210.245.124.131',
        'network': '210.245.112.0/20',
        'version': 'IPv4',
        ...
    }


proxy_list = [proxies[proxy]['proxy'] for proxy in proxies]

#Get the information of each proxy in the list
print(checker.info(proxy_list=proxy_list))

    [
        ...,
        {
        'ip': '210.245.124.131',
        'network': '210.245.112.0/20',
        'version': 'IPv4',
        ...
        },
        ...
    ]
    
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
