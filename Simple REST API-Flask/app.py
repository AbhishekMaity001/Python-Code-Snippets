from flask import Flask, request
from flask_restful import Resource, Api, marshal_with, fields  # from flask-restful you can use Class based Views  # pip install flask-restful
import os
from flask_sqlalchemy import SQLAlchemy

print(os.getenv('port'))

app = Flask(__name__)  # Flask object
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'  # postgres:///todo.db
db = SQLAlchemy(app)


class Task(db.Model):
    """In our table there will be 2 columns so 2 variables in the class is written"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        """Every time you will print this class object it will return you the name"""
        return self.name


# Traditional method of Flask
# @app.route('/', methods=['GET', 'POST'])
# def hello():
#     print(os.getenv('port'))
#     return '<center><h1> Welcome home page ! port={}</h1></center>'.format(os.getenv('port'))


fakedb = {1: {'name': 'Royal Enfield'},
          2: {'name': 'Meteor 350'},
          3: {'name': 'Himalayan 400'}}

taskFields = {
    'id': fields.Integer,
    'name': fields.String
}


class Items(Resource):
    @marshal_with(taskFields)
    def get(self):
        tasks = Task.query.all()
        return tasks  # fakedb

    @marshal_with(taskFields)
    def post(self):
        data = request.json  # or request.form()
        task = Task(name=data['name'])
        db.session.add(task)
        db.session.commit()

        tasks = Task.query.all()
        # itemId = len(fakedb.keys()) + 1
        # fakedb[itemId] = {'name': data['name']}
        return tasks  # fakedb


class SingleItem(Resource):

    @marshal_with(taskFields)
    def get(self, pk):
        try:
            task = Task.query.filter_by(id=pk).first()
            return task
            # obj = fakedb[pk]
            # return obj
        except:
            return '404 Object not found!'

    @marshal_with(taskFields)
    def put(self, pk):
        data = request.json
        task = Task.query.filter_by(id=pk).first()
        task.name = data["name"]
        db.session.commit()
        return task
        # if pk not in fakedb.keys():
        #     return "Item not found, first add it!"
        # fakedb[pk]['name'] = data['name']
        # return fakedb

    @marshal_with(taskFields)
    def delete(self, pk):
        try:
            task = Task.query.filter_by(id=pk).first()
            db.session.delete(task)
            db.session.commit()
            tasks = Task.query.all()
            return tasks

            # del fakedb[pk]
            # return fakedb
        except:
            return 'Item not found, first add it!'


api.add_resource(Items, '/')
api.add_resource(SingleItem, '/<int:pk>')

if __name__ == '__main__':
    app.run(host='localhost', port=os.getenv('port'), debug=True)
