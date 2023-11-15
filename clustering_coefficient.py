from itertools import combinations
from tqdm import tqdm
from collections import defaultdict
import dynetx.dynetx as dn
from dynetx.dynetx.algorithms.paths import *
import networkx as nx

"""
ti: (start, end)
tg: ()
"""

def temporal_clustering_coefficient(tg, ti):
    num_nodes = dn.number_of_nodes(tg) #tg.get_number_of_nodes()
    result = [0.0] * num_nodes
    timesteps = ti[1] - ti[0]

    nodes = tg.nodes()
    # print(nodes)
    # print ('edges')

    for nid in range(num_nodes):
        # print('=========================================================')
        # print('node: ', nodes[nid],'edges:' , dn.interactions(tg, nbunch=nodes[nid]))
    # for node in tg.nodes():
        neighbors = set()

        for e in dn.interactions(tg, nbunch=nodes[nid]):
            # print(e)
            # e = (v, u, dict('t', [tstart, tend]))
            for i in range(len(e[2]['t'])):
                # print(e[2]['t'][i][0])
                if not ti[0] <= e[2]['t'][i][0] <= ti[1]:
                    continue
                neighbors.add((e[0],e[1]))
            # if not ti[0] <= e.t <= ti[1]:
            #     continue
            # neighbors.add(e.v)

        

        # print('neighbors', neighbors)
        count = 0
        for v in neighbors:
            for e in dn.interactions(tg, nbunch=nodes[v[0]]):
                # print('edges', e)
                for i in range(len(e[2]['t'])):
                    # print('i', i, 't ', e[2]['t'][i][0])
                    if not ti[0] <= e[2]['t'][i][0] <= ti[1]:
                        count += 1
        # 
        if len(neighbors) <= 1:
            result[nid] = 0.0
        else:
            m = len(neighbors) * (len(neighbors) - 1)
            result[nid] = (1.0 / timesteps) * (count / m)

    return result

# g = dn.read_snapshots("./tglib/example_datasets/example_from_paper.tg", nodetype=int, timestamptype=int, directed=True, delimiter=" ")
# print(temporal_clustering_coefficient(g, (1,12)))