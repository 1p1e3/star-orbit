from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse


app = Flask(__name__)
api = Api(app)


class Login(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True, help="用户名不能为空")
    parser.add_argument("password", type=str, required=True, help="密码不能为空")

    def post(self):
        username = request.json.get("username")
        password = request.json.get("password")

        if username == "admin" and password == "admin":
            return jsonify({
                "msg": "success",
                "token": "a1b2c3d4f5"
            })
        return jsonify({
            "msg": "用户名或密码错误",
        })


api.add_resource(Login, "/login")


if __name__ == '__main__':
    app.run(debug=True)