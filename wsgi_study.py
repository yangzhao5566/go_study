# coding = utf-8

from wsgiref.simple_server import make_server


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']


if __name__ == "__main__":
    httpd = make_server('', 9999, application)
    print("Serving HTTP on port 9999...")
    httpd.serve_forever()
    