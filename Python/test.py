from search import *
from calculate_time import *


# test search timing:

li = list(range(1000000000))
calculate_time(binary_search(li, 3))
calculate_time(linear_search(li, 3))

