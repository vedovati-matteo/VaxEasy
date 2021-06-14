# Make all the files available as submodules
from . import user

# Allow 'from my_Flask_app import *' syntax
__all__ = [
    "user"
]