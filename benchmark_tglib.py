
import pytglib as tgl  # tglib
import scipy.stats as ss  # for Kendall's tau correlation
from tqdm import tqdm
import time
import numpy as np
import random


class testname():
    def do_benchmark(inPath, pathsSize):
        results = {}
        
# Load Graph
        start = time.time()
        directed = True
        g = tgl.load_ordered_edge_list(inPath, directed)
        end = time.time()

        print(f"Time taken to read graph {end-start} seconds")
        results["loadTime"] = end-start

# Get statistcs
        start = time.time()
        stats = tgl.get_statistics(g)
        end = time.time()

        results["stats"] = end-start
        print(f"Time taken to get stats {end-start} seconds \n")
        print(stats)

# Paths
        # start = time.time()

        num_nodes = g.getNumberOfNodes()
        nodes  = list(g.getNodeMap().keys())
        incidents = tgl.to_incident_lists(g)

        selected_from = np.random.choice(nodes, size=pathsSize)
        selected_to = nodes


        # for fro in tqdm(selected_from):
        #     for to in (selected_to):
        #         temp = tgl.minimum_transition_time_path(incidents, fro, to, g.getTimeInterval())
        
        # end = time.time()
        # results["paths"] = end-start
        # print(f"Time taken to get shortest paths {end-start} seconds")
        

# clustering coefficient
        
        start = time.time()

        tgl.temporal_clustering_coefficient(incidents, g.getTimeInterval())

        end = time.time()
        results["clusteringCoefficient"] = end-start
        print(f"Time to get clustering coefficient: {end - start}")
# Pagerank
        start = time.time()

        pr = tgl.temporal_pagerank(g, 1.0,1.0,1.0)

        end = time.time()
        results["pagerank"] = end-start
        print(f"Time to get Pagerank: {end - start}")


# Traingles and triplets


        return results