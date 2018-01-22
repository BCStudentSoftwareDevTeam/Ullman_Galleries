from os.path import dirname, basename, isfile
from flask import Blueprint
import glob
modules = glob.glob(dirname(__file__)+"/*.py")


__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]

