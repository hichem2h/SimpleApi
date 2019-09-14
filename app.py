from flask import Flask, json, abort
from flask.views import MethodView

app = Flask(__name__)

objects = [
    {
        'name': 'first',
        'code': 1
    },
    {
        'name': 'second',
        'code': 2
    },
    {
        'name': 'third',
        'code': 3
    }
]


class GetAll(MethodView):
    def get(self):
        return json.jsonify(objects)


class GetObject(MethodView):
    def get(self, id):
        try:
            my_object = objects[id]
            return json.jsonify(my_object)
        except:
            abort(404)
 

class GetStats(MethodView):
    def get(self):
        stats = {
            'length': len(objects),
            'ready': True
        }
        return json.jsonify(stats)

app.add_url_rule('/all', view_func=GetAll.as_view('get_all'))
app.add_url_rule('/<int:id>', view_func=GetObject.as_view('get_object'))
app.add_url_rule('/stats', view_func=GetStats.as_view('get_stats'))

if __name__ == '__main__':
    app.run()
