from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_pymongo import PyMongo
from flask_restful import Resource, Api, reqparse, abort, fields , marshal_with


app = Flask(__name__)

app.config["MONGODB_SETTINGS"] = {
    'db': 'MokhlesGame',
    'db': 'localhost',
    'db': '27017',

}

users_list = [
    {
        'id': 1,
        'name': 'Mokhles',
        'age': '25',
        'job': 'backend developer',
    },
    {
        'id': 2,
        'name': 'Ahmed',
        'age': '25',
        'job': 'frontend developer',
    },
    {
        'id': 3,
        'name': 'Mohamed',
        'age': '22',
        'job': 'frontend developer',
    },
    ]



@app.route('/users', methods=('GET', 'POST'))
def users():
    if request.method == 'POST':
        user = request.get_json()
        users_list.append(user)
        return jsonify(users_list), 201


    if request.method == 'GET':
        if len(users_list) > 0:
            return jsonify(users_list), 200
        else:
            return jsonify({'message': 'No users found'}), 404



if __name__ == '__main__':
    app.run(debug=True)