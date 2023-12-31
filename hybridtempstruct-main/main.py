import glob
import os
import csv
from datetime import datetime as dt
import re
import pickle
import random
import math
from timeit import default_timer as timer
from itertools import product
import multiprocessing as mp
import tqdm
from pympler import asizeof
import matplotlib.pylab as plt
from random import sample

from intervalIntervalGraph import IntervalGraph
from snapshotGraph import SnapshotGraph
import networkx as nx
from networkx import MultiGraph
from dictsortlist import AdjTree
from tvg import TVG

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, balanced_accuracy_score

if __name__ == "__main__":

    creation_results = {}

def load_from_txt(path, delimiter=" ", nodetype=int, intervaltype=float, order=('u', 'v', 'begin', 'end'), comments="#", impulse=False):
    if delimiter == '=':
        raise ValueError("Delimiter cannot be =.")

    data = []
    with open(path, 'r') as file:
        begin = 0
        end = 0
        t = 0
        for line in file:
            p = line.find(comments)
            if p >= 0:
                line = line[:p]
            if not len(line):
                continue

            line = line.rstrip().split(delimiter)
            if len(order) == 4:
                u = line[order.index('u')]
                v = line[order.index('v')]
                begin = line[order.index('begin')]
                end = line[order.index('end')]
            elif len(order) == 3 and not impulse:
                u = line[order.index('u')]
                v = line[order.index('v')]
                begin = float(line[order.index('end')]) - 20
                end = line[order.index('end')]
            elif len(order) == 3:
                u = line[order.index('u')]
                v = line[order.index('v')]
                t = float(line[order.index('timestamp')])

            else:
                raise ValueError('Invalid Order')

            if nodetype is not int:
                try:
                    u = nodetype(u)
                    v = nodetype(v)
                except:
                    raise TypeError("Failed to convert node to {0}".format(nodetype))
            else:
                try:
                    u = int(u)
                    v = int(v)
                except:
                    pass

            try:
                begin = intervaltype(begin)
                end = intervaltype(end)
                t = intervaltype(t)
            except:
                raise TypeError("Failed to convert interval time to {}".format(intervaltype))

            if not impulse:
                data.append((u, v, begin, end))
            else:
                data.append((u, v, t, t))

    return data


def generateStructures(struct_item, dataset_item):
    struct_name, structure = struct_item
    dataset_name, dataset = dataset_item
    if type(structure) == MultiGraph:
        start_time = timer()
        for edge in dataset:
            structure.add_edge(edge[0], edge[1], begin=edge[2], end=edge[3])
        creation_time = timer() - start_time
    elif type(structure) == SnapshotGraph:
        start_time = timer()
        structure.add_edges_from(dataset)
        creation_time = timer() - start_time
    else:
        start_time = timer()
        for edge in dataset:
            structure.add_edge(*edge)
        creation_time = timer() - start_time

    print(f'{struct_name}_{dataset_name} finished!')
    return creation_time, struct_name, dataset_name, structure


