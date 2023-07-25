from serverless_reverse_proxy.Reverse_Proxy import Reverse_Proxy
from serverless_reverse_proxy.Serverless_Reverse_Proxy import Serverless_Reverse_Proxy

TARGET_SITE__GOOGLE = 'https://www.google.com'

class Reverse_Proxy__Google(Serverless_Reverse_Proxy):

    def __init__(self):
        super().__init__(target_site=TARGET_SITE__GOOGLE)
        self.reverse_proxy = Reverse_Proxy()

    def request_get(self, path='', query_string=None):
        return self.reverse_proxy.run__via__target_site__path('GET', target_site=self.target_site, path=path)

