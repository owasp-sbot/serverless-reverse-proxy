from bs4 import BeautifulSoup
from osbot_utils.utils.Dev import pprint
from osbot_utils.utils.Misc import replace


class Step_4__Response__Transform:

    def __init__(self, reverse_proxy):
        self.reverse_proxy   = reverse_proxy

    def run(self, page_title=None, text_replaces=None):
        response      = self.reverse_proxy.step_3__request__execute.response()
        try:
            if response:
                response_text = response.get('text')
                if response_text:
                    soup              = BeautifulSoup(response_text, 'html.parser')
                    if page_title and soup.title:
                        soup.title.string = page_title
                        response['text']  = str(soup)
                    if text_replaces and isinstance(text_replaces, dict):
                        for key,value in text_replaces.items():
                            response['text'] = replace(response['text'], key, value)
        except Exception as error:
            print(f'Error in Step_4__Response__Transform: {error}') # todo: send error to global error handling system
        return response