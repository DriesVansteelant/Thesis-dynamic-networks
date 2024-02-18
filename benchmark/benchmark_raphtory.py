from raphtory import Graph
from raphtory import algorithms as algo
import time 
from tqdm import tqdm
import pandas as pd


class BenchmarkRaphtory():
    def do_benchmark(inPath):
        results = {}
        
# Load Graph
        start = time.time()
        edges_df = pd.read_csv(inPath, delimiter=" ")
        end = time.time()

        results["loadTime"] = end-start
        print(f"Time to read pandas from file: {round(end - start, 2)}")

        start = time.time()
        g = Graph.load_from_pandas(
            edge_df=edges_df,
            edge_src="s",
            edge_dst="d",
            edge_time="ts",
            # edge_props=["weight"],
        )
        end = time.time()

        results["loadTime"] += end-start
        print(f"Time to load graph from pandas: {end - start}")

# Get statistcs (maybe: avg degree + see tglib)
        start = time.time()
        num_nodes = g.count_nodes()
        num_edges = g.count_edges()
        num_interactions = g.count_temporal_edges()

        num_temp_edges = g.count_temporal_edges()
        min_in_deg = algo.min_in_degree(g)
        max_in_deg = algo.max_in_degree(g)
        min_out_deg = algo.min_out_degree(g)
        max_out_deg = algo.max_out_degree(g)
        min_ts = g.start
        max_ts = g.end
        end = time.time()
        print(f"num_nodes: {num_nodes}")
        print(f"num_edges: {num_edges}")
        print(f"num_temp_edges: {num_temp_edges}")
        print(f"min_in_deg: {min_in_deg}")
        print(f"max_in_deg: {max_in_deg}")
        print(f"min_out_deg: {min_out_deg}")
        print(f"max_out_deg: {max_out_deg}")
        print(f"min_ts: {min_ts}")
        print(f"max_ts: {max_ts}")


        results["num_nodes"] = num_nodes
        results["num_edges"] = num_edges
        results["num_temporal_edges"] = num_temp_edges
        results["stats"] = end-start
        print(f"Time to get stats: {end - start}")
        results["num_nodes"] = num_nodes
        results["num_edges"] = num_edges
        results["num_interactions"] = num_interactions
# Paths
        """..."""
        # algo.single_source_shortest_path(g,g.vertex(2265))


# clustering coefficient
        start = time.time()

        cc = algo.global_clustering_coefficient(g)

        end = time.time()
        results["clusteringCoefficient"] = end-start
        print(f"Time to get clustering coefficient: {end - start}")

# Pagerank
        start = time.time()

        pr = algo.pagerank(g)

        end = time.time()
        results["pagerank"] = end-start
        print(f"Time to get Pagerank: {end - start}")

# Traingles and triplets
        """..."""


        results["density"] = algo.directed_graph_density(g)

        return results

# inPath = "../Code/Data/enron_h.txt"
# res = BenchmarkRaphtory.do_benchmark(inPath)
# print(res)
inPath = "C:/Users/dries/Documents/GitHub/Code/Data/Flights_h.txt"
BenchmarkRaphtory.do_benchmark(inPath)
# print(res)