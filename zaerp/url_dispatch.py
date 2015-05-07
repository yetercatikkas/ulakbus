__author__ = 'evren kutar'
# from zdispatch.dispatcher import app
from lib.views import SimpleView
import falcon

app = falcon.API()


class LoginView():
    # def __init__(self, current):
    #     super(SimpleView, self).__init__(current)
    #     if current.request.context.jsonin.get('cmd', '') == 'do':
    #         self._do()
    #     else:
    #         self._show()

    def on_get(self, req, resp):
        print req.context
        try:
            if req.context.get('cmd', '') == 'do':
                self._do(resp)
            else:
                self._show(resp)
        except:

            self._do(resp)

    def _do(self, resp):
        resp.status = falcon.HTTP_200
        resp.body = ('this is do func')
        return resp

    def _show(self, resp):
        resp.status = falcon.HTTP_200
        resp.body = ('this is show func')
        return resp


view = LoginView()
app.add_route('/login', view)