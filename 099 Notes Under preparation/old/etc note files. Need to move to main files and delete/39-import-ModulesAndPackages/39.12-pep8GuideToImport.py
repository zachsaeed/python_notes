# Pep8 Import styling:
"""Illustration of good import statement styling. Note that the imports come after the doc string"""

# Standard library imports
import datetime
import os

# Third-party imports
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

# Local application imports
from local_module import local_class
from local_package import local_function

# NOTE: we can import multiple modules using commas but PEP8 says to import each module in a separate line
import module1, module2 as b, module3
# should be:
import module1
import module2 as b
import module3

# PEP8 is ok with using commas when using from. Example:
from XXX import a, b, c