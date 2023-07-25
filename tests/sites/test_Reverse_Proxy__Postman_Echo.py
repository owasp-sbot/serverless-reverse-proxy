from unittest import TestCase

from osbot_utils.testing.Duration import Duration
from osbot_utils.utils.Dev import pprint
from osbot_utils.utils.Misc import list_set, list_contains, list_contains_list

from serverless_reverse_proxy.sites.Reverse_Proxy__Postman_Echo import Reverse_Proxy__Postman_Echo, TARGET_SITE__POSTMAN_ECHO


class test_Reverse_Proxy__Http_Bin(TestCase):

    def setUp(self) -> None:
        self.rp_postman_echo = Reverse_Proxy__Postman_Echo()

    def test__init__(self):
        assert self.rp_postman_echo.target_site == TARGET_SITE__POSTMAN_ECHO

    def test_request_get(self):
        query_string = 'aaaa=123'
        response     = self.rp_postman_echo.request_get(f'/get?{query_string}')

        assert list_set(response)                == ['content', 'content_type', 'headers', 'json', 'status_code', 'text']
        assert list_set(response.get('headers')) == ['Connection', 'Content-Length', 'Content-Type', 'Date', 'ETag', 'set-cookie']
        assert list_set(response.get('json'   )) == ['args', 'headers', 'url']
        assert response.get('json').get('args' ) == {'aaaa': '123'}

    def test_request_post(self):
        query_string = 'aaaa=123&bbb=aaa'
        post_data    = "post=data&goes=here"
        headers      = {}
        response     = self.rp_postman_echo.request_post(f'/post?{query_string}', post_data=post_data, headers=headers)

        assert list_set(response.get('headers')) == ['Connection', 'Content-Length', 'Content-Type', 'Date', 'ETag', 'set-cookie']
        assert list_set(response)                == ['content', 'content_type', 'headers', 'json', 'status_code', 'text']
        assert list_set(response.get('json'   )) == ['args', 'data', 'files', 'form', 'headers', 'json', 'url']
        assert response.get('json').get('args' ) == {'aaaa': '123', 'bbb': 'aaa'}
        assert response.get('json').get('data' ) == 'post=data&goes=here'
        assert response.get('json').get('files') == {}
        assert response.get('json').get('form' ) == {}

        query_string = 'now=with&form=urlencoded'
        headers = {'Content-Type' : 'application/x-www-form-urlencoded',
                   'aaaa'         : 'bbbb'                             }
        response = self.rp_postman_echo.request_post(f'/post?{query_string}', post_data=post_data, headers=headers)

        assert list_set(response)                == ['content', 'content_type', 'headers', 'json', 'status_code', 'text']
        assert list_set(response.get('json'   )) == ['args', 'data', 'files', 'form', 'headers', 'json', 'url']
        assert response.get('json').get('args' ) == {'form': 'urlencoded', 'now': 'with'}
        assert response.get('json').get('data' ) == ''
        assert response.get('json').get('files') == {}
        assert response.get('json').get('form' ) == {'goes': 'here', 'post': 'data'}