def generateCompoundSlices(inputs):
    # global creation_results
    G = inputs[2][inputs[0]][inputs[1]][0]
    if type(G) == MultiGraph:
        node_list = list(G.nodes)
        graph_begin = math.inf
        graph_end = -math.inf
        for u, v, d in G.edges(data=True):
            graph_begin = min(graph_begin, d['begin'])
            graph_end = max(graph_end, d['end'])
    else:
        node_list = list(G.node.keys())
        graph_begin, graph_end = G.interval()
    while True:
        node_percent = random.randint(1, 50)
        interval_percent = random.randint(1, 50)
        begin = random.randint(graph_begin, graph_end - math.ceil((graph_end - graph_begin) * interval_percent / 100))
        nodes = set(random.choices(node_list, k=math.floor(node_percent / 100 * len(node_list))))
        end = begin + (graph_end - graph_begin) * interval_percent / 100

        node_edges = set()

        if type(G) == TVG:
            start_timer = timer()
            for b in G.adj.irange(begin, end, inclusive=(True, False)):
                for e in G.adj[b].irange(b, end, inclusive=(True, False)):
                    for u in nodes:
                        if u in G.adj[b][e]:
                            for v in G.adj[b][e][u]:
                                for edge in G.adj[b][e][u][v]:
                                    if edge not in node_edges:
                                        node_edges.add(edge)
            node_time = timer() - start_timer
        elif type(G) == MultiGraph:
            start_timer = timer()
            for u, v, d in G.edges(nodes, data=True):
                edge = (u, v, d['begin'], d['end'])
                if edge not in node_edges and (d['begin'] == begin or (d['begin'] > begin and d['end'] < end)):
                    node_edges.add(edge)
            node_time = timer() - start_timer
        else:
            start_timer = timer()
            for u in nodes:
                for v in G.adj[u]:
                    for edge in G.adj[u][v]:
                        if edge not in node_edges and (edge.begin == begin or (edge.begin > begin and edge.end < end)):
                            node_edges.add(edge)
            node_time = timer() - start_timer

        if len(node_edges) == 0:
            continue

        interval_edges = []
        if type(G) == MultiGraph or type(G) == TVG:
            interval_time = node_time
        else:
            start_timer = timer()
            for edge in G.slice(begin, end):
                if edge.u in nodes or edge.v in nodes:
                    interval_edges.append(edge)
            interval_time = timer() - start_timer

        return (node_time, interval_time, node_percent, interval_percent, nodes, begin, end, len(node_edges))


def generateSlices(inputs):
    # global creation_results
    G = inputs[2][inputs[0]][inputs[1]][0]
    if type(G) == MultiGraph:
        graph_begin = math.inf
        graph_end = -math.inf
        for u, v, d in G.edges(data=True):
            graph_begin = min(graph_begin, d['begin'])
            graph_end = max(graph_end, d['end'])
    else:
        graph_begin, graph_end = G.interval()

    times = []
    for interval_percent in [1, 5, 10, 20]:
        begin = random.randint(graph_begin, graph_end - math.ceil((graph_end - graph_begin) * interval_percent / 100))
        end = begin + (graph_end - graph_begin) * interval_percent / 100

        slice_edges = set()
        if type(G) == MultiGraph:
            start_timer = timer()
            for u, v, d in G.edges(data=True):
                if d['begin'] == begin or (d['begin'] > begin and d['end'] < end):
                    slice_edges.add((u, v, d['begin'], d['end']))
            interval_time = timer() - start_timer
        else:
            start_timer = timer()
            for edge in G.slice(begin, end):
                slice_edges.add(edge)
            interval_time = timer() - start_timer
        times.append(interval_time)
    return tuple(times)


def generateFeatures(dataset_name, result):
    global creation_results, slice_results

    feats = []
    times = []
    G = creation_results['interval'][dataset_name][0]
    for funct in [generateNodePercent, generateIntervalPercent, generateMeanWeightedNodeDegree, generateLifeSpan, generateBins]:
        start_time = timer()
        r = funct(result, G)
        t = timer() - start_time
        if funct == generateBins:
            feats.extend(r)
            times.extend([t/3]*3)
        else:
            feats.append(r)
            times.append(t)

    return feats, times, (result[0], result[1])


def generateNodePercent(result, G):
    return len(result[4]) / len(G.node)


def generateIntervalPercent(result, G):
    return (result[6] - result[5]) / (G.end - G.begin)


def generateMeanNodeDegree(result, G):
    edges = set()
    for u in result[4]:
        for v in G.adj[u]:
            edges.add((u, v))
    return len(edges) / len(result[4])


def generateMeanWeightedNodeDegree(result, G):
    e = 0
    for u in result[4]:
        for v in G.adj[u]:
            e += len(G.adj[u][v])
    return e / len(result[4])


