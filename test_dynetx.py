import dynetx.dynetx as dn
import dynetx.dynetx.algorithms as al
import time




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


start = time.time()
h = dn.read_snapshots("./tglib/example_datasets/edgeList_final.txt", nodetype=int, timestamptype=float)
end = time.time()

# print(f"Time taken to read graph {end-start} seconds")
# print(len(h.interactions()))
# print(h.interactions()[0])
# pts = al.time_respecting_paths(h, 30122, 18303)
# end1 = time.time()

# print(f"Time taken to calculate paths between 1 set of nodes {end1-end} seconds")
# print(pts)


pts2 = al.all_time_respecting_paths(h, start=0, end=5000, sample=100)
print(pts2)