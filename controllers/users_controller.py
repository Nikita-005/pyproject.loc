from controllers.controller import Controller
from models.user import User
from models.user_auth_service import UserAuthService
from exceptions import InvalidArgumentException


class UsersController(Controller):

    def sign_up(self, request, response):

        if request.method == 'POST':
            try:
                user = User.sign_up(request.POST)
                if isinstance(user, User):
                    response.text = self.view.render_html('users/sign_up_success.html')
                    return
            except InvalidArgumentException as e:
                response.text = self.view.render_html('users/sign_up.html', {'title' : 'MVC фреймворк - регистрация', 'user_data' : request.POST, 'error' : e})
                return

        response.text = self.view.render_html('users/sign_up.html', {'title' : 'MVC фреймворк - регистрация'})

    def sign_in(self, request, response):

        if request.method == 'POST':
            try:
                user = User.sign_in(request.POST)
                if isinstance(user, User):
                    token = UserAuthService.create_token(user)
                    response.set_cookie('token', token, 500, '/', False, httponly = True)
                    response.status_code = 302
                    response.location = '/articles'
                    return
            except InvalidArgumentException as e:
                response.text = self.view.render_html('users/sign_in.html', {'title' : 'MVC фреймворк - вход', 'user_data' : request.POST, 'error' : e})
                return

        response.text = self.view.render_html('users/sign_in.html', {'title' : 'MVC фреймворк - вход'})

    def logout(self, request , response):
        response.set_cookie('token', '', -1, '/')
        response.status_code = 302
        response.location = request.referer