import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

from pairing import SzudzikPair
# from shared_utils import minmaxscale


def collect_node_statistics(df):
    """An in-place function that adds the following columns to the dataframe:
    - src_arrival_rank: the arrival rank of the source node
    - dst_arrival_rank: the arrival rank of the destination node
    - src_degree: the degree of the source node
    - dst_degree: the degree of the destination node
    Args:
        df (pd.DataFrame): a dataframe of events
    """

    df_dup = pd.concat([df.reset_index(), df.reset_index()]).sort_values("index")
    df_dup["node"] = np.transpose(np.vstack([df.u.values, df.i.values])).ravel()
    df_dup["node_degree"] = df_dup.groupby("node")["ts"].rank(method="first")
    df_dup["role"] = np.tile(["u", "i"], len(df))
    df_node = (
        df_dup.groupby("node")
        .agg(
            t_min=("ts", "min"),
            t_max=("ts", "max"),
        )
        .sort_values(["t_min", "t_max"], ascending=True)
    )

    df_node["rank"] = np.arange(len(df_node))

    df["src_arrival_rank"] = df.u.map(df_node["rank"])
    df["dst_arrival_rank"] = df.i.map(df_node["rank"])

    df_dup = df_dup.set_index("role")

    df["src_degree"] = df_dup.loc["u", "node_degree"].values
    df["dst_degree"] = df_dup.loc["i", "node_degree"].values
    # return df


def collect_edge_statistics(df):
    df["edge_key"] = SzudzikPair.encode(df.u, df.i)

    df["edge_degree"] = df.groupby("edge_key")["ts"].rank(method="first").values

    df_edge = df.groupby("edge_key").agg(
        t_min=("ts", "min"),
        t_max=("ts", "max"),
        edge_count=("ts", "count"),
        u=("u", "first"),
        i=("i", "first"),
    )
    df_edge.sort_values(["t_min", "t_max"], inplace=True)
    df_edge["rank"] = np.arange(len(df_edge))
    # df_edge.loc[df.edge_key, 'rank'].values
    df["edge_arrival_rank"] = df_edge.loc[df.edge_key, "rank"].values


# def temporal_node_traffic(src, dst, t):
#     df = pd.DataFrame(
#         {
#             "u": src,
#             "i": dst,
#             "absolute_t": t,
#             "ts": minmaxscale(t),
#         }
#     )
#     df["node"] = df.apply(lambda x: [x["u"], x["i"]], axis=1)
#     df = df.explode("node")
#     df["node"] = df["node"].astype(int)
#     df_node = (
#         df.groupby("node")
#         .agg(
#             t_min=("ts", "min"),
#             t_max=("ts", "max"),
#         )
#         .sort_values(["t_min", "t_max"], ascending=True)
#     )
#     df_node["rank"] = np.arange(len(df_node))
#     df_node["x_pos"] = minmaxscale(df_node["rank"].values)
#     return df_node


# def temporal_sender_traffic(src, t):
#     df = pd.DataFrame(
#         {
#             "u": src,
#             "absolute_t": t,
#             "ts": minmaxscale(t),
#         }
#     )

#     df_sender = (
#         df.groupby("u")
#         .agg(t_min=("ts", "min"), t_max=("ts", "max"))
#         .sort_values(["t_min", "t_max"], ascending=True)
#     )
#     df_sender["rank"] = np.arange(len(df_sender))
#     df_sender["x_pos"] = minmaxscale(df_sender["rank"].values)
#     return df_sender


# def temporal_receiver_traffic(dst, t):
#     df = pd.DataFrame(
#         {
#             "i": dst,
#             "absolute_t": t,
#             "ts": minmaxscale(t),
#         }
#     )

#     df_receiver = (
#         df.groupby("i")
#         .agg(t_min=("ts", "min"), t_max=("ts", "max"))
#         .sort_values(["t_min", "t_max"], ascending=True)
#     )
#     df_receiver["rank"] = np.arange(len(df_receiver))
#     df_receiver["x_pos"] = minmaxscale(df_receiver["rank"].values)
#     return df_receiver


# def temporal_edge_traffic(src, dst, t):
#     df = pd.DataFrame(
#         {
#             "u": src,
#             "i": dst,
#             "absolute_t": t,
#             "ts": minmaxscale(t),
#         }
#     )

#     df["edge_key"] = SzudzikPair.encode(df["u"].values, df["i"].values)

#     df_edge = df.groupby(["edge_key"]).agg(
#         t_min=("ts", "min"),
#         t_max=("ts", "max"),
#         edge_count=("ts", "count"),
#         src=("u", "first"),
#         dst=("i", "first"),
#     )
#     df_edge.sort_values(["t_min", "t_max"], inplace=True)
#     df_edge["rank"] = np.arange(len(df_edge))
#     df_edge["x_pos"] = minmaxscale(df_edge["rank"])
#     return df_edge


# def get_x_tet(src, dst, t):
#     """
#     A helper function that directly returns the x_tet values for each event
#     """
#     df = pd.DataFrame(
#         {
#             "u": src,
#             "i": dst,
#             "absolute_t": t,
#             "ts": minmaxscale(t),
#         }
#     )

#     df["edge_key"] = SzudzikPair.encode(df["u"].values, df["i"].values)

#     df_edge = df.groupby(["edge_key"]).agg(
#         t_min=("ts", "min"),
#         t_max=("ts", "max"),
#         edge_count=("ts", "count"),
#         src=("u", "first"),
#         dst=("i", "first"),
#     )
#     df_edge.sort_values(["t_min", "t_max"], inplace=True)
#     df_edge["rank"] = np.arange(len(df_edge))
#     df_edge["x_pos"] = minmaxscale(df_edge["rank"])
#     x_tet = df_edge.loc[df["edge_key"], "x_pos"].values
#     return x_tet


# def get_test_only_edges(events):
#     """Calculate test only edges"""
#     test_mask = events.index.get_level_values("split") == "test"
#     train_mask = events.index.get_level_values("split") == "train"
#     val_mask = events.index.get_level_values("split") == "val"
#     edge_keys = SzudzikPair.encode(events.src, events.dst)
#     keys_observed_during_test_only = (
#         set(edge_keys.loc[test_mask])
#         - set(edge_keys.loc[train_mask])
#         - set(edge_keys.loc[val_mask])
#     )
#     src_test_only, dst_test_only = SzudzikPair.decode(
#         np.array(list(keys_observed_during_test_only))
#     )

#     return src_test_only, dst_test_only


# def get_test_only_nodes(events):
#     """Calculate test only nodes"""

#     node_cols = ["u", "i"]
#     nodes_observed_during_test_only = (
#         set(events.loc["test", node_cols])
#         - set(events.loc["train", node_cols])
#         - set(events.loc["val", node_cols])
#     )

#     return np.array(list(nodes_observed_during_test_only))


# def get_test_only_senders(events):
#     """Calculate test only nodes"""

#     src_observed_during_test_only = (
#         set(events.loc["test", "u"])
#         - set(events.loc["train", "u"])
#         - set(events.loc["val", "u"])
#     )

#     return np.array(list(src_observed_during_test_only))


# def get_test_only_receivers(events):
#     """Calculate test only nodes"""

#     dst_observed_during_test_only = (
#         set(events.loc["test", "i"])
#         - set(events.loc["train", "i"])
#         - set(events.loc["val", "i"])
#     )

#     return np.array(list(dst_observed_during_test_only))


# def get_temporal_edge_degree(src, dst, t):
#     """
#     For each event, return the number of past interactions of the edge just after the event.
#     """
#     df = pd.DataFrame({"u": src, "i": dst, "ts": t})

#     edge_key = ["u", "i"]

#     return df.groupby(edge_key)["ts"].rank(method="first").values


# def get_temporal_node_degrees(src, dst, t):
#     """
#     For each event, return the number of past interactions of the source and the destination
#     just after the event.
#     """
#     df = pd.DataFrame({"u": src, "i": dst, "ts": t})

#     df_node = pd.concat([df.reset_index(), df.reset_index()]).sort_values("ts")
#     df_node["node"] = np.transpose(np.vstack([df.src.values, df.dst.values])).ravel()

#     df_node["node_event_rank"] = df_node.groupby("node")["ts"].rank(method="first")
#     df_node["role"] = np.tile(["u", "i"], len(df))
#     df_node = df_node.set_index(["role"])

#     src_degree = df_node.loc["u", "node_event_rank"].values
#     dst_degree = df_node.loc["i", "node_event_rank"].values

#     return src_degree, dst_degree


# def plot_tet(
#     df,
#     x="x_tet",
#     y="t_scaled",
#     size="size",
#     ax=None,
#     *args,
#     **kwargs,
# ):
#     ax = plt.gca() if ax is None else ax

#     sns.scatterplot(
#         data=df,
#         x="x_tet",
#         y="t_scaled",
#         hue="best_ns",
#         size="size",
#         sizes=(1, 50),
#         palette=palette,
#         alpha=0.5,
#     )
