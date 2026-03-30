from controllers.site_controller import SiteController
from controllers.articles_controller import ArticlesController

routes = {
    r"^/article/(\d+)$" : [ArticlesController, ArticlesController.view],
    r"^/articles$" : [ArticlesController, ArticlesController.index],
    r"^/home$" : [SiteController, SiteController.index],
    r"^/about$" : [SiteController, SiteController.about],
    r"^/hello/(.*)$" : [SiteController, SiteController.hello],
}