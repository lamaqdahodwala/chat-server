from tornado.web import Application, url, RequestHandler
from tornado.ioloop import IOLoop

class HomeHandler(RequestHandler):
    def get(self):
        self.write('pranked')

def prepare_app():
    print('preparing app')
    return Application([
        url(r'/', HomeHandler)
    ])
app = prepare_app()
print('listening')
port = 8888
app.listen(port)
print('server started')
print(f'127.0.0.1:{port}')
IOLoop().current().start()