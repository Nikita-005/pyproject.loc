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
            try:
                form = cgi.FieldStorage(fp=request.environ['wsgi.input'], environ = request.environ)
                fields = {
                    'name' : form.getvalue('name'),
                    'text' : form.getvalue('text')
                }
                img_file = form['img']
                article.updateFromArray(fields, img_file)
                response.status_code = 302
                response.headers = [('Location', f'/article/{article.get_id()}')]
            except InvalidArgumentException as e:
                response.text = self.view.render_html('articles/edit.html', {
                    'title' : f'Редактирование - {article.get_name()}',
                    'article' : article,
                    'article_data' : fields,
                    'error' : e
                    })
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
            except InvalidArgumentException as e:
                response.text = self.view.render_html('articles/add.html', {'title' : 'Добавление статьи', 'article_data' : fields, 'error' : e})
            return
        response.text = self.view.render_html('articles/add.html', {'title' : 'Добавление статьи'})

    def search(self, request, response):
        if not 'q' in request.GET:
            response.text = self.view.render_html('articles/search.html')
            return
        else:
            articles = Article.search_by_name(request.GET['q'])
            response.text = self.view.render_html('articles/search.html', { 'q' : request.GET['q'], 'articles' : articles})