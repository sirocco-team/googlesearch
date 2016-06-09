import os
GOOGLE_API_URL_TEMPLATE = \
    'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s'


PROXY_LIST_TEMPLATE = 'socks5://{host}:{port}'
BASE_SOCKS_PORT = os.getenv('BASE_SOCKS_PORT', '9050')
SOCKS_PORT_COUNT = int(os.getenv('SOCKS_PORT_COUNT', '50'))
TOR_HOST = os.getenv('TOR_HOST', 'tornet')

base_port = int(BASE_SOCKS_PORT)
PROXY_LIST = [PROXY_LIST_TEMPLATE.format(host=TOR_HOST, port=p) for p in
              range(base_port, base_port + SOCKS_PORT_COUNT)]
