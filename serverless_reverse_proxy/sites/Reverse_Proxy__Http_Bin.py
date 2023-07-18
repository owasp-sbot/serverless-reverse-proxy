from urllib.parse import urljoin

import requests
from osbot_utils.decorators.methods.cache_on_tmp import cache_on_tmp

from serverless_reverse_proxy.Serverless_Reverse_Proxy import Serverless_Reverse_Proxy

TARGET_SITE__HTTP_BIN = 'https://httpbin.org'

class Reverse_Proxy__Http_Bin(Serverless_Reverse_Proxy):

    def __init__(self):
        super().__init__(target_site=TARGET_SITE__HTTP_BIN)

    def request_get(self, path='', headers=None):
        return self.request('GET', path, headers=headers)

    def request_post(self, path='', post_data=None, headers=None):
        return self.request('POST', path, data=post_data, headers=headers)

    @cache_on_tmp(reload_data=False)                    # todo: add native support for caching
    def request(self, method, path, data=None, headers=None):
        url            = urljoin(self.target_site, path)
        request_kwargs = dict(method  = method ,
                              url     = url    ,
                              data    = data   ,
                              headers = headers)
        response       = requests.request(**request_kwargs)

        status_code    = response.status_code
        headers        = dict(response.headers)
        content_type   = headers.get('Content-Type')
        text           = ''
        json           = None
        content        = None
        if content_type == 'application/json':
            json = response.json()
        else:
            text = response.text

        return dict(content_type = content_type,
                    status_code  = status_code ,
                    content      = content     ,
                    json         = json        ,
                    text         = text        ,
                    headers      = headers     )
