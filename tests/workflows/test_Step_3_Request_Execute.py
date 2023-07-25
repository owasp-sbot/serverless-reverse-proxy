from unittest import TestCase

from osbot_utils.utils.Dev import pprint
from osbot_utils.utils.Misc import random_string

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
        test_url = 'https://postman-echo.com/get'
        with self.step_3_request_execute as _:
            _.setup(method='GET', url=test_url)
            assert _.run() == _.response()
            assert test_url in _.response().text
