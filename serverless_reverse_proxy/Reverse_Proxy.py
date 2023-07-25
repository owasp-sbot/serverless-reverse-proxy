from serverless_reverse_proxy.workflow.Step_1__Request__Receive import Step_1__Request__Receive


class Reverse_Proxy:

    def __init__(self):
        self.step_1__request__receive    = Step_1__Request__Receive(self)
        # self.step_2__request__execute    = Step_2__Request__Execute(self)
        # self.step_3__request__transform  = Step_3__Request__Transform(self)
        # self.step_4__response__transform = Step_4__Response__Transform(self)
        # self.step_5__response__return    = Step_5__Response__Return(self)

    def run(self, request_payload):
        self.step_1__request__receive.run(request_payload)