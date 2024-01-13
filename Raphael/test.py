import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

import tglib.tglib_cpp.build.src.python_binding.Release.pytglib as tgl  # tglib 

# import pytglib as tgl

from stats import collect_node_statistics, collect_edge_statistics

import time

inPath = '../Code/Data/enron.csv'
inPathTG = '../Code/Data/enron.txt'


start = time.time()
directed = True
g = tgl.load_ordered_edge_list(inPathTG, directed)
degrees = tgl.get_degrees(g)
end = time.time()

for d in degrees:
    print(d)
print('TGLib time: ' + str(end - start))
print(degrees.keys())

start = time.time()
edges_df = pd.read_csv(inPath, delimiter=",")

# print(edges_df)

collect_node_statistics(edges_df)
# collect_edge_statistics(edges_df)
end = time.time()

print('pandas time: ' + str((end - start)))

# edges_df.to_excel('rapha.xlsx', sheet_name='enron')

# print(edges_df)