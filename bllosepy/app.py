from wsgiref.simple_server import make_server


def Web_App(environment, response):
    status = "200 OK"
    headers = [("content-type", "text/html; charset=utf-8")]
    response(status, headers)
    return [b"<h2>Hi there, this is WSGI server</h2>"]


with make_server("", 5000, Web_App) as server:
    print(
        "serving on port 5000...\nvisit http://127.0.0.1:5000\nTo exit press ctrl + c"
    )
    server.serve_forever()