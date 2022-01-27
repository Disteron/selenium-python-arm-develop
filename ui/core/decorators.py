import time
import shared_vars

from selenium.common.exceptions import TimeoutException


def retry(func):
    """ Decorator

    :param func: метод, который будет повторно исполняться в случае ошибки
    :return: возвращаемое значение метода или пустое значение
    """

    def func_wrapper(*args, **kwargs):

        end = time.time() + int(shared_vars.APPLICATION_PROPERTIES.get("timeout"))
        time.sleep(0.5)
        exception = None

        while end > time.time():
            try:
                return func(*args, **kwargs)
            except Exception as exc:
                exception = exc
                if exc.__class__.__name__ == 'TestFailException':
                    raise exc
                time.sleep(0.5)

        raise TimeoutException(exception)

    return func_wrapper
