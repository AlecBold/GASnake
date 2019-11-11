#! /usr/bin/python3

from os import curdir, sep, environ
from http.server import HTTPServer, BaseHTTPRequestHandler
from index import Model

PORT_NUMBER = 80
SERVER_ADDRESS = ("gasnake.herokuapp.com", PORT_NUMBER)

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
        print('GET REQUEST')
        try:
            if file_data:
                file_path = curdir + sep + file_data['path'].replace('/', sep)
                file_type = file_data['type']

                self.send_response(200)
                self.send_header('Content-type', file_type)
                self.end_headers()

                with open(file_path, 'rb') as file:
                    self.wfile.write(file.read())

            return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)


try:
    server = HTTPServer(SERVER_ADDRESS, Handler)
    print('Im here')
    #model = Model()
    print('Started httpserver on port ', PORT_NUMBER)

    #model.run_process()
    server.serve_forever()

except KeyboardInterrupt:
    print('^C received, shutting down the web server')
    #model.stop_process()
    server.socket.close()
