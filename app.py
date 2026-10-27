import os
import sys
import re

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from webob import Request, Response
from whitenoise import WhiteNoise
from controllers.site_controller import SiteController
from exceptions import NotFoundException
from exceptions import UnauthorizedException
from exceptions import InvalidMethodException
from views.view import View
import routes

STATIC_DIR="assets"

class API:
    def __init__(self):
        self.routes = routes.routes
        self.whitenoise = WhiteNoise(self.wsgi_app, root=STATIC_DIR, autorefresh=False)


    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        # print(request.path_info)
        response = self.handle_request(request)

        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.whitenoise(environ, start_response)

    def handle_request(self, request):
        response = Response()

        controller = SiteController(request)
        api = False

        try:
            result = self.find_handler_re(request_path=request.path)
            # print('!!!!!!!', result)
            if result is None:
                raise NotFoundException('Страница не найдена')

            handler, params = result
            controller = handler[0](request)

            method = request.method
            if isinstance(handler[1], dict):
                api = True
                if method in handler[1]:
                    action = handler[1][method]
                else:
                    raise InvalidMethodException('Method not support')
            else:
                action = handler[1]

            # action = handler[1]
            action(controller, request, response, *params)

        except NotFoundException as e:
            response.status_code =404
            if api:
                response.text = controller.view.display_json({'error' : e})
            else:
                response.text = controller.view.render_html('errors/404.html', {'error' : e})
        except UnauthorizedException as e:
            response.status_code =401
            if api:
                response.text = controller.view.display_json({'error' : e})
            else:
                response.text = controller.view.render_html('errors/401.html', {'error' : e})
        except InvalidMethodException as e:
            response.status_code = 405
            if api:
                response.text = controller.view.display_json({'error' : str(e)})
            else:
                response.text = controller.view.render_html('errors/405.html', {'error' : e})
        return response

    def find_handler(self, request_path):
        for path, handler in self.routes.items():
            if path == request_path:
                return handler

    def find_handler_re(self, request_path):
        # print(request_path)
        for path, handler in self.routes.items():
            match = re.search(path, request_path)
            if match is not None:
                return handler, match.groups()


    def default_response(self, response):
        response.status_code = 404
        response.text = "Not found"

    def route(self, path):
        def wrapper(handler):
            self.routes[path] = handler
            return handler
        return wrapper

app = API()

