from .api_response_error import APIResponseError


class ParameterError(APIResponseError):
    def __init__(self, error, status_code=None, payload=None):
        Exception.__init__(self)
        self._error = error
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        return_value = dict(self.payload or ())
        return_value['status'] = 'error'
        return_value['message'] = 'Parameter error'
        return_value['invalidParams'] = []
        if isinstance(self._error, str):
            return_value['message'] = self._error

        if isinstance(self._error, dict):
            for k in self._error.keys():
                return_value['invalidParams'].append({
                    'name': k,
                    'message': self._error[k][0]
                })
        return return_value
