from flask import Blueprint, request

bp = Blueprint('routes', __name__)

@bp.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return "Hello, this is a GET request!"
    elif request.method == 'POST':
        return "Hello, this is a POST request!"
