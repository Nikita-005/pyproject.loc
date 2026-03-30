from views.view import View

class Controller:
    def __init__(self):
        self.layout =  "default"
        self.view = View(self.layout)