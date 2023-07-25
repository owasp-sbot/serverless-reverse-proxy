from serverless_reverse_proxy.Serverless_Reverse_Proxy import Serverless_Reverse_Proxy

TARGET_SITE__GOOGLE = 'https://www.google.com'

class Reverse_Proxy__Google(Serverless_Reverse_Proxy):

    def __init__(self):
        super().__init__(target_site=TARGET_SITE__GOOGLE)
