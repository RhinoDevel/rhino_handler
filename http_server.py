#!/usr/bin/python

# Marcel Timm, RhinoDevel, 2022jul23

from http.server import HTTPServer, BaseHTTPRequestHandler

import responder_rhasspy

ADDR = '127.0.0.1' # Use this in an intranet, only (no security stuff at all).
PORT = 7581

class MtHttpHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_POST(self):
        req_content_len = int(self.headers["Content-Length"])
        req_body = self.rfile.read(req_content_len).decode() # 'utf-8'?

        response_body = responder_rhasspy.exec_with_str(req_body)

        self._set_headers()
        self.wfile.write(response_body.encode('utf8'))

def exec():
    httpd = HTTPServer((ADDR, PORT), MtHttpHandler)

    httpd.serve_forever()

if __name__ == "__main__":
    exec()