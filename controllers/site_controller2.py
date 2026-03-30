from views.view import View

class SiteController:
    def __init__(self):
        self.layout =  "default"
        self.view = View(self.layout)

    def index(self, request, response):
        response.text = self.view.render_html('index.html', {'title' : 'MVC фреймворк', 'h1' : 'Главная страница'})

    def about(self, request, response):
        response.text = "Cтраница о нас"