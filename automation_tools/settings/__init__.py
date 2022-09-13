"""For production, we'll automatically generate settings from prod.py via ci/cd script"""

# DEV = False
env_name = "stage"

if env_name == "prod":
    from .production import *
elif env_name == "stage":
    from .stage import *
else:
    from .local import *
