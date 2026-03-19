from webob import Request, Response
from whitenoise import WhiteNoise
import routes

class API:
    def __init__(self, static_dir="assets"):
        self.routes = routes.routes
        self.whitenoise = WhiteNoise(self.wsgi_app, root=static_dir)

    def wsgi_app(self, environ, start_response):
        request = Request(environ)

        response = self.handle_request(request)

        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.whitenoise(environ, start_response)

    def handle_request(self, request):
        response = Response()

        handler = self.find_handler(request_path=request.path)
        if handler is not None:
            controller = handler[0]
            action = handler[1]
            action(controller, request, response)
        else:
            self.default_response(response)

        return response

    def find_handler(self, request_path):
        for path, handler in self.routes.items():
            if path == request_path:
                return handler
    def default_response(self, response):
        response.status_code = 404
        response.text = "Not found"

    def route(self, path):
        def wrapper(handler):
            self.routes[path] = handler
            return handler
        return wrapper

app = API()

