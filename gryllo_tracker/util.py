import os


def set_settings_module(env):
    """Sets the settings module to use

    Args:
        env (:obj:`str`, optional): Environment to use.
            Possible values: 'local', 'development', 'production'. Defaults to 'local'.
    """
    valid_envs = ['local', 'development', 'production']
    env = env if env in valid_envs else 'local'

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'gryllo_tracker.settings.{env}')
