from bs4 import BeautifulSoup
from osbot_utils.utils.Dev import pprint
from osbot_utils.utils.Misc import replace


TEXT_REPLACES = {
                    'TEST'                                      : 'TEST (via Lambda !!)'                                    ,
                    'https://hollandbarretttest.24sessions.com' : "https://ihboa0cikj.execute-api.eu-west-2.amazonaws.com"  ,
                    'Pick a meeting'                            : 'Select a meeting'
                 }
PAGE_TITLE    = "This is the proxied 24 Sessions"

class Step_4__Response__Transform:

    def __init__(self, reverse_proxy):
        self.reverse_proxy   = reverse_proxy

    def run(self):
        response      = self.reverse_proxy.step_3__request__execute.response()
        if response:
            response_text = response.get('text')
            soup          = BeautifulSoup(response_text, 'html.parser')



            soup.title.string = PAGE_TITLE
            response['text'] = str(soup)

            for key,value in TEXT_REPLACES.items():
                response['text'] = replace(response['text'], key, value)

        return response