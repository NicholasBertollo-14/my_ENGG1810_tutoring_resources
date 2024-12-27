# There are many ways to import

# First we have to note the difference between a script and a module

# Second we have to note the difference between a library, package, and module

# All of these import the pyplot module with or without an alias:

# You have to write full name, eg. matplotlib.pyplot.plot()
import matplotlib.pyplot

# You get to write alias, eg. plt.plot()
import matplotlib.pyplot as plt

# You have to write module name, eg. pyplot.plot()
from matplotlib import pyplot

# You have to write alias, eg. plt.plot()
from matplotlib import pyplot as plt

# Import my own modules
import x_my_module as x_my_module
import x_my_package.inner_module
print(x_my_module.global_variable_in_a_module)
print(x_my_module.function_in_a_module())

# Import in a different way
from x_my_module import function_in_a_module, global_variable_in_a_module
print(global_variable_in_a_module)
print(function_in_a_module())

# You can alias individual components
from x_my_module import function_in_a_module as function, global_variable_in_a_module as variable
print(variable)
print(function())

# Why does this run the code?
# Why does this differ from when you run it normally
import x_my_script

# A script and a module are the same thing when you use a main function with __name__ == "__main__"
import x_main_again as x_main_again # Notice this doesn't run anything, but it still defines functions and can also be run
print(x_main_again.what_is_this())
x_main_again.main() # Why can I run main() # Talk about __main

# Trying to answer: Do you understand what matplotlib is really doing?
# A module in a package?
import x_my_package
print(x_my_package.inner_module.function_in_inner_module())

from x_my_package import inner_module as mom
print(mom.function_in_inner_module())

from x_my_package.inner_module import function_in_inner_module as fiim
print(fiim())

# Notice that: from .. import ... doesn't except objects, only names of files or folders
"""
from x_my_package import my_other_module
from my_other_module import function_in_inner_module
"""

# What is python's standard library? Look this up...