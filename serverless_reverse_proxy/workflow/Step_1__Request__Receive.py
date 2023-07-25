class Step_1__Request__Receive:

    def __init__(self, reverse_proxy):
        self.reverse_proxy   = reverse_proxy
        self.request_payload = None

    def run(self, request_payload):
        self.request_payload = request_payload
        return self