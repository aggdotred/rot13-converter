import os
import jinja2
import webapp2
import string

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)
    
    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class MainPage(Handler):
    def get(self):
        text=""
        self.render("converter.html", text = text)
    
    def post(self):
        u = string.lowercase
        l = string.uppercase

        original_text = self.request.get("text")
        text = ""

        for i in original_text:
            if i in u:
                x = u.index(i) + 13
                if x > len(u) - 1:
                    x = x - len(u)
                text += u[x]
            if i in l:
                x = l.index(i) + 13
                if x > len(l) - 1:
                    x = x - len(l)
                text += l[x]
            if i not in l and i not in u:
                text += original_text[original_text.index(i)]
            

        self.render("converter.html", text = text)

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)