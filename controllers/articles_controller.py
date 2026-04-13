import cgi

from controllers.controller import Controller
from models.article import Article
from models.user import User
from exceptions import NotFoundException
from exceptions import UnauthorizedException
from exceptions import InvalidArgumentException


class ArticlesController(Controller):

    def index(self, request, response):
        articles = Article.find_all()
        print(articles)
        response.text = self.view.render_html('articles/index.html', {'title' : 'MVC фреймворк - статьи', 'h1' : 'Статьи на сайте', 'articles' : articles})

    def view(self, request, response, id):
        article = Article.get_by_id(id)
        if article is None:
             raise NotFoundException('Статья не найдена')

        user = User.get_by_id(article.get_author_id())
        response.text = self.view.render_html('articles/view.html', {
            'title' : f'MVC фреймворк - {article.get_name()}',
            'h1' : f'Статья: {article.get_name()} ',
            'article' : article})

    def edit(self, request, response, id):
        article = Article.get_by_id(id)
        if article is None:
            raise NotFoundException('Статья не найдена')

        if self.user is None:
            raise UnauthorizedException('Необходимо авторизоваться')


        if request.method == 'POST':
            article.set_name(request.POST['name'])
            article.set_text(request.POST['text'])
            article.save()
            response.status_code = 302
            response.headers = [('Location', f'/article/{article.get_id()}')]
            return

        response.text = self.view.render_html('articles/edit.html', {
            'title' : f'Редактирование - {article.get_name()}',
            'article' : article})

    def delete(self, request, response, id):
        article = Article.get_by_id(id)
        if article is None:
            raise NotFoundException('Статья не найдена')

        article.delete()
        response.status_code = 302
        response.headers = [('Location', '/articles')]

    def add(self, request, response):
        if self.user is None:
            raise UnauthorizedException('Необходимо авторизоваться')
        if request.method == 'POST':
            try:
                form = cgi.FieldStorage(fp=request.environ['wsgi.input'], environ = request.environ)
                fields = {
                    'name' : form.getvalue('name'),
                    'text' : form.getvalue('text')
                }
                img_file = form['img']
                article =Article.create(fields, img_file, self.user)
                if isinstance( article, Article):
                    response.status_code = 302
                    response.headers = [('Location', '/articles')]
                    return
            except InvalidArgumentException as e:
                response.text = self.view.render_html('articles/add.html', {'title' : 'Добавление статьи', 'article_data' : fields, 'error' : e})
                return
        response.text = self.view.render_html('articles/add.html', {'title' : 'Добавление статьи'})