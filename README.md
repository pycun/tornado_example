# Ejemplos con Tornado

En los siguientes pasos mostramos como podemos ejecutar los ejemplos realizados en este repositorio

## Requisitos

- python3.8
- virtualenv
- git

## Crear entorno

Nos posicionamos en nuestra carpeta donde vamos a guardar nuestro proyecto y creamos nuestro entorno

```shell
virtualenv env_tornado_example -p3.8
```

## Clonamos el repositorio

```shell
git clone https://github.com/pycun/tornado_example.git
```

## Activamos el entorno 

```shell
source env_tornado_example/bin/activate
```

## Entramos a la carpeta del proyecto

```shell
cd tornado_example
```

## Instalamos tornado

```shell
pip install tornado
```

O tambien podemos instalar el requirements.txt

```shell
pip install -r requirements.txt
```

## Ejemplos

### Ejemplo 1 - Hola Tornado

```shell
python ejemplo1.py
```

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
```shell
python ejemplo2.py
```
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
```shell
python ejemplo3.py
```
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
```shell
python ejemplo4.py
```
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
### Ejemplo 5 - Chat Demo con Poll

```shell
python chatdemo.py
```

### Ejemplo 6 - Chat Demo con Websocket

```shell
python chatdemowebsocket.py
```