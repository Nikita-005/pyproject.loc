import json
from controllers.controller import Controller
from models.article import Article

class ArticlesApiController(Controller):
    def index(self, request, response):
        articles = Article.find_all()
        #article = articles[0].to_dict()
        articles_dict = [article.to_dict() for article in articles]

        # print(articles_dict)
        response.text = self.view.display_json({'articles' : articles_dict })
