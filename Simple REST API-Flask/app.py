from flask import Flask, request
from flask_restful import Resource, Api  # from flask-restful you can use Class based Views  # pip install flask-restful
import os

print(os.getenv('port'))

app = Flask(__name__)  # Flask object
api = Api(app)

# Traditional method of Flask
# @app.route('/', methods=['GET', 'POST'])
# def hello():
#     print(os.getenv('port'))
#     return '<center><h1> Welcome home page ! port={}</h1></center>'.format(os.getenv('port'))

fakedb = {1: {'name': 'Royal Enfield'},
          2: {'name': 'Meteor 350'},
          3: {'name': 'Himalayan 400'}}


class Items(Resource):
    def get(self):
        return fakedb

    def post(self):
        data = request.json  # or request.form()
        itemId = len(fakedb.keys()) + 1
        fakedb[itemId] = {'name': data['name']}
        return fakedb


class SingleItem(Resource):
    def get(self, pk):
        try:
            obj = fakedb[pk]
            return obj
        except:
            return '404 Object not found!'

    def put(self, pk):
        data = request.json
        if pk not in fakedb.keys():
            return "Item not found, first add it!"
        fakedb[pk]['name'] = data['name']
        return fakedb

    def delete(self, pk):
        try:
            del fakedb[pk]
            return fakedb
        except:
            return 'Item not found, first add it!'


api.add_resource(Items, '/')
api.add_resource(SingleItem, '/<int:pk>')

if __name__ == '__main__':
    app.run(host='localhost', port=os.getenv('port'), debug=True)
