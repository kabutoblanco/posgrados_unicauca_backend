
from django.utils.encoding import force_text
from rest_framework import status
from rest_framework.exceptions import APIException

class CustomException(APIException):
    status_code = status.HTTP_204_NO_CONTENT
    default_detail = "Error no especificado"

    def __init__(self, detail, field, status_code):
        if status_code is not None:self.status_code = status_code
        if detail is not None:
            self.detail = {field: force_text(detail)}
        else: self.detail = {'detail': force_text(self.default_detail)}