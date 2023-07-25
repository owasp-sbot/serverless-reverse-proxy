from unittest import TestCase

from osbot_utils.utils.Dev import pprint

from serverless_reverse_proxy.Reverse_Proxy import Reverse_Proxy


class test_Reverse_Proxy(TestCase):

    def setUp(self) -> None:
        self.reverse_proxy = Reverse_Proxy()

    def test_run(self):
        request_payload = {"url"}
        response = self.reverse_proxy.run(request_payload)
        pprint(response)


