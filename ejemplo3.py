# importing the main event loop
import tornado.ioloop

# for HTTP requesthandlers ( to map the requests to request handlers)
import tornado.web

import os.path

class WeatherHandler(tornado.web.RequestHandler):
    def get(self):
        degree = int(self.get_argument("degree"))
        output = "Hot ☀️!" if degree > 20 else "cold 🌦️"
        drink = "Have some Beer 🍺!" if degree > 20 else "you need hot beverage ☕"
        self.render("ejemplo3.html", output = output, drink = drink)

def make_app():
    return tornado.web.Application([
        (r"/weather", WeatherHandler),
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
    # to start ther server on the current thread
    tornado.ioloop.IOLoop.current().start()
