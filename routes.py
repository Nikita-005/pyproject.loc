from controllers.site_controller import SiteController
from controllers.articles_controller import ArticlesController
from controllers.users_controller import UsersController

routes = {
    r"^/article/(\d+)/edit$" : [ArticlesController, ArticlesController.edit],
    r"^/article/(\d+)/delete$" : [ArticlesController, ArticlesController.delete],
    r"^/article/(\d+)$" : [ArticlesController, ArticlesController.view],
    r"^/articles$" : [ArticlesController, ArticlesController.index],
    r"^/articles/add$" : [ArticlesController, ArticlesController.add],
    r"^/articles/search$" : [ArticlesController, ArticlesController.search],
    r"^/user/register$" : [UsersController, UsersController.sign_up],
    r"^/user/login$" : [UsersController, UsersController.sign_in],
    r"^/user/logout$" : [UsersController, UsersController.logout],
    r"^/$" : [SiteController, SiteController.index],
    r"^/about$" : [SiteController, SiteController.about],
    r"^/hello/(.*)$" : [SiteController, SiteController.hello],
}