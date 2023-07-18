from unittest import TestCase

from osbot_utils.utils.Dev import pprint
from osbot_utils.utils.Misc import list_set, list_contains, list_contains_list

from serverless_reverse_proxy.sites.Reverse_Proxy__Http_Bin import Reverse_Proxy__Http_Bin, TARGET_SITE__HTTP_BIN


class test_Reverse_Proxy__Http_Bin(TestCase):

    def setUp(self) -> None:
        self.rp_http_bin = Reverse_Proxy__Http_Bin()

    def test__init__(self):
        assert self.rp_http_bin.target_site == TARGET_SITE__HTTP_BIN

    def test_request_get(self):
        query_string = 'aaaa=123'
        response     = self.rp_http_bin.request_get(f'/get?{query_string}')

        assert list_set(response)                == ['content', 'content_type', 'headers', 'json', 'status_code', 'text']
        assert list_set(response.get('headers')) == ['Access-Control-Allow-Credentials', 'Access-Control-Allow-Origin',
                                                     'Connection', 'Content-Length', 'Content-Type',
                                                     'Date', 'Server']
        assert list_set(response.get('json'   )) == ['args', 'headers', 'origin', 'url']
        assert response.get('json').get('args' ) == {'aaaa': '123'}

        #assert self.rp_http_bin.request_get('/get') == self.rp_http_bin.request_get('get')

    def test_request_post(self):
        query_string = 'aaaa=123&bbb=aaa'
        post_data    = "post=data&goes=here"
        headers      = {}
        response     = self.rp_http_bin.request_post(f'/post?{query_string}', post_data=post_data, headers=headers)

        assert list_contains_list(list_set(response.get('headers')), ['Connection', 'Content-Length', 'Content-Type', 'Date', 'Server'] )
        assert list_set(response)                == ['content', 'content_type', 'headers', 'json', 'status_code', 'text']
        assert list_set(response.get('json'   )) == ['args', 'data', 'files', 'form', 'headers', 'json', 'origin', 'url']
        assert response.get('json').get('args' ) == {'aaaa': '123', 'bbb': 'aaa'}
        assert response.get('json').get('data' ) == 'post=data&goes=here'
        assert response.get('json').get('files') == {}
        assert response.get('json').get('form' ) == {}

        query_string = 'now=with&form=urlencoded'
        headers = {'Content-Type' : 'application/x-www-form-urlencoded',
                   'aaaa'         : 'bbbb'                             }
        response = self.rp_http_bin.request_post(f'/post?{query_string}', post_data=post_data, headers=headers)

        pprint(response)
        return
        assert list_contains_list(list_set(response.get('headers')), ['Connection', 'Content-Length', 'Content-Type', 'Date', 'Server'] )
        assert list_set(response)                == ['content', 'content_type', 'headers', 'json', 'status_code', 'text']
        assert list_set(response.get('json'   )) == ['args', 'data', 'files', 'form', 'headers', 'json', 'origin', 'url']
        assert response.get('json').get('args' ) == {'form': 'urlencoded', 'now': 'with'}
        assert response.get('json').get('data' ) == ''
        assert response.get('json').get('files') == {}
        assert response.get('json').get('form' ) == {'goes': 'here', 'post': 'data'}

