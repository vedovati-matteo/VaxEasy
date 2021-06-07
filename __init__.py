# Make all the files available as submodules
from . import model_utils
from . import app

# Allow 'from my_Flask_app import *' syntax
__all__ = [
    "model_utils",
    "app"
]
