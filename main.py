from tornado.web import Application, url, RequestHandler
from tornado.ioloop import IOLoop

class HomeHandler(): pass

def prepare_app():
    return Application([
        url(r'/', HomeHandler)
    ])
app = prepare_app()
app.listen(8888)
IOLoop().current().start()
print('server started')