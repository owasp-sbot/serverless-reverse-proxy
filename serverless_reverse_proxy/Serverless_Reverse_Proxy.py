from serverless_reverse_proxy.Reverse_Proxy import Reverse_Proxy


class Serverless_Reverse_Proxy:

    def __init__(self, target_site):
        self.target_site = target_site
        self.reverse_proxy = Reverse_Proxy()