from django.core.exceptions import ImproperlyConfigured
import os


def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = '{} is not set'.format(var_name)
        raise ImproperlyConfigured(error_msg)
