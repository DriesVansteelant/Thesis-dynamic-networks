import tglib.tglib_cpp.build.src.python_binding.Release.pytglib as tgl  # tglib
import scipy.stats as ss  # for Kendall's tau correlation
from tqdm import tqdm
import time
import numpy as np
import random

# inPath = "../Code/Data/example_from_paper.tg"
inPath = "../Code/Data/enron.txt"

start = time.time()
directed = True
g = tgl.load_ordered_edge_list(inPath, directed)
end = time.time()

print(f"Time taken to read graph {end-start} seconds")


start = time.time()

stats = tgl.get_statistics(g)
stats2 = tgl.get_order_by_in_degree(g)

end = time.time()

print(f"Time taken to sort graph {end-start} seconds")

print(stats)
print(len(stats2))
for x in stats2:
    print(x)