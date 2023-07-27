from urllib.parse import urljoin

from serverless_reverse_proxy.workflow.Step_1__Request__Receive import Step_1__Request__Receive
from serverless_reverse_proxy.workflow.Step_3__Request__Execute import Step_3__Request__Execute
from serverless_reverse_proxy.workflow.Step_4__Response__Transform import Step_4__Response__Transform


class Reverse_Proxy:

    def __init__(self):
        self.step_1__request__receive    = Step_1__Request__Receive(self)
        #self.step_2__request__transform  = Step_2__Request__Transform(self)
        self.step_3__request__execute    = Step_3__Request__Execute()
        self.step_4__response__transform = Step_4__Response__Transform(self)
        # self.step_5__response__return    = Step_5__Response__Return(self)

    def run__via__target_site__path(self, method, target_site, path, params=None, data=None, headers=None):

        url = urljoin(target_site, path)
        #self.step_1__request__receive.run()
        self.step_3__request__execute.setup(method=method, url=url, params=params, data=data, headers=headers)
        self.step_3__request__execute.run()
        return self.step_3__request__execute.response()