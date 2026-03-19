

class SiteController:
    def index(self, request, response):
        response.text = "Главная страница"
    def about(self, request, response):
        response.text = "Cтраница о нас"