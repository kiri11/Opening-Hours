from http.server import HTTPServer, BaseHTTPRequestHandler, HTTPStatus
from opening_hours import OpeningHours
from io import BytesIO

PORT = 8000


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        response = BytesIO()
        try:
            schedule = OpeningHours(body)
            resp_text = str(schedule)
            self.send_response(HTTPStatus.OK)
        except Exception as e:
            resp_text = str(e)
            self.send_response(HTTPStatus.BAD_REQUEST)
        self.end_headers()
        response.write(bytes(resp_text, encoding='utf-8'))
        self.wfile.write(response.getvalue())


if __name__ == "__main__":
    httpd = HTTPServer(('localhost', PORT), SimpleHTTPRequestHandler)
    httpd.serve_forever()
