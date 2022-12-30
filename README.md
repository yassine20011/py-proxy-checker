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

# this will return a list of proxies that are working and the speed of the proxy
print(P.check("proxies.txt"))

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


