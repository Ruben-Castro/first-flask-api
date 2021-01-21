from flask_restful import Resource, reqparse
from app.models.user import UserModel



class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True,
                        help="This field is required and thus can't be blank")
    parser.add_argument('password', type=str, required=True,
                        help="This field is required and thus can't be blank")

    def post(self):

        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        user = UserModel(**data)
        print("user created successfully")
        if user:
            user.save_to_db()
            print("user saved successfully")

        return {"message": "User created successfully."}, 201
