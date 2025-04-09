# python uses a package installing software called pip
# when installing packages, use a virtual environment
# python3 -m venv .venv 
# source .venv/bin/activate
# some libraries are built-in - we dont need to pip install
# some libraries need to be installed with `pip install`

# built in
import math

# pip install statistics
import statistics

# import just a function
from statistics import mean

# import from another file
from functions import adding_together

print(math.ceil(2.3))
print(statistics.mean([1, 3]))
print(mean([1, 5]))

print(adding_together(1, 4))