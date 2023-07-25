import requests

class Step_3_Request_Execute:

    def __init__(self):
        self.method       = None
        self.url          = None
        self.params       = None
        self.data         = None
        self.headers      = None
        self.raw_response = None

    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, exc_tb): return False

    def setup(self, method, url, params=None, data=None, headers=None):
        self.method  = method                           # todo: add validation for multiple types of methods
        self.url     = url                              # todo: add validation to make sure it is an url
        self.params  = params                           # todo: add validation to check if it is valid url params
        self.data    = data                             # todo: add validation to check if it is valid post data (according to provided headers)
        self.headers = headers                          # todo: add validation to check if it is a dict and has valid headers names & values

    def run(self):
        kwargs =  dict( method  = self.method  ,
                        url     = self.url     ,
                        params  = self.params  ,
                        data    = self.data    ,
                        headers = self.headers )
        self.raw_response = requests.request(**kwargs)
        return self.response()

    def response(self):
        if self.raw_response is None:
            return {}

        status_code    = self.raw_response.status_code
        headers        = dict(self.raw_response.headers)
        content_type   = headers.get('Content-Type')
        text           = ''
        json           = None
        content        = None
        if content_type.startswith('application/json'):
            json = self.raw_response.json()
        else:
            text = self.raw_response.text

        return dict(content_type = content_type,
                    status_code  = status_code ,
                    content      = content     ,
                    json         = json        ,
                    text         = text        ,
                    headers      = headers     )
