

class SiteController:
    def index(self, request, response):
        response.text = '''<html>
    <head>
        <title>Главная</title>

        <link href="css/main.css" type="text/css" rel="stylesheet">
    </head>

    <body>
        <h1>The name of the framework is {{ name }}</h1>
    </body>

</html>'''
    def about(self, request, response):
        response.text = "Cтраница о нас"