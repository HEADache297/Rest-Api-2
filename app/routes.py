from flask import Blueprint, request, abort, jsonify
from marshmallow import ValidationError
from .extentions import connect
from .schema import User

api = Blueprint("/", "")

@api.route('/users/<string:UUID>', methods=['GET'])
async def get_user(UUID):
    from asyncpg.exceptions import PostgresError
    try:
        conn = await connect()
        result = await conn.fetch("SELECT * FROM users where id = $1;", UUID)
        await conn.close()
        user = {'status': 'success', 'user': dict(result[0])}
        return user
    except PostgresError as p:
        error = {'status': 'failed', 'message': str(p)}
        return jsonify(error), 400
    except any as a:
        error = {'status': 'failed', 'message': str(a)}
        return jsonify(error), 400
    

@api.route('/users', methods=['GET'])
async def get_users():
    try:
        conn = await connect()
        result = await conn.fetch("SELECT * FROM users;")
        await conn.close()
        users = {'status': 'success', 'user': [dict(row) for row in result]}
        return users
    except any as a:
        error = {'status': 'failed', 'message': str(a)}
        return jsonify(error), 400
    

@api.route('/users', methods=['POST'])
async def create_user():
    from asyncpg.exceptions import UniqueViolationError, PostgresError
    try:
        data = User().load(request.get_json())
    except ValidationError as err:
        print(err.messages)
        error = {'status': 'failed', 'message': err.messages}
        return jsonify(error), 400
    
    try:
        conn = await connect()
        result = await conn.fetch("INSERT INTO users(username, email, password) VALUES($1, $2, $3) RETURNING *", 
                                data["username"], data["email"], data["password"])
        response = {'status': 'success', 'user': dict(result[0])}
        return jsonify(response), 200
    except UniqueViolationError as e:
        print(e)
        error = {'status': 'failed', 'message': str(e)}
        return jsonify(error), 400
    except any as a:
        print(a)
        error = {'status': 'failed', 'message': str(a)}
        return jsonify(error), 501
    finally:
        await conn.close()