def generateTemporalDurations(result, G):
    durations = []
    for u in result[4]:
        for v in G.adj[u]:
            for edge in G.adj[u][v]:
                durations.append(edge.end - edge.begin)
    return sum(durations) / len(durations)


def generateLifeSpan(result, G):
    graph_begin, graph_end = G.interval()
    lifespans = []
    for u in result[4]:
        u_start, u_end = G.lifespans[u][0], G.lifespans[u][-1]
        lifespans.append((u_end - u_start) / (graph_end - graph_begin))
    return sum(lifespans) / len(lifespans)


def generateBins(result, dataset_name):
    begin, end = result[5], result[6]
    global numEdges
    overlappingEdges = []
    for b, e in numEdges[dataset_name]:
        if b == begin or (e > begin and b < end):
            overlappingEdges.append(numEdges[dataset_name][(b, e)])

    if len(overlappingEdges) == 0:
        return 0, 0, 0
    return min(overlappingEdges), max(overlappingEdges), sum(overlappingEdges) / len(overlappingEdges)


def generateNodeEdges(result, G):
    e = 0
    for u in result[4]:
        for v in G.adj[u]:
            e += len(G.adj[u][v])
    return e / G.number_of_edges


def generateCaseStudy():
    iG, iG_creation_time = pickle.load(open(f'creation_results_interval_bikeshare.pkl', 'rb'))
    nG, nG_creation_time = pickle.load(open(f'creation_results_networkx_bikeshare.pkl', 'rb'))
    graph_begin, graph_end = iG.interval()

    interval_slice_times = []
    networkx_slice_times = []
    raw_slice_times = []
    analysis_times = []

    begin = graph_begin
    while begin < graph_end:
        end = begin + 60 * 60 * 24
        # Interval Graph Slice
        start_timer = timer()
        G1 = nx.Graph()
        for edge in iG.slice(begin, end):
            G1.add_edge(edge.u, edge.v, begin=edge.begin, end=edge.end)
        interval_slice_times.append(timer() - start_timer)

        # NetworkX Slice
        start_timer = timer()
        G2 = nx.Graph()
        for u, v, d in nG.edges(data=True):
            if d['begin'] == begin or (d['begin'] < end and begin < d['end']):
                G2.add_edge(u, v, begin=d['begin'], end=d['end'])
        networkx_slice_times.append(timer() - start_timer)

        # Raw Text Slice
        start_timer = timer()
        G3 = nx.Graph()
        for filename in glob.glob(os.path.join('2016TripDataZip', '*.csv')):
            with open(filename, 'r') as file:
                next(file)
                for line in csv.reader(file, delimiter=","):
                    if len(line) < 9:
                        continue
                    start_station_id = line[7]
                    end_station_id = line[4]
                    start_date = line[6]
                    end_date = line[3]
                    try:
                        day, month, year, hour, minute = re.split('\s|/|:', end_date)
                        end_time = dt(int(year), int(month), int(day), int(hour), int(minute)).timestamp()
                        day, month, year, hour, minute = re.split('\s|/|:', start_date)
                        start_time = dt(int(year), int(month), int(day), int(hour), int(minute)).timestamp()
                    except:
                        continue
                    if start_time == begin or (start_time < end and begin < end_time):
                        G3.add_edge(start_station_id, end_station_id, begin=start_time, end=end_time)

        # Analysis - (All subgraphs, G1, G2, G3 are same at this point, only have to calculate once)
        if G1.number_of_edges() != 0:
            start_timer = timer()
            nx.betweenness_centrality(G1)
            analysis_times.append(timer() - start_timer)
        else:
            analysis_times.append(0)

        begin = end
        print(len(interval_slice_times))

    return (iG_creation_time, sum(interval_slice_times), nG_creation_time, sum(networkx_slice_times), sum(raw_slice_times), sum(analysis_times))


