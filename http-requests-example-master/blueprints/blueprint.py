from flask import Blueprint

our_bp = Blueprint('blueprint', __name__)


@our_bp.route('/blueprint')
def hello():
    return "Hello from blueprint!"
