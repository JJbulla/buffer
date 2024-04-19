"""Utility functions for the buffer module."""

from custom_exceptions import buffer_custom_exception
from src import constants


def is_empty(method_buffer) -> bool:
    """Check if the buffer is empty."""

    def wrapper(buffer):
        if buffer.buffer:
            return method_buffer(buffer)
        return custom_exception(constants.BUFFER_EMPTY)

    return wrapper


def custom_exception(msg: str) -> Exception:
    """Raise a custom exception."""
    raise buffer_custom_exception.BufferEmptyError(msg)
