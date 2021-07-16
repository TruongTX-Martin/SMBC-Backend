import traceback

from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException

from app.exceptions import APIResponseError, LogicError, ParameterError
from app.helpers import SlackHelper


class ResponseErrorHandler:
    def __init__(self, app: Flask):
        @app.errorhandler(ParameterError)
        def handle_parameter_error(error):
            app.logger.error(error.to_dict())
            response = jsonify(error.to_dict())
            response.status_code = error.status_code
            return response

        @app.errorhandler(APIResponseError)
        def handle_api_response_error(error):
            app.logger.error(error.to_dict())
            response = jsonify(error.to_dict())
            response.status_code = error.status_code
            return response

        @app.errorhandler(LogicError)
        def handle_logic_error(error):
            app.logger.error(error.to_dict())
            response = jsonify(error.to_dict())
            response.status_code = error.status_code
            return response

        @app.errorhandler(404)
        def resource_not_found(e):
            response = jsonify({'status': 'error', 'message': str(e)})
            response.status_code = 404
            return response

        @app.errorhandler(405)
        def handle_method_not_allow_exception(error):
            app.logger.exception(error)
            response = jsonify({
                'status': 'error',
                'message': 'Method Not Allowed'
            })
            response.status_code = 500
            return response

        @app.errorhandler(HTTPException)
        def handle_http_exception(error):
            app.logger.error(error)
            response = jsonify({'status': 'error', 'message': str(error)})
            response.status_code = 400
            return response

        @app.errorhandler(Exception)
        def handle_exception(error):
            app.logger.exception(error)
            error_msg = traceback.format_exc()
            SlackHelper.send_error(error_msg)
            response = jsonify({
                'status': 'error',
                'message': 'Internal Server Error'
            })
            response.status_code = 500
            return response
