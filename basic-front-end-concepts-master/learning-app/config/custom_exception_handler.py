# -*- coding: utf-8 -*-
from django.db import IntegrityError
from jose import ExpiredSignatureError, JWTError
from rest_framework.response import Response
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):

    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code

    elif isinstance(exc, ExpiredSignatureError):
        response = Response({'detail': str(exc), 'status_code': 401},
                            status=401)

    elif isinstance(exc, IntegrityError):
        error_msg = exc.args[0]
        response = Response({'detail': error_msg, 'status_code': 409},
                            status=409)

    elif isinstance(exc, JWTError):
        response = Response({'detail': str(exc), 'status_code': 401},
                            status=401)

    elif isinstance(exc, Exception):
        response = Response({'detail': str(exc), 'status_code': 500},
                            status=500)

    return response
