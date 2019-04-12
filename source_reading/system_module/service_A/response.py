# -*- coding: utf8 -*-

from enum import Enum


class HttpStatusCodeEnum(Enum):
    OK = 200  # GET, POST, PUT, Delete 请求成功
    NotFound = 404  # 请求资源不存在或不可用
    ClientClosedRequest = 499  # The operation was cancelled, typically by the caller.
    InternalServerError = 500  # 服务端请求错误


class ResponseCodeEnum(Enum):
    """
        Not an error; returned on success

        HTTP Mapping: 200 OK
        """
    OK = 0
    """
    The operation was cancelled, typically by the caller.

    HTTP Mapping: 499 Client Closed Request
    """
    CANCELLED = 1
    """
        Some requested entity (e.g., file or directory) was not found.

        Note to server developers: if a request is denied for an entire class
        of users, such as gradual feature rollout or undocumented whitelist,
        `NOT_FOUND` may be used. If a request is denied for some users within
        a class of users, such as user-based access control, `PERMISSION_DENIED`
        must be used.

        HTTP Mapping: 404 Not Found
        """
    NOT_FOUND = 5


class ApiBaseException(Exception):
    status_code = None
    status = None
    message = None

    def __init__(self, status_code: HttpStatusCodeEnum = None, status: ResponseCodeEnum = None,
                 message: str = None):
        super().__init__()
        if status_code:
            self.status_code = status_code
        if status:
            self.status = status
        if message:
            self.message = message


class Canceled(ApiBaseException):
    """
    客户端取消操作
    """
    print("Canceled has been called")
    status_code = HttpStatusCodeEnum.ClientClosedRequest.value
    status = ResponseCodeEnum.CANCELLED
    log_level = None
    message = (
        'Operation cancelled by caller.'
    )


class NotFound(ApiBaseException):
    """
    数据不存在
    """
    status_code = HttpStatusCodeEnum.NotFound.value
    status = ResponseCodeEnum.NOT_FOUND
    log_level = None
    message = (
        'Requested entity was not found.'
    )
