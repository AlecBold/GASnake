#!/usr/bin/python

from os import curdir, sep
from http.server import HTTPServer, BaseHTTPRequestHandler

PORT_NUMBER = 3000
SERVER_ADDRES = ('localhost', PORT_NUMBER)

DUMB_FILE_MAP = {
    '/'           : {'path': 'client/index.html', 'type': 'text/html'},
    '/index.html' : {'path': 'client/index.html', 'type': 'text/html'},

    '/coords.json': {'path': 'data/coords.json',    'type': 'application/json'},

    '/style.css'  : {'path': 'client/style.css',  'type': 'text/css'},
    '/display.js' : {'path': 'client/display.js', 'type': 'application/javascript'},
    '/engine.js'  : {'path': 'client/engine.js',  'type': 'application/javascript'},
    '/main.js'    : {'path': 'client/main.js',    'type': 'application/javascript'},
    '/utils.js'   : {'path': 'client/utils.js',   'type': 'application/javascript'},
    '/favicon.ico': {'path': 'client/favicon/favicon.ico', 'type': 'image/x-icon'},
}

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        file_data = DUMB_FILE_MAP.get(self.path, False)

        try:
            if file_data:
                print(self.path, file_data)
                file_path = curdir + sep + file_data['path'].replace('/', sep)
                file_type = file_data['type']

                self.send_response(200)
                self.send_header('Content-type', file_type)
                self.end_headers()
                print("FILE PATH : ", file_path)
                with open(file_path, 'rb') as file:
                    self.wfile.write(file.read())

            return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)


try:
    server = HTTPServer(SERVER_ADDRES, Handler)
    print('Started httpserver on port ', PORT_NUMBER)

    server.serve_forever()

except KeyboardInterrupt:
    print('^C received, shutting down the web server')
    server.socket.close()
