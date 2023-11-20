from raphtory import Graph
from raphtory import algorithms as algo
import time 
from tqdm import tqdm
import pandas as pd

# start = time.time()
# edges_df = pd.read_csv("tgbl-review_edgelist_v2.csv")
# end = time.time()
# print(f"Time to read pandas from file: {end - start}")

# start = time.time()
# g = Graph.load_from_pandas(
#     edge_df=edges_df,
#     edge_src="source",
#     edge_dst="target",
#     edge_time="ts",
#     edge_props=["weight"],
# )
# end = time.time()

# print(f"Time to load graph from pandas: {end - start}")


start = time.time()
edges_df = pd.read_csv("tgbl-wiki_edgelist.txt", delimiter=" ")
end = time.time()
print(f"Time to read pandas from file: {end - start}")

start = time.time()
g = Graph.load_from_pandas(
    edge_df=edges_df,
    edge_src="s",
    edge_dst="d",
    edge_time="ts",
    # edge_props=["weight"],
)
end = time.time()

print(f"Time to load graph from pandas: {end - start}")

start = time.time()
print("The resulting graphs and example vertex/edge:")
print(g)
print(g.vertex("0"))
print(g.edge("0", "3"))
end = time.time()

print(f"Time to print random info: {end - start}")


# stats


start = time.time()
num_nodes = g.count_vertices()
num_edges = g.count_edges()
min_in_deg = algo.min_in_degree(g)
max_in_deg = algo.max_in_degree(g)
min_out_deg = algo.min_out_degree(g)
max_out_deg = algo.max_out_degree(g)
min_ts = g.start
max_ts = g.end
# print(f"num_nodes: {num_nodes}")
# print(f"num_edges: {num_edges}")
# print(f"min_in_deg: {min_in_deg}")
# print(f"max_in_deg: {max_in_deg}")
# print(f"min_out_deg: {min_out_deg}")
# print(f"max_out_deg: {max_out_deg}")
# print(f"min_ts: {min_ts}")
# print(f"max_ts: {max_ts}")

end = time.time()

print(f"Time to get stats: {end - start}")

# print(g.vertices)
nodes = [x.name for x in g.vertices] 

# reachable = algo.temporally_reachable_nodes(g, 9999999, 0, nodes)
# print(reachable.to_string())
# print(reachable.to_df())

for s in tqdm(g.vertices):
    path = algo.temporally_reachable_nodes(g, 9999999, 0, nodes)
    # print(f"source: {s}")
    # if(len(path.get_all()) > 0):
    #     print(path.to_string())
    #     print(path.to_df())
    #     print("==================================")
        
# for s in tqdm(g.vertices):
#     path = algo.single_source_shortest_path(g, str(s))
#     # print(f"source: {s}")
#     if(len(path.get_all()) > 0):
#         print(path.to_string())
#         print(path.to_df())
#         print("==================================")


# print("Edge Dataframe:")
# print(f"{edges_df}\n")
# print("Vertex Dataframe:")
# print(f"{vertices_df}\n")