from raphtory import Graph
from raphtory import algorithms as algo
import pandas as pd

edges_df = pd.read_csv("tgbl-review_edgelist_v2.csv")
# pd.read_csv('tglib/example_datasets/example_from_paper.tg', sep=" ", header=None)
print("Edge Dataframe:")
print(f"{edges_df}\n")

g = Graph.load_from_pandas(
    edge_df=edges_df,
    edge_src="source",
    edge_dst="target",
    edge_time="ts",
    edge_props=["weight"],
)

print("The resulting graphs and example vertex/edge:")
print(g)
print(g.vertex("2729"))
print(g.edge("2729", "117010"))

# print("Edge Dataframe:")
# print(f"{edges_df}\n")
# print("Vertex Dataframe:")
# print(f"{vertices_df}\n")