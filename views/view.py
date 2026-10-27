# import os
from jinja2 import Environment, FileSystemLoader
import json

class View:
    def __init__(self, layout):
        self.layout = layout
        self.extra_vars = {}
        self.env = Environment(loader=FileSystemLoader('views'), autoescape=(["html", "xml"]))

    def render_html(self, view_name, vars = {}):
        layout_file = f"layouts/{self.layout}.html"
        file_vars = {"content" : view_name}
        file_vars.update(vars)
        file_vars.update(self.extra_vars)
        template = self.env.get_template(layout_file)
        return template.render(file_vars)
    def set_var(self, name, value):
        self.extra_vars[name] = value

    def display_json(self, data, code = 200):
        # header('Content-type: application/json; charset=utf-8')
        # http_response_code(code)

        # print(data)
        # print(json.dumps(data))
        return json.dumps(data)