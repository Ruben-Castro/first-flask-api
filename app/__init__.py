from flask_restful import Resource, Api, reqparse
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from app.security import authenticate, identity
from app.resources.user import UserRegister
from app.resources.item import Item, ItemList
from app.resources.user import UserRegister
from app.resources.store import Store, StoreList
from app.db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'Ruben'
api = Api(app)
db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(ItemList, '/items')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
