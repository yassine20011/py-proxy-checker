''' Requirements '''

import requests


class Checker():
    """Proxy Checker is a python package that allows you to check the validity of a proxy,
    >>> from proxychecker import Checker
    >>> checker = Checker()
    >>> proxies = checker.check("proxies.txt")
    >>> print(proxies)
    {
    ...
    2: {
    'proxy': '77.109.178.218:80', 
    'Timeout': 529}
    ...
    }
    >>> print(checker.info(proxies[2]['proxy']))
    {
        'ip': '210.245.124.131', 
        'network': '210.245.112.0/20', 
        'version': 'IPv4', 
        ...
    }

    also you can check the proxy information of a list of proxies
    >>> list = [proxies[proxy]['proxy'] for proxy in proxies]
    >>> print(checker.info(proxy_list=list))
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

    """

    def __init__(self):
        pass

    def check(self, filename: str):
        """This function will check the proxy and return a dictionary of working proxies,

            param filename: The path of the file containing the proxies as a string
            return: A dictionary of working proxies

        """

        with open(filename, 'r') as file_:
            http_proxy = [str(line) for line in file_]

        working_proxy = {}
        counter = 0
        for line in http_proxy:

            proxy_dict = {"http": f"http://{line}"}

            try:
                url = "http://httpbin.org/ip"

                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) \
                    AppleWebKit/537.36 (KHTML, like Gecko) \
                    Chrome/41.0.2228.0 Safari/537.36'}
                response = requests.get(
                    url, proxies=proxy_dict, headers=headers, timeout=1.9)

                proxy_dict = {}
                if response.status_code == 200:

                    proxy_dict["proxy"] = line.replace("\n", "")
                    proxy_dict["Timeout"] = int(
                        response.elapsed.total_seconds() * 1000)

                    working_proxy[counter] = proxy_dict
                    counter += 1

            except Exception:
                pass

        return working_proxy

    def info(self, ip: str = None, proxy_list: list[str] = None):
        """This function will return the proxy information,

        :param ip: The ip address of the proxy
        :param proxy_list: (Optional) Check the proxy information of a list of proxies

        :return: A dictionary of the proxy information or a list of dictionaries of the proxy information

        """

        try:
            if proxy_list is not None:
                info_list = []
                for proxy in proxy_list:
                    url = f"https://ipapi.co/{proxy.split(':')[0] }/json/"
                    response = requests.get(url)
                    response.raise_for_status()
                    if response.status_code != 204:
                        info_list.append(response.json())
                    else:
                        info_list.append(
                            f'Invalid IP Address {proxy.split(":")[0]} or something went wrong')
                return info_list
            elif ip is not None:
                url = f"https://ipapi.co/{ip.split(':')[0]}/json/"
                response = requests.get(url)
                response.raise_for_status()
                if response.status_code != 204:
                    return response.json()
                else:
                    return f'Invalid IP Address {ip} or something went wrong'
        except requests.exceptions.ConnectionError as e:
            raise requests.exceptions.ConnectionError(
                "Please check your internet connection and try again"
            ) from e
