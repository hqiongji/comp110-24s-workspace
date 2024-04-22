"""evaluate_algorithms!"""

__author__: str = "730520183"


import matplotlib.pyplot as plt
from runtime_analysis_functions import evaluate_memory_usage

start_size: int = 0
end_size: int = 1000


import matplotlib.pyplot as plt
from runtime_analysis_functions import evaluate_runtime 

times = evaluate_runtime("selection_sort", start_size, end_size)
plt.plot(times)
plt.title("Runtime Analysis of Selection Sort - hqiongji")
plt.show()

times = evaluate_runtime("insertion_sort", start_size, end_size)
plt.plot(times)
plt.title("Runtime Analysis of Insertion Sort - hqiongji")
plt.show()

usage = evaluate_memory_usage("selection_sort", start_size, end_size)
plt.plot(usage)
plt.title("Memory Usage Analysis of Selection Sort - hqiongji")
plt.show()

usage = evaluate_memory_usage("insertion_sort", start_size, end_size)
plt.plot(usage)
plt.title("Memory Usage Analysis of Insertion Sort - hqiongji")
plt.show()
