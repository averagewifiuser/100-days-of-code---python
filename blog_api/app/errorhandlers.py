from flask import jsonify

def page_not_found(e):
    return jsonify({'message':'Error page not found!'}), 404


def method_not_allowed(e):
    return jsonify({'message': 'Method not allowed!'}), 405


def internal_server_error(e):
    return jsonify({'message':'Sorry something went wrong! Try Later'}), 500


def forbidden(e):
    return jsonify({'message':'Sorry. You cannot do that!'}), 403


