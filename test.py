import requests
from bs4 import BeautifulSoup
from collections import OrderedDict

###############################################
base_url = r"https://www.google.com/search?"
delim = r"&"
delim_q = r"="


###############################################
def build_search_string(search_params):
    fin_url = base_url
    for param, value in search_params.items():
        if value != '':
            fin_url = fin_url + delim + param + delim_q + value
    return fin_url


def search_GOOG(search_params):
    response = requests.get(build_search_string(search_params))
    soup = BeautifulSoup(response.content, "html.parser")
    return soup

def validate_results():
    soup = search_GOOG(search_params)
    # print(soup.prettify())
    # print('#'*100)
    for link in soup.find_all('a'):
        if (link.get('href').find('url')) == 1 & (link.get('href').find('modi')) == 1:
            print(link.get('href'))
            print('Test passed')



search_params = OrderedDict([
    ('q', 'Modi'),
    ('oq', 'Modi'),
    ('aqs', 'Chrome'),
    ('tbm', 'nws'),
    ('sa', '')
])


validate_results()
