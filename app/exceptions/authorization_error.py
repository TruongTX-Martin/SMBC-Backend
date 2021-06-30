from .api_response_error import APIResponseError


class AuthorizationError(APIResponseError):
    status_code = 403
