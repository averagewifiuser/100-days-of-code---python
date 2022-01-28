#the generic responses of the API

from flask import jsonify, message_flashed
from werkzeug.http import HTTP_STATUS_CODES

def error_response(status_code, message=None):
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
    response = jsonify({'error': payload})
    response.status_code = status_code
    return response


def success_response(message=None, data=None):
    if data:
        response = {'data': data}
    elif message:
        response = {'message': message}
    else:
        response = {'message':'success'}

    #for both
    if data and message:
        response = {'data': data, 'message': message}
    return jsonify(response), 200


def bad_request(message):
    return error_response(400, message)


def unauthorized_request(message="You're not allowed to do that!"):
    return error_response(401, message)


def server_error(message="Something went wrong! Our backend team has been notified and are working to resolve it."):
    return error_response(500, message)


def not_found(message='The object was not found!'):
    return error_response(404, message)