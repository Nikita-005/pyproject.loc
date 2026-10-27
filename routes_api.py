from controllers.site_controller import SiteController
from controllers.api.articles_controller import ArticlesApiController
from controllers.users_controller import UsersController

routes = {
    # r"^/article/(\d+)/edit$" : [ArticlesController, ArticlesController.edit],
    r"^/article/(\d+)$~" : [ArticlesApiController,  {'GET' : 'view', 'DELETE' : 'delete','OPTIONS' : 'options'}],
    # r"^/article/(\d+)/delete$" : [ArticlesController, ArticlesController.delete],
    # r"^/article/(\d+)$" : [ArticlesController, ArticlesController.view],
    # r"^/articles$" : [ArticlesController, ArticlesController.index],
    # r"^/articles/add$" : [ArticlesController, ArticlesController.add],
    # r"^/articles/search$" : [ArticlesController, ArticlesController.search],
    # r"^/user/register$" : [UsersController, UsersController.sign_up],
    # r"^/user/login$" : [UsersController, UsersController.sign_in],
    # r"^/user/logout$" : [UsersController, UsersController.logout],
    # r"^/$" : [SiteController, SiteController.index],
    # r"^/about$" : [SiteController, SiteController.about],
    # r"^/hello/(.*)$" : [SiteController, SiteController.hello],
}

    # '~^articles/(\d+)$~' => [\Src\Controllers\Api\ArticlesApiController::class,  'GET' =>'view', 'DELETE' => 'delete','OPTIONS' => 'options'],
    #  '~^articles$~' => [\Src\Controllers\Api\ArticlesApiController::class,  'GET' =>'all', 'POST' => 'add'],
    # '~^users/login$~' => [\Src\Controllers\Api\UsersApiController::class, 'POST' =>'login'],
    # '~^users/login/free$~' => [\Src\Controllers\Api\UsersApiController::class, 'GET' =>'loginFree'],
    # '~^users$~' => [\Src\Controllers\Api\UsersApiController::class, 'GET' =>'user'],