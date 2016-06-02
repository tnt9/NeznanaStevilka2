#!/usr/bin/env python
import os
import jinja2
import webapp2
import random


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)



def convert(x):
    ''' convert x or y into integer '''
    if x == "":
        return ""
    try:
        x = float(x)
        return x
    except ValueError:  # user entered non-numeric value
        return "invalid input"


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        parametri = {"sporocilo": "To sem jaz Main Handler"}
        return self.render_template("index.html", params=parametri)

    def post(self):
        x = self.request.get("vnos")
        x1 = convert(x)
        number = random.randint(1, 10)
        if x1 == "invalid input":
            rezultat = "Not valid input"
        elif x1 == number:
            rezultat = "The number is correct! "
        else:
            rezultat = "The number is not correct"

        parametri = {"rezultat": rezultat}
        return self.render_template("index.html", params=parametri)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)
