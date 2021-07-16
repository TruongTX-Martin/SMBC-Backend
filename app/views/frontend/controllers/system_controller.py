from flask import Blueprint, jsonify

from app.database import db

app = Blueprint('frontend.system', __name__)


@app.route('/health')
def health():
    try:
        db.session.execute('SELECT 1')
    except Exception as e:
        raise e

    return jsonify({'status': 'healthy'}), 200