if __name__ == "__main__":
    print("RUNNING MAIN")

    ## LOAD DATASETS
    data_edge_lists = {}
    ## bikeshare dataset is unique format
    # for filename in glob.glob(os.path.join('2016TripDataZip', '*.csv')):
    #     with open(filename, 'r') as file:
    #         next(file)
    #         for line in csv.reader(file, delimiter=","):
    #             if len(line) < 9:
    #                 continue
    #             start_station_id = line[7]
    #             end_station_id = line[4]
    #             start_date = line[6]
    #             end_date = line[3]
    #             try:
    #                 day, month, year, hour, minute = re.split('\s|/|:', end_date)
    #                 end_time = dt(int(year), int(month), int(day), int(hour), int(minute)).timestamp()
    #                 day, month, year, hour, minute = re.split('\s|/|:', start_date)
    #                 start_time = dt(int(year), int(month), int(day), int(hour), int(minute)).timestamp()
    #             except:
    #                 continue
    #             data_edge_lists.setdefault('bikeshare', []).append((start_station_id, end_station_id, int(start_time), int(end_time)))
    data_edge_lists['realitymining'] = load_from_txt('realitymining.edges', delimiter='\t', order=('u', 'v', 'begin', 'end'))
    print("realitymining")
    # data_edge_lists['wikipedia'] = load_from_txt('wikipedia.edges', delimiter=' ', order=('u', 'v', 'begin', 'end'))
    # print("wikipedia")
    # data_edge_lists['infectious'] = load_from_txt('infectious_merged.edges', delimiter='\t', order=('u', 'v', 'begin', 'end'))
    # print("infectious")
    # data_edge_lists['askubuntu'] = load_from_txt('askubuntu.edges', delimiter=' ', order=('u', 'v', 'timestamp'), impulse=True)
    # data_edge_lists['wallposts'] = load_from_txt('fb_wall.edges', delimiter='\t', order=('u', 'v', 'timestamp'), impulse=True)
    data_edge_lists['enron'] = load_from_txt('execs.email.lines2.txt', delimiter=' ', order=('timestamp', 'u', 'v'), impulse=True)
    print("loaded from text")

    ## GENERATE STRUCTURES
    # global creation_results
    creation_results = {}
    structures = {'interval': IntervalGraph(), 'snapshot': SnapshotGraph(), 'networkx': MultiGraph(), 'adjtree': AdjTree(), 'tvg': TVG()}
    with mp.Pool(10) as p:
        for creation_time, struct_name, dataset_name, G in tqdm.tqdm(p.starmap(generateStructures, product(structures.items(), data_edge_lists.items())), total=len(structures)*len(data_edge_lists)):
            creation_results.setdefault(struct_name, {})[dataset_name] = (G, creation_time)
            pickle.dump((G, creation_time), open(f'creation_results_{struct_name}_{dataset_name}.pkl', 'wb'))  # Comment out this line if you do not wish to save structures
    print("struct generated")
    # print('creation_results', creation_results)
    
    ## TRAIN INTERVALGRAPH
    # for dataset_name in creation_results['interval']:
    #     for t in [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]:
    #         G = creation_results['interval'][dataset_name][0]
    #         start_time = timer()
    #         attempts = G.generateModel(trainingSize=t)
    #         model_time = timer() - start_time
    #         print(dataset_name, creation_results['interval'][dataset_name][1], model_time, attempts)
    #         pickle.dump((None, creation_results['interval'][dataset_name][1], model_time, attempts), open(f'creation_results_interval_{dataset_name}_{t}.pkl', 'wb')) # Comment out this line if you do not wish to save structures
    # print("intervalgraph trained")

    ## GENERATE MEMORY
    memory_results = {}
    for struct_name in creation_results:
        for dataset_name in creation_results[struct_name]:
            mem = asizeof.asizeof(creation_results[struct_name][dataset_name][0])*1e-6
            memory_results.setdefault(struct_name, {})[dataset_name] = mem
            pickle.dump(memory_results[struct_name][dataset_name], open(f'memory_results_{struct_name}_{dataset_name}.pkl', 'wb'))  # Comment out this line if you do not wish to save results
    print("memory result aquired")
    print("preplot", structures, ["realitymining", "enron"] )

    import plot_figures as pf
    pf.plot_memory(structures, ["realitymining", "enron"])
    ## CALCULATE INTERVALGRAPH MODEL MEMORY
    # model_memory_results = {}
    # for dataset_name in creation_results['interval']:
    #     print(struct_name)
    #     mem = asizeof.asizeof(creation_results[struct_name][dataset_name][0].model) * 1e-6
    #     model_memory_results.setdefault(struct_name, {})[dataset_name] = mem
    #     pickle.dump(model_memory_results[struct_name][dataset_name], open(f'model_memory_results_{struct_name}_{dataset_name}.pkl', 'wb'))
    # print(model_memory_results)

    # GENERATE INTERVAL SLICES
    slice_results = {}
    for struct_name in creation_results:
        for dataset_name in creation_results[struct_name]:
            # print('struct_name', struct_name)
            # print('dataset_name', dataset_name)
            # print('creation_results', creation_results)
            with mp.Pool(10) as p:
                for one, five, ten, twenty in tqdm.tqdm(p.imap_unordered(generateSlices, [(struct_name, dataset_name, creation_results)]*50), total=50):
                    slice_results.setdefault(struct_name, {}).setdefault(dataset_name, {}).setdefault(1, []).append(one)
                    slice_results.setdefault(struct_name, {}).setdefault(dataset_name, {}).setdefault(5, []).append(five)
                    slice_results.setdefault(struct_name, {}).setdefault(dataset_name, {}).setdefault(10, []).append(ten)
                    slice_results.setdefault(struct_name, {}).setdefault(dataset_name, {}).setdefault(20, []).append(twenty)
                pickle.dump(slice_results[struct_name][dataset_name], open(f'slice_results_{struct_name}_{dataset_name}.pkl', 'wb'))  # Comment out this line if you do not wish to save results
    print("INTERVAL SLICES generated")

    ## GENERATE COMPOUND SLICES
    query_results = {}
    for struct_name in creation_results:
        for dataset_name in creation_results[struct_name]:
            with mp.Pool(10) as p:
                for result in tqdm.tqdm(p.imap_unordered(generateCompoundSlices, [(struct_name, dataset_name, creation_results)]*50), total=50):
                    query_results.setdefault(struct_name, {}).setdefault(dataset_name, []).append(result)
                pickle.dump(query_results[struct_name][dataset_name], open(f'compound_results_{struct_name}_{dataset_name}.pkl', 'wb'))  # Comment out this line if you do not wish to save results
    print("COMPOUND SLICES generated")

    ## Generating Samples
    structures = {'interval': IntervalGraph()}
    sample_data_edge_lists = {}
    sample_creation_results = {}
    for dataset_name in data_edge_lists:
        sample_data_edge_lists[dataset_name] = sample(data_edge_lists[dataset_name], int(len(data_edge_lists[dataset_name])*0.01))

    subsetCreateTime = {}
    with mp.Pool(10) as p:
        for creation_time, struct_name, dataset_name, G in tqdm.tqdm(p.starmap(generateStructures, product(structures.items(), sample_data_edge_lists.items())), total=len(structures)*len(sample_data_edge_lists)):
            sample_creation_results.setdefault(struct_name, {})[dataset_name] = (G, creation_time)

    pickle.dump((G, creation_time), open(f'sample_creation_results_{struct_name}_{dataset_name}.pkl', 'wb'))  # Comment out this line if you do not wish to save structures
    print("samples generated")

    # # # Create Bins
    global numEdges
    numEdges = {}
    for dataset_name in data_edge_lists:
        start_time = timer()
        G = sample_creation_results['interval'][dataset_name][0]

        begin, end = G.interval()

        bins = [(begin + i * (end - begin) / 100, begin + (i + 1) * (end - begin) / 100) for i in range(100)]
        for b, e in bins:
            results = [x for x in G.slice(b, e)]
            numEdges.setdefault(dataset_name, {})[(b, e)] = len(results)
        end_time = timer() - start_time
    print("bins generated")

    # GENERATE FEATURES (IntervalGraph Only!)
    print("Generating Features")
    feature_results = {}
    for dataset_name in query_results['interval']:
        with mp.Pool(10) as p:
            for features, times, results in tqdm.tqdm(p.starmap(generateFeatures, [(dataset_name, x) for x in query_results['interval'][dataset_name]]), total=5000):
                feature_results.setdefault(dataset_name, []).append((features, results, times))
        pickle.dump(feature_results[dataset_name],
                    open(f'feature_results_interval_{dataset_name}.pkl', 'wb'))  # Comment out this line if you do not wish to save results
    print("feats generated")

    ## LOG MODEL FEATURES (IntervalGraph Only!)
    score_results = {}
    for dataset_name in feature_results:
        X = [result[0][:2] for result in feature_results[dataset_name]]
        y = []
        for result in feature_results[dataset_name]:
            if result[1][0] <= result[1][1]:
                y.append(0)
            else:
                y.append(1)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.95)

        model = LogisticRegression(penalty='none', class_weight='balanced')
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        score_results[dataset_name] = {'Model': model,
                                       'RMSE': mean_squared_error(y_test, y_pred, squared=False),
                                       'R2 Score': r2_score(y_test, y_pred),
                                       'Accuracy': accuracy_score(y_test, y_pred),
                                       'Balanced Accuracy': balanced_accuracy_score(y_test, y_pred),
                                       'Coef': model.coef_,
                                       'Intercept': model.intercept_,
                                       'X_test': X_test,
                                       'Predictions': y_pred
                                       }

        pickle.dump(score_results[dataset_name], open(f'score_results_{dataset_name}_log.pkl', 'wb'))  # Comment out this line if you do not wish to save results



    # print("Generating Models")
    ## LIN MODEL FEATURES (IntervalGraph Only!)
    score_results = {}
    for dataset_name in feature_results:
        for percent in range(1, 11):
            trim_feats = range(4)
            X = [result[0] for result in feature_results[dataset_name]]
            y = [result[1] for result in feature_results[dataset_name]]

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=(1-percent/100), random_state=0)

            X_train_trim = [[x[i] for i in trim_feats] for x in X_train]
            X_test_trim = [[x[i] for i in trim_feats] for x in X_test]

            model = LinearRegression()
            model.fit(X_train_trim, y_train)
            y_pred = model.predict(X_test_trim)

            faster_y_pred = [0 if out[0] > out[1] else 1 for out in y_pred]
            faster_y_test = [0 if out[0] > out[1] else 1 for out in y_test]

            score_results[dataset_name] = {'Model': model,
                                           'RMSE': mean_squared_error(y_test, y_pred, squared=False),
                                           'R2 Score': r2_score(y_test, y_pred),
                                           'Accuracy': accuracy_score(faster_y_test, faster_y_pred),
                                           'Balanced Accuracy': balanced_accuracy_score(faster_y_test, faster_y_pred),
                                           'Coef': model.coef_,
                                           'Intercept': model.intercept_,
                                           'X_test': X_test,
                                           'Predictions': y_pred
                                           }

            pickle.dump(score_results[dataset_name], open(f'score_results_{dataset_name}_lin_{percent}_4.pkl', 'wb'))  # Comment out this line if you do not wish to save results

    ## GENERATE CASE STUDY
    result = generateCaseStudy()
    pickle.dump(result, open(f'case_study_results.pkl', 'wb'))
