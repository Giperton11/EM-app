#!/usr/bin/env python3

#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler
import logging
import os

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            response = "Hello from Effective Mobile!"
            self.wfile.write(response.encode('utf-8'))
            logging.info("Served 200 to %s", self.client_address)
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(b'Not Found')
            logging.warning("404 for path: %s from %s", self.path, self.client_address)

    def log_message(self, format, *args):
        # Переопределяем стандартный вывод в stderr на logging
        logging.info("%s - %s", self.address_string(), format % args)


def run_server():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
    )

    PORT = int(os.getenv("BACKEND_PORT", "8080"))           # ← здесь
    server_address = ('0.0.0.0', PORT)                      # ← здесь
    httpd = HTTPServer(server_address, SimpleHandler)
    logging.info('Server starting on http://0.0.0.0:8080')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        logging.info('Server stopped by user')
    finally:
        httpd.server_close()


if __name__ == '__main__':
    run_server()
