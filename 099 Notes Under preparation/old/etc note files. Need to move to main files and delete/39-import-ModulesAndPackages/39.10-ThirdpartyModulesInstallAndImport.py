# - External modules are made by third-parties and dont come with python by default. We can search for 3rd party python
#   packages on the python package index
#       https://pypi.org/ (PyPi: Python Package index)
# - External modules can be downloaded and installed using a python package manager pip (Pip Installs Packages). It
#   comes with python by default as of python 3.4+
#       python -m pip install <NAME_OF_PACKAGE>
# - For example, Install termcolor (https://pypi.org/project/termcolor/):
#       python -m pip install termcolor
# - Ater install, we can simply import the third-party package and use it in our code:

import termcolor

# to see  the available attributes and methods
print(dir(termcolor))
print(termcolor.colored("Hi There", color="cyan"))

# Standard aliases:
# Before running code below, run following on command line:
# python3 -m pip install matplotlib
# python3 -m pip install numpy
# python3 -m pip install pandas
# We ca also use 'as' with just 'import' of third party modules:

# Note: pyplot is itself a module within matplotlib so we can't do: from matplotlib import pyplot:
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# In the examples above, the import as is not to prevent name clashes, but to make the notation handier.
# Instead of typing:
# matplotlib.pyplot.plot(4, 4)
# You can simply type:
plt.plot(4, 4)

# Different packages have different shortcuts. For example PyQtGraph is normally shortened as pg, and for sure different
# fields use different abbreviations. Importing Numpy as np or Pandas as pd is not mandatory. However, since it is what
# the community does, it will make your code much more readable.
# If you go through StackOverflow, you will see that more often than not, the line in which numpy is imported is omitted
# and you just see the use of np.
