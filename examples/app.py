from giraffe.core.html import make_html
from giraffe.core.responses import response, json_response, html_response
from giraffe.core.routes import Routes
from giraffe import Giraffe

app = Giraffe(__name__)
routes = Routes()


@routes.route('/')
def text(request):
    return response(request, 'hello world', 200)


@routes.route('/json')
def json(request):
    return json_response(request, {'hello' : 'world'}, 200)


@routes.route('/html/<str:string>/<int:integer>')
def html(request, string, integer):
    return html_response(request, make_html(f'<h1 style="text-align: center;">{string} + {integer}</h1>'), 200)


app.add_routes(routes)


if __name__ == '__main__':
    app.start()
