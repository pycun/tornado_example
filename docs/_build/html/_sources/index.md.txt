# Introducción a Tornado

![image](https://user-images.githubusercontent.com/56738048/209691837-f6cf9c29-f15a-40ab-947d-b6cc9a1e92ec.png)

## ¿Que es Tornado?

- Un framework asyncrono
- Framework Python Open Source
- Desarrollado por FriendFeed y comprado por Facebook en 2009
- Resuelve el problema C10k
 

## Tornado se divide en 4 componentes

- Web Framework, (RequestHandler) para crear aplicaciones web
- Servidores y clientes asincrónicos
- Libreria asincrona
- Corutinas y otras primitivas

## Instalación

```
pip install tornado
```

## Ejemplos

### Ejemplo 1 - Hola Tornado
**ejemplo1.py**
```python
# importing the main event loop
import tornado.ioloop

# for HTTP requesthandlers ( to map the request to request handlers)
import tornado.web

class HelloHandler(tornado.web.RequestHandler):

    def get(self):
        self.write('Hello, Tornado 🌪️!')

def make_app():

    return tornado.web.Application([
        (r"/", HelloHandler),
    ],
    debug = True,
    autoreload = True)

if __name__ == "__main__":
    app = make_app()
    port = 8888
    app.listen(port)
    print(f'🌐 Server is listening on localhost on port {port}')
    # to start ther server on the curren thread
    tornado.ioloop.IOLoop.current().start()
```

### Ejemplo 2 - Hola Tornado 2
**ejemplo2.py**
```python
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

```
**ejemplo2.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Hola Tornado</title>
</head>
<body>
  <p>
      {{ message }}
  </p>
</body>
</html>
```
### Ejemplo 3 - ¿Hace calor o frio? | GET
**ejemplo3.py**
```python
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
        self.render("weather.html", output = output, drink = drink)

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

```
**ejemplo3.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome, Tornado 🌪️</title>
</head>
<body>
    <h1>Welcome, Tornado 🌪️</h1>
    <h2>Using Arguments For Data Query in Tornado </h2>
    <hr>
    Today is ...
    {{ output }}
    <br>
    <br>
    {{ drink }}
</body>
</html>
```
### Ejemplo 4 - ¿Hace calor o frio? | POST
**ejemplo4.py**
```python
# importing the main event loop
import tornado.ioloop

# for HTTP requesthandlers ( to map the requests to request handlers)
import tornado.web

import os.path

class WeatherHandler(tornado.web.RequestHandler):

    def get(self):

        self.render("ejemplo4.html", output="")

    def post(self):
        degree = int(self.get_argument("degree"))
        output = "Hot ☀️!" if degree > 20 else "cold 🌦️"
        drink = "Have some Beer 🍺!" if degree > 20 else "you need hot beverage ☕"
        self.render("ejemplo4.html", output = output, drink = drink)

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
```
**ejemplo4.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome, Tornado 🌪️</title>
</head>
<body>
    <h1>Welcome, Tornado 🌪️</h1>
    <h2>Using Arguments For Data Query in Tornado </h2>

    <h3>Form</h3>

    <form action="" method="post">
        <label for="">degree</label>
        <input type="text" name="degree" value="">
        <input type="submit">
    </form>

    {% if output %}
        <hr>
    Today is ...
    {{ output }}
    <br>
    <br>
    {{ drink }}
    {% end %}
</body>
</html>
```