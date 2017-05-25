# -*- coding: utf-8 -*-

__all__ = [
    'ApiCallError',
    'ArgumentError',
    'HttpError',
    'RateLimitExceeded',
    'AuthenticationError',
    'BadGatewayError',
    'BadRequestError',
    'ResourceNotFound',
    'ServerError',
    'ServiceUnavailableError',
    'UnexpectedError',
]


class EmarsysError(Exception):
    def __init__(self, message=None, context=None):
        super(EmarsysError, self).__init__(message)
        self.message = message
        self.context = context


class ArgumentError(ValueError, EmarsysError):
    pass


class HttpError(EmarsysError):
    pass


class RateLimitExceeded(EmarsysError):
    pass


class UnexpectedError(EmarsysError):
    pass


class ResourceNotFound(EmarsysError):
    pass


class AuthenticationError(EmarsysError):
    pass


class ServerError(EmarsysError):
    pass


class BadGatewayError(EmarsysError):
    pass


class ServiceUnavailableError(EmarsysError):
    pass


class BadRequestError(EmarsysError):
    pass


class ApiCallError(EmarsysError):
    pass


error_codes = {
    'rate_limit_exceeded': RateLimitExceeded,
}
