# importing the main event loop
import tornado.ioloop

# for HTTP requesthandlers ( to map the request to request handlers)
import tornado.web

import os.path

class HelloHandler(tornado.web.RequestHandler):

    def get(self):
        message = 'Hello, Tornado 🌪️!'
        self.render("ejemplo2.html", message=message)

def make_app():

    return tornado.web.Application([
        (r"/", HelloHandler),
    ],
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    debug = True,
    autoreload = True)

if __name__ == "__main__":
    app = make_app()
    port = 8888
    app.listen(port)
    print(f'🌐 Server is listening on localhost on port {port}')
    # to start ther server on the curren thread
    tornado.ioloop.IOLoop.current().start()
