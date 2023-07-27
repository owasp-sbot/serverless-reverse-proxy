from bs4 import BeautifulSoup
from osbot_utils.utils.Dev import pprint
from osbot_utils.utils.Misc import replace


class Step_4__Response__Transform:

    def __init__(self, reverse_proxy):
        self.reverse_proxy   = reverse_proxy

    def run(self, page_title, text_replaces):
        response      = self.reverse_proxy.step_3__request__execute.response()
        if response:
            response_text = response.get('text')
            soup          = BeautifulSoup(response_text, 'html.parser')



            soup.title.string = page_title
            response['text'] = str(soup)

            for key,value in text_replaces.items():
                response['text'] = replace(response['text'], key, value)

        return response