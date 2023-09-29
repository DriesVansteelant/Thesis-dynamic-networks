import pytglib as tgl  # tglib
import scipy.stats as ss  # for Kendall's tau correlation

# no read file => open folder in terminal

# The example from the paper
# TODO: convert csv ("ts,u,v, weigth") to "u v ts"
# tgs = tgl.load_ordered_edge_list("../example_datasets/tgbl-review_edgelist_v2.csv")

# f = open("../example_datasets/test.tg", "r")
# print(f.read()) 
tgs = tgl.load_ordered_edge_list("./tglib/example_datasets/test.tg")
stats = tgl.get_statistics(tgs)
print(stats)


closeness_fastest = tgl.temporal_closeness(tgs, tgl.Distance_Type.Fastest)
closeness_ea = tgl.temporal_closeness(tgs, tgl.Distance_Type.Earliest_Arrival)
tau, p_value = ss.kendalltau(closeness_fastest, closeness_ea)
print(tau, p_value)  