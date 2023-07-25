from unittest import TestCase

from osbot_utils.utils.Dev import pprint
from osbot_utils.utils.Misc import random_string, list_set

from serverless_reverse_proxy.workflow.Step_3__Request__Execute import Step_3_Request_Execute


class test_Step_3_Request_Execute(TestCase):

    def setUp(self):
        self.step_3_request_execute = Step_3_Request_Execute()

    def test__init__(self):
        with self.step_3_request_execute as _:
            assert _.method       is None
            assert _.url          is None
            assert _.params       is None
            assert _.data         is None
            assert _.headers      is None
            assert _.raw_response is None


    def test_setup(self):
        random_method  = random_string()
        random_url     = random_string()
        random_params  = random_string()
        random_data    = random_string()
        random_headers = random_string()
        with self.step_3_request_execute as _:
            _.setup(method=random_method, url= random_url, params=random_params, data=random_data, headers=random_headers)
            assert _.method        == random_method
            assert _.url           == random_url
            assert _.params        == random_params
            assert _.data          == random_data
            assert _.headers       == random_headers
            assert _.raw_response is None

    def test_run(self):
        test_url     = 'https://postman-echo.com/get'
        query_string = 'aaaa=123'
        with self.step_3_request_execute as _:
            _.setup(method='GET', url=test_url, params=query_string)
            response = _.run()

            response_headers = response.get('headers'   )
            response_json    = response.get('json'   )

            assert response == _.response()
            assert list_set(response)                == ['content', 'content_type', 'headers', 'json', 'status_code', 'text']
            assert list_set(response_headers) == ['Connection', 'Content-Length', 'Content-Type', 'Date', 'ETag', 'set-cookie']
            assert list_set(response_json   ) == ['args', 'headers', 'url']
            assert response_json.get('args' ) == {'aaaa': '123'           }
            assert response_json.get('url'  ) == f"{test_url}?{query_string}"
            assert list_set(response_json.get('headers')) == ['accept', 'accept-encoding', 'host', 'user-agent', 'x-amzn-trace-id', 'x-forwarded-port', 'x-forwarded-proto']
