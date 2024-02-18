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

from line_profiler import profile, LineProfiler

# import pytglib as tgl

from stats import collect_node_statistics, collect_edge_statistics

import time

inPath = '../Code/Data/enron.csv'
inPathTG = '../Code/Data/enron.txt'

@profile
def tgl_get_cc():
    start = time.time()
    directed = True
    g = tgl.load_ordered_edge_list(inPathTG, directed)
    incidents = tgl.to_incident_lists(g)
    cc = tgl.temporal_clustering_coefficient(incidents, g.getTimeInterval())
    end = time.time()

@profile
def pandas_get_degrees():
    start = time.time()
    edges_df = pd.read_csv(inPath, delimiter=",")

    # print(edges_df)

    collect_node_statistics(edges_df)
    # collect_edge_statistics(edges_df)
    end = time.time()

    print('pandas time: ' + str((end - start)))



# @profile
def main():    
    # numbers = [random.randint(1,100) for i in range(1000)]
    lp = LineProfiler()
    lp_wrapper = lp(tgl_get_cc)
    lp_wrapper()
    lp.print_stats()

    
    # lp_wrapper = lp(pandas_get_degrees)
    # lp_wrapper()
    # lp.print_stats()
    # tgl_get_degrees()
    # pandas_get_degrees()


if __name__ == '__main__':
    main()