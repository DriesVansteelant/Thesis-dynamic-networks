import sys
# import pytglib as tgl  # tglib
import scipy.stats as ss  # for Kendall's tau correlation
from tqdm import tqdm
# sys.path.append("/dynetx/dynetx")
# print(sys.path)
import dynetx.dynetx as dn
import dynetx.dynetx.algorithms as al
import time
import matplotlib.pylab as plt
import numpy as np


list1 = [1,2,3,4,5,6]
list2 = [2,3,4,5,6,7]
labels = ["jeff","piet","jan","rogier","kurt","jorik"]
    memory_results = {}
    for struct in structs:
        for dataset_name in datasets:
            memory_results.setdefault(struct, {})[dataset_name] = pickle.load(open(f'memory_results_{struct}_{dataset_name}.pkl', 'rb'))

    fig, ax = plt.subplots()
    width = 0.15
    offset = {'interval': 2 * width, 'snapshot': 1 * width, 'adjtree': 0 * width, 'tvg': -1 * width,'networkx': -2 * width}
    color = {'interval': (0.65, 0.3, 0.3), 'snapshot': (0, 0.75, 0), 'networkx': (0.8, 0.8, 0.8), 'adjtree': (0, 0, .75), 'tvg': (1, 1, 0)}
    labels = {'interval': 'IntervalGraph', 'snapshot': 'SnapshotGraph', 'networkx': 'NetworkX', 'adjtree': 'AdjTree', 'tvg': 'TVG'}
    label_location = np.arange(len(datasets))

    for struct in structs:
        nums = [memory_results[struct][d] for d in memory_results[struct]]
        ax.barh(label_location + offset[struct], nums, width, label=labels[struct], color=color[struct])

    # ax.set_title('Memory')
    ax.set_yticks(label_location)
    ax.set_yticklabels(datasets)
    ax.set_xscale('log')
    ax.set_xlabel('Memory (MB)')
    fig.tight_layout()
    fig.set_figheight(4)
    fig.set_figwidth(6)
    plt.tight_layout(pad=0.2)
    plt.legend()
    fig.savefig('memory.eps', format='eps')
    plt.show()

# outp = open('./tglib/example_datasets/edgeList_final.txt', 'w')
# outp.write('')
# outp.close()

# outp = open('./tglib/example_datasets/edgeList_final.txt', 'a')
# inp = open('./tglib/example_datasets/tgbl-review_edgelist_v2.csv', 'r')

# # path = "./tglib/example_datasets/tgbl-review_edgelist_v2.csv"
# # lines = (line.decode('utf-8') for line in path)

# line = inp.readline()
# line = inp.readline()
# while line:
#     # print(line)
#     s = line.strip().split(',')

#     brol = s.pop()
#     source = s.pop()
#     target = s.pop()
#     # ts2 = float(ts)+50
#     ts = s.pop()

#     newline = source + " " + target + " " + ts + "\n"

#     outp.write(newline)
#     line = inp.readline()

# inp.close()
# outp.close()
print('file Formatted, loading list')

# ================================ dynetX ====================================


# start = time.time()
# h = dn.read_snapshots("./tglib/example_datasets/edgeList_final.txt", nodetype=int, timestamptype=int)
# # h = dn.read_snapshots("./tglib/example_datasets/example_from_paper.tg", nodetype=int, timestamptype=int)
# end = time.time()

# print(f"Time taken to read graph {end-start} seconds")
# print(len(h.interactions()))
# print(h.interactions()[0])
# pts = al.time_respecting_paths(h, 30122, 18303)
# pts2 = al.all_time_respecting_paths(h)
end1 = time.time()

# print(f"Time taken to calculate paths between 1 set of nodes {end1-end} seconds")
# print(pts2)

# tgs = tgl.load_ordered_edge_list("./tglib/example_datasets/edgeList_final.txt")
# tg = tgl.to_incident_lists(tgs)
# edges = tgs.getEdges()[0:100]

# t1 = time.time()
# e2 = 30122
# for e1 in tqdm(edges):
#         if(e1!=e2):
#             pats = al.time_respecting_paths(h,e1.u)   
# t2=time.time()
# print("time: ", t2-t2)     
# pts = al.all_time_respecting_paths(h, e1.u, e2)
# t3 = time.time()
# print("time: ", t3-t2)
# print(pts2)
# ================================ tglib =====================================

# tgs = tgl.load_ordered_edge_list("./tglib/example_datasets/edgeList_final.txt")
# stats = tgl.get_statistics(tgs)
# print(stats)
# print('loaded')
# tg = tgl.to_incident_lists(tgs)

# print('to incidentList')
# edges = tgs.getEdges()[0:5000]



# sps = []
# print((tg))
# e2 = 30122
# for e1 in tqdm(edges):
#         if(e1!=e2):
#             tgl.minimum_transition_time_path(tg, e1.u, e2, tgs.getTimeInterval())

