import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

import tglib.tglib_cpp.build.src.python_binding.Release.pytglib as tgl  # tglib 
import scipy.stats as ss  # for Kendall's tau correlation
from tqdm import tqdm
import time
import numpy as np
import random


from line_profiler import profile, LineProfiler


@profile
class TGBLibBenchmark():
    @profile
    def do_benchmark(inPath, pathsSize, do_paths = True):
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


        # start = time.time()
        # stats2 = tgl.get_node_statistics(g)
        # end = time.time()
        # print(f"Time taken to get node stats {end-start} seconds \n")
        # for i in stats2:
        #         print(i)

# To incidents
        start = time.time()
        incidents = tgl.to_incident_lists(g)
        end = time.time()

        results["to_incidents"] = end-start
# Paths
        # from_nodes = [2265, 2265, 2267, 7560, 7241, 2186, 2176, 2174, 2164, 2157, 1723, 1716]
        # to_nodes =   [980, 973, 992, 341, 993, 979, 988, 948, 995, 981, 271, 995]

        nodes = g.getReverseNodeMap()
        from_nodes = np.random.choice(list(nodes), size=pathsSize)
        to_nodes = np.random.choice(list(nodes), size=pathsSize)

        paths = []

        if do_paths:
            start = time.time()
            for fro in tqdm(from_nodes):
                for to in (to_nodes):
                    temp = tgl.minimum_transition_time_path(incidents, fro, to, g.getTimeInterval())
                    paths.append(temp)
            end = time.time()
            results["paths"] = end-start
            print(f"Time taken to get shortest paths {end-start} seconds")
        

# clustering coefficient
        # print('cc')
        start = time.time()

        tgl.temporal_clustering_coefficient(incidents, g.getTimeInterval())

        end = time.time()
        results["clusteringCoefficient"] = end-start
        print(f"Time to get clustering coefficient: {end - start}")
# Pagerank
        start = time.time()

        pr = tgl.temporal_pagerank(g, 0.5,0.5,0.5)

        end = time.time()
        # print(f"Pagerank value:   {pr}")
        results["pagerank"] = end-start
        print(f"Time to get Pagerank: {end - start}")


# Traingles and triplets

        # print("==================================================================================")
        # print(np.random.choice(paths, size=20))
        return results
    
    @profile
    def profile(): 
        TGBLibBenchmark.do_benchmark("C:/Users/dries/Documents/GitHub/Code/Data/Flights.txt", 10, do_paths = False)

# folder = "C:/Users/dries/Documents/GitHub/Code/Data/"

# files = ['enron', 'SocialEvo', 'wikipedia', 'UNvote', 'CanParl', 'reddit',  'lastfm', 'Flights', 'tgbl-review']


# for file in files:    
#         path = folder+file+'.txt'

#         res = TGBLibBenchmark.do_benchmark(path, 0, do_paths=false)

# TGBLibBenchmark.do_benchmark("C:/Users/dries/Documents/GitHub/Code/Data/Flights.txt", 10, do_paths = False)



def main():    
        # numbers = [random.randint(1,100) for i in range(1000)]
        lp = LineProfiler()
        lp_wrapper = lp(TGBLibBenchmark.profile)
        lp_wrapper()
        lp.print_stats()


        # lp_wrapper = lp(pandas_get_degrees)
        # lp_wrapper()
        # lp.print_stats()
        # tgl_get_degrees()
        # pandas_get_degrees()


if __name__ == '__main__':
        main()