from raphtory import Graph
from raphtory import algorithms as algo
import pandas as pd

edges_df = pd.read_fwf("tglib/example_datasets/example_from_paper.tg", header=None)
# pd.read_csv('tglib/example_datasets/example_from_paper.tg', sep=" ", header=None)
print("Edge Dataframe:")
print(f"{edges_df}\n")

# edges_df["timestamp"] = pd.to_datetime(edges_df["timestamp"]).astype(
#     "datetime64[ms, UTC]"
# )

# vertices_df = pd.read_csv("data/network_traffic_vertices.csv")
# vertices_df["timestamp"] = pd.to_datetime(vertices_df["timestamp"]).astype(
#     "datetime64[ms, UTC]"
# )

# print("Edge Dataframe:")
# print(f"{edges_df}\n")
# print("Vertex Dataframe:")
# print(f"{vertices_df}\n")