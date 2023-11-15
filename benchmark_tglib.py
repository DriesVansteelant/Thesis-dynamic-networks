
import pytglib as tgl  # tglib
import scipy.stats as ss  # for Kendall's tau correlation
from tqdm import tqdm
import time
import numpy as np
import random


# class testname():
#     def do_benchmark(inPath, statsPath, pathsSize):
statsFile = open(statsPath, 'a')

start = time.time()
directed = True
g = tgl.load_ordered_edge_list(inPath, directed)
end = time.time()

print(f"Time taken to read graph {end-start} seconds")
statsFile.write(f"Time taken to read graph {end-start} seconds \n")

start = time.time()
stats = tgl.get_statistics(g)
end = time.time()

statsFile.write(f"Time taken to get stats {end-start} seconds")
print(f"Time taken to get stats {end-start} seconds \n")
statsFile.write(str(stats))
statsFile.write("\n")
print(stats)

start = time.time()

num_nodes = g.getNumberOfNodes()
nodes  = list(g.getNodeMap().keys())
incidents = tgl.to_incident_lists(g)

selected_from = np.random.choice(nodes, size=pathsSize)
selected_to = nodes

# for fro in tqdm(selected_from):
#     for to in (selected_to):
#         temp = tgl.minimum_transition_time_path(incidents, fro, to, g.getTimeInterval())


end = time.time()
print(f"Time taken to get shortest paths {end-start} seconds")
statsFile.write(f"Time taken to get shortest paths {end-start} seconds\n")
statsFile.close()
statsFile.write("\n")
statsFile.write("\n")