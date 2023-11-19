# import pytglib as tgl  # tglib
import scipy.stats as ss  # for Kendall's tau correlation
from tqdm import tqdm
import numpy as np

import dynetx.dynetx as dn
import dynetx.dynetx.algorithms as al

import time
import functools 

class BenchmarkDyNetX():
    def do_benchmark(inPath, numPaths):
        results = {}
        
        # statsFile = open(statsPath, 'a')
        # Load graph
        # inPath = './datasets/tgbl-wiki_edgelist_final_with_intervals.txt'
        start = time.time()
        h = dn.read_snapshots(inPath, nodetype=int, timestamptype=int, directed=True, delimiter=" ")

        end = time.time()
        results["loadTime"] = end-start
        print(f"Time taken to read graph {end-start} seconds")
        # statsFile.write(f"DYNETX: tgbl-wiki_edgelist_final_with_intervals.txt \n")
        # statsFile.write(f"Time taken to read graph {end-start} seconds \n")

        # get stats
        start = time.time()
        num_nodes = dn.number_of_nodes(h)
        num_edges = dn.number_of_interactions(h)
        ts = dn.temporal_snapshots_ids(h)
        num_ts = len(ts)
        min_ts = min(ts)
        max_ts = max(ts)
        min_in_degree = min((h.in_degree()).values())
        max_in_degree = max((h.in_degree()).values())
        min_out_degree = min((h.out_degree()).values())
        max_out_degree = max((h.out_degree()).values())
        num_interactions = len(h.interactions())

        end = time.time()
        results["stats"] = end-start
        print(f"Time taken to get stats {end-start} seconds")
        # statsFile.write(f"Time taken to get stats {end-start} seconds \n")

        print("===========stats===========")
        print("num_Nodes: ", num_nodes)
        print("num_edges: ", num_edges)
        print("number of interactions: ", num_interactions)
        print("number of timestamps: ", num_ts)
        print("min. timestamps: ", min_ts)
        print("max. timestamps: ", max_ts)
        print("min in degree: ", min_in_degree)
        print("max in degree: ", max_in_degree)
        print("min out degree: ", min_out_degree)
        print("max out degree: ", max_out_degree)
        print("===========================")
        # statsFile.write("num_Nodes: "+ str(num_nodes) + "\n")
        # statsFile.write("num_edges: " + str(num_edges) + "\n")
        # statsFile.write("number of interactions: " + str(num_interactions) + "\n")
        # statsFile.write("number of timestamps: " + str(num_ts) + "\n")
        # statsFile.write("min. timestamps: " + str(min_ts) + "\n")
        # statsFile.write("max. timestamps: " + str(max_ts) + "\n")
        # statsFile.write("min in degree: " + str(min_in_degree) + "\n")
        # statsFile.write("max in degree: " + str(max_in_degree) + "\n")
        # statsFile.write("min out degree: " + str(min_out_degree) + "\n")
        # statsFile.write("max out degree: " + str(max_out_degree) + "\n")

        # start = time.time()
        # print(min_ts)
        # print(max_ts)
        # cc = al.temporal_clustering_coefficient(h, (min_ts, max_ts))
        # end = time.time()
        # results["clusteringCoefficient"] = end-start
        # print(f"Time taken to get clustering coefficient {end-start} seconds")
        # statsFile.write(f"Time taken to get clustering coefficient {end-start} seconds \n")

        start = time.time()

        # get ?10%? of nodes and calculate paths
        nodes = h.nodes()
        num_select = int(np.floor(0.01 * num_nodes))

        selected_from = np.random.choice(nodes, size=numPaths)
        selected_to = np.random.choice(nodes, size=numPaths)

        pathStats = {}

        for fro in tqdm(selected_from):
            for to in (selected_to):

                paths = al.time_respecting_paths(h, fro, to)
                
                for path in paths:
                    if len(paths[path]) > 0:
                        annotated = (al.annotate_paths(paths[path]))
                        pathStats[(fro,to)] = annotated

        end = time.time()
        tt = end-start
        m, s = divmod(tt, 60)
        h, m = divmod(m, 60)
        
        results["paths"] = end-start
        print(f"Time taken to get and annotate {num_select * 5} paths {tt} seconds or {int(h)}:{int(m)}:{s}")
        
        return results
        # statsFile.write(f"Time taken to get and annotate {num_select * 5} paths {tt} seconds or {int(h)}:{int(m)}:{s}" + "\n")
        
        # statsFile.write(str(pathStats))
        # statsFile.write("\n")
        # statsFile.write("\n")
        # statsFile.write("\n")

        # statsFile.close()

# inPath = "tgbl-wiki_edgelist.txt"
# res = BenchmarkDyNetX.do_benchmark(inPath,5)
# print(res)
# inPath = "tgbl-review_edgelist_final.txt"
# res = BenchmarkDyNetX.do_benchmark(inPath,5)
# print(res)
