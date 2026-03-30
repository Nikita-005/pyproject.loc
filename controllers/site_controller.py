from controllers.controller import Controller



class SiteController(Controller):

    def index(self, request, response):

        response.text = self.view.render_html('site/index.html', {'title' : 'MVC фреймворк', 'h1' : 'Главная страница'})

    def about(self, request, response):
        response.text = self.view.render_html('site/about.html', {'title' : 'MVC фреймворк - о нас', 'h1' : 'Страница о нас'})

    def hello(self, request, response, user_name):
        response.text = self.view.render_html('site/hello.html', {'title' : 'MVC фреймворк - приветствие', 'h1' : 'Привет!', 'user' : user_name})
