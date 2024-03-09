import numpy as np

CanParl = {
    "clustering_coefficient": {
        "temporal_clustering_coefficient": {
            "set_end": 0.548,
            "set_find": 2.063,
            "set_insert": 0.016,
            "set_op_equals": 0.079,
            "set_const_iterator": 0.804,
            "set_alloc": 0.016,
            "set_alloc": 0.016,
            "set": 0,
        },
        "to_incident_lists": 0.016,
    },
    "load_time": {
        "load_ordered_edge_list": {
            "basic_ifstream": 0.015,
            "std_get_inline": 0.119,
            "sort": 0.688,
            "vector_alloc": 0.03,
            "vector_pushback": 0.031,
            "getNodeId": 0.108,
            "splitString": 0.741,
        }
    },
    "degree_list": {
        "get_degrees": {
            "eh vector destructor iterator": 0,
            "set_insert": 0,
            "basic_string": 0,
            "map_alloc": 0,
            "map_op_get": 0,
            "map_op_get": 0.047,
            "pair_alloc": 0.016,
            "sort": 0.341,
            "vector_push_back": 0.016,
        }
    },
    "get_stats": {
        "get_statistics": {
            "hash_insert": 0.079,
            "set_insert": 0.158,
            "set_alloc": 0.016,
            "pair_alloc": 0,
            "pair_alloc2": 0,
            "pair": 0,
            "unordered_set": 0,
        }
    },
    "pageRank": {-1},
}


# =======================================================

Flights = {
    "clustering_coefficient": {
        "temporal_clustering_coefficient": {
            "set_end": 32.36,
            "set_find": 131.265,
            "set_insert": 1.193,
            "set_op_equals": 5.294,
            "set_const_iterator": 53.015,
            "set_alloc": 0,
            "set_alloc": 0,
            "set": 0,
        },
        "to_incident_lists": 0,
    },
    "load_time": {
        "load_ordered_edge_list": {
            "basic_ifstream": 0,
            "std_get_inline": 3.329,
            "sort": 21.239,
            "vector_alloc": 0.78,
            "vector_pushback": 0.612,
            "getNodeId": 2.231,
            "splitString": 18.379,
        }
    },
    "degree_list": {
        "get_degrees": {
            "eh vector destructor iterator": 0,
            "set_insert": 0.47,
            "basic_string": 0.032,
            "map_alloc": 0.032,
            "map_op_get": 0.031,
            "map_op_get": 1.631,
            "pair_alloc": 0.031,
            "sort": 4.924,
            "vector_push_back": 0.0,
        }
    },
    "get_stats": {
        "get_statistics": {
            "hash_insert": 1.264,
            "set_insert": 4.49,
            "pair_alloc": 0.186,
            "pair_alloc2": 0.141,
            "set_alloc": 0.087,
            "pair": 0,
            "unordered_set": 0,
        }
    },
    "pageRank": {
        "temporal_page_rank": {
            "vector_op_get": 0.063,
            "vector_at": 0.015,
        }
    },
}

# =======================================================

SocialEvo = {
    "clustering_coefficient": {
        "temporal_clustering_coefficient": {
            "set_end": 10.082,
            "set_find": 37.551,
            "set_insert": 0.891,
            "set_op_equals": 1.156,
            "set_const_iterator": 15.401,
            "set_alloc": 0,
            "set_alloc": 0,
            "set": 0,
        },
        "to_incident_lists": 0.393,
    },
    "load_time": {
        "load_ordered_edge_list": {
            "basic_ifstream": 0,
            "std_get_inline": 3.871,
            "sort": 14.183,
            "vector_alloc": 0.899,
            "vector_pushback": 0.451,
            "getNodeId": 1.87,
            "splitString": 20.333,
        }
    },
    "degree_list": {
        "get_degrees": {
            "eh_vector_destructor_iterator": 0,
            "set_insert": 0,
            "basic_string": 0,
            "map_alloc": 0,
            "map_op_get": 0.932,
            "map_op_get": 0,
            "pair_alloc": 0,
            "sort": 0.031,
            "vector_pushback": 0,
        }
    },
    "get_stats": {
        "get_statistics": {
            "hash_insert": 2.22,
            "set_insert": 3.146,
            "pair_alloc": 0.281,
            "pair_alloc2": 0.047,
            "pair": 0.15,
            "unordered_set": 0,
            "set_alloc": 0.155,
        }
    },
    "pageRank": {"temporal_page_rank": {"vector_op_get": 0.047, "vector_at": 0}},
}

# =======================================================

enron = {
    "clustering_coefficient": {
        "temporal_clustering_coefficient": {
            "set_end": 0.267,
            "set_find": 0.732,
            "set_insert": 0.063,
            "set_op_equals": 0.016,
            "set_const_iterator": 0.356,
            "set_alloc": 0,
            "set_alloc": 0,
            "set": 0,
        },
        "to_incident_lists": 0.031,
    },
    "load_time": {
        "load_ordered_edge_list": {
            "basic_ifstream": 0,
            "std_get_inline": 0.264,
            "sort": 0.671,
            "vector_alloc": 0.062,
            "vector_pushback": 0.047,
            "getNodeId": 0.078,
            "splitString": 1.211,
        }
    },
    "degree_list": {
        "get_degrees": {
            "eh_vector_destructor_iterator": 0,
            "set_insert": 0,
            "basic_string": 0,
            "map_alloc": 0,
            "map_op_get": 0.062,
            "map_op_get": 0,
            "pair_alloc": 0,
            "sort": 0.094,
            "vector_pushback": 0,
        }
    },
    "get_stats": {
        "get_statistics": {
            "hash_insert": 0.095,
            "set_insert": 0.157,
            "pair_alloc": 0.047,
            "pair_alloc2": 0,
            "pair": 0,
            "unordered_set": 0,
            "set_alloc": 0,
        }
    },
    "pageRank": {"temporal_page_rank" "vector_op_get": 0, "vector_at": 0},
}
# ========================================================

lastfm = {
    "clustering_coefficient": {
        "temporal_clustering_coefficient": {
            "set_end": 0,
            "set_find": 0,
            "set_insert": 0.751,
            "set_op_equals": 0,
            "set_const_iterator": 0,
            "set_alloc": 0.032,
            "set_alloc": 0,
            "set": 0.063,
        },
        "to_incident_lists": 0.234,
    },
    "load_time": {
        "load_ordered_edge_list": {
            "basic_ifstream": 0.007,
            "std_get_inline": 2.635,
            "sort": 7.928,
            "vector_alloc": 0.607,
            "vector_pushback": 0.204,
            "getNodeId": 1.441,
            "splitString": 13.064,
        }
    },
    "degree_list": {
        "get_degrees": {
            "eh_vector_destructor_iterator": 0,
            "set_insert": 0,
            "basic_string": 0.016,
            "map_alloc": 0,
            "map_op_get": 0.988,
            "map_op_get": 0.015,
            "pair_alloc": 0,
            "sort": 0.656,
            "eh_vector_destructor_iterator": 0.016,
            "vector_pushback": 0.032,
        }
    },
    "get_stats": {
        "get_statistics": {
            "hash_insert": 2.57,
            "set_insert": 2.755,
            "pair_alloc": 0.141,
            "pair_alloc2": 0.047,
            "pair": 0.016,
            "set_alloc": 0.047,
            "unordered_set": 0.392,
        }
    },
    "pageRank": {"temporal_page_rank": {"vector_op_get": 0.016, "vector_at": 0}},
}
# ========================================================

reddit = {
    "clustering_coefficient": {
        "temporal_clustering_coefficient": {
            "set_end": 0,
            "set_find": 0,
            "set_insert": 0.28,
            "set_op_equals": 0,
            "set_const_iterator": 0,
            "set_alloc": 0.016,
            "set_alloc": 0,
            "set": 0.063,
        },
        "to_incident_lists": 0.252,
    },
    "load_time": {
        "load_ordered_edge_list": {
            "basic_ifstream": 0,
            "std_get_inline": 1.398,
            "sort": 3.895,
            "vector_alloc": 0.299,
            "vector_pushback": 0.204,
            "getNodeId": 0.887,
            "splitString": 6.805,
        }
    },
    "degree_list": {
        "get_degrees": {
            "eh_vector_destructor_iterator": 0.016,
            "set_insert": 0.031,
            "basic_string": 0.062,
            "map_alloc": 0.016,
            "map_op_get": 0.016,
            "map_op_get": 0.596,
            "pair_alloc": 0.016,
            "sort": 2.369,
            "vector_pushback": 0.158,
        }
    },
    "get_stats": {
        "get_statistics": {
            "hash_insert": 1.274,
            "set_insert": 1.249,
            "pair_alloc": 0.031,
            "pair_alloc2": 0.016,
            "pair": 0,
            "set_alloc": 0.03,
            "unordered_set": 0.157,
        }
    },
    "pageRank": {"temporal_page_rank	" "vector_op_get": 0.016, "vector_at": 0},
}

# ========================================================

tgblReview = {
    "clustering_coefficient": {
        "temporal_clustering_coefficient": {
            "set_end": 20.395,
            "set_find": 62.917,
            "set_insert": 4.359,
            "set_op_equals": 2.991,
            "set_const_iterator": 34.868,
            "set_alloc": 0.675,
            "set_alloc": 0,
            "set": 1.443,
        },
        "to_incident_lists": 4.262,
    },
    "load_time": {
        "load_ordered_edge_list": {
            "basic_ifstream": 0,
            "std_get_inline": 11.748,
            "sort": 51.97,
            "vector_alloc": 2.066,
            "vector_pushback": 1.387,
            "getNodeId": 6.371,
            "splitString": 51.504,
        }
    },
    "degree_list": {
        "get_degrees": {
            "eh_vector_destructor_iterator": 0.232,
            "set_insert": 1.402,
            "basic_string": 0.618,
            "basic_string": 0.452,
            "map_alloc": 1.59,
            "map_op_get": 0.426,
            "map_op_get": 9.073,
            "pair_alloc": 0,
            "sort": 72.522,
            "vector_pushback": 5.687,
        }
    },
    "get_stats": {
        "get_statistics": {
            "hash_insert": 3.158,
            "set_insert": 16.099,
            "pair_alloc": 0.698,
            "pair_alloc2": 0.281,
            "pair": 0,
            "set_alloc": 1.67,
            "unordered_set": 0,
        }
    },
    "pageRank": {"temporal_page_rank": {"vector_op_get": 0.016, "vector_at": 0}},
}

# ========================================================

wikipedia = {
    "clustering_coefficient": {
        "temporal_clustering_coefficient": {
            "set_end": 0,
            "set_find": 0,
            "set_insert": 0.092,
            "set_op_equals": 0,
            "set_const_iterator": 0,
            "set_alloc": 0,
            "set_alloc": 0,
            "set": 0.016,
        },
        "to_incident_lists": 4.262,
    },
    "load_time": {
        "load_ordered_edge_list": {
            "basic_ifstream": 0,
            "std_get_inline": 0.327,
            "sort": 0.778,
            "vector_alloc": 0.11,
            "vector_pushback": 0.016,
            "getNodeId": 0.155,
            "splitString": 1.562,
        }
    },
    "degree_list": {
        "get_degrees": {
            "eh_vector_destructor_iterator": 0,
            "set_insert": 0,
            "basic_string": 0.031,
            "basic_string": 0,
            "map_alloc": 0.03,
            "map_op_get": 0.016,
            "map_op_get": 0,
            "pair_alloc": 0.016,
            "sort": 1.44,
            "vector_pushback": 0.156,
        }
    },
    "get_stats": {
        "get_statistics": {
            "hash_insert": 0.187,
            "set_insert": 0.297,
            "pair_alloc": 0.031,
            "pair_alloc2": 0.031,
            "pair": 0,
            "set_alloc": 0,
            "unordered_set": 0.031,
        }
    },
    "pageRank": {"temporal_page_rank": {"vector_op_get": 0.016, 
                                        "vector_at": 0
                                        }},
}


UNVote = {
    "clustering_coefficient": {
        "temporal_clustering_coefficient": {
            "set_end": 11.507,
            "set_find": 49.098,
            "set_insert": 0.663,
            "set_op_equals": 1.873,
            "set_const_iterator": 19.496,
            "set_alloc": 0,
            "set_alloc": 0,
            "set": 0.232,
        },
        "to_incident_lists": 0.393,
    },
    "load_time": {
        "load_ordered_edge_list": {
            "basic_ifstream":     0,
            "std_get_inline": 2.039,
            "sort": 11.343,
            "vector_alloc": 0.528,
            "vector_pushback": 0.187,
            "getNodeId": 0.981,
            "splitString": 10.236,
        }
    },
    "degree_list": {
        "get_degrees": {
            "eh_vector_destructor_iterator": 0,
            "set_insert": 0,
            "basic_string": 0,
            "map_alloc": 0.016,
            "map_op_get": 0.528,
            "map_op_get": 0,
            "pair_alloc": 0,
            "sort": 0.093,
            "vector_pushback": 0,
        }
    },
    "get_stats": {
        "get_statistics": {
            "hash_insert": 0.627,
            "set_insert": 1.821,
            "pair_alloc": 0.125,
            "pair_alloc2": 0.095,
            "pair": 0.032,
            "set_alloc": 0,
            "unordered_set": 0
        }
    },
    "pageRank": {"temporal_page_rank": {
        "vector_op_get": 0.047,
        "vector_at": 0
        }},
}

allData = {
    "CanParl": CanParl,
    "Flights": Flights,
    "SocialEvo": SocialEvo,
    "enron": enron,
    "lastfm": lastfm,
    "reddit": reddit,
    "tgblReview": tgblReview,
    "wikipedia":wikipedia,
    "UNVote":UNVote
}

num_nodes = {'CanParl': '10^3',
 'Flights': '10^4',
 'SocialEvo': '100',
 'UNVote': '100',
 'enron': '100',
 'lastfm': '10^3',
 'reddit': '10^4',
 'tgblReview': '10^5',
 'wikipedia': '10^5'}

num_edges = {'CanParl': '10^5',
 'Flights': '10^5',
 'SocialEvo': '10^3',
 'UNVote': '10^5',
 'enron': '10^3',
 'lastfm': '10^5',
 'reddit': '10^5',
 'tgblReview': '10^6',
 'wikipedia': '10^5'}

num_interactions = {'CanParl': '10^5',
 'Flights': '10^6',
 'SocialEvo': '10^6',
 'UNVote': '10^6',
 'enron': '10^5',
 'lastfm': '10^6',
 'reddit': '10^5',
 'tgblReview': '10^6',
 'wikipedia': '10^5'}

'10⁰ ¹²³⁴⁵⁶⁷⁸⁹'

def sum_of_dict(x):
    return np.sum(list(x[1].values()))
def sum_list(x):
    return np.sum(x[1])
datasets = ['enron', 'SocialEvo', 'wikipedia', 'UNVote', 'CanParl', 'reddit', 'lastfm', 'Flights', 'tgblReview']

# get stats data from allData
stats = {}
for dataset in allData:
    stats[dataset] = allData[dataset]["get_stats"]["get_statistics"]
# get list of function names
funcs = list(stats['CanParl'].keys())
# sort by total run time
stats_sorted = dict((sorted(stats.items(), key=sum_of_dict)) )
# stats_datasets = list(stats_sorted.keys())
some_stats_datasets = ['CanParl', 'enron', 'reddit', 'lastfm', 'SocialEvo', 'Flights',]


# get total runtime
stats_total = {}
for ds in datasets:
    stats_total[ds] = np.sum(list(stats_sorted[ds].values()))

# make plottable dict {'functionName': [values]}
stats_plot = {}
stats_relative_plot = {}
for func in funcs:
    stats_plot[func] = []
    stats_relative_plot[func] = []
    for ds in datasets:
        stats_plot[func].append(stats_sorted[ds][func])
        stats_relative_plot[func].append(stats_sorted[ds][func]/stats_total[ds])
stats_plot_sorted = dict((sorted(stats_plot.items(), key=sum_list, reverse=True)) )

some_stats_plot = {}
for func in funcs:
    some_stats_plot[func] = []
    for ds in some_stats_datasets:
        some_stats_plot[func].append(stats_sorted[ds][func])
some_stats_plot_sorted = dict((sorted(some_stats_plot.items(), key=sum_list, reverse=True)) )


# get cc data from allData
clustering_coefficients = {}
for dataset in allData:
    clustering_coefficients[dataset] = allData[dataset]["clustering_coefficient"]["temporal_clustering_coefficient"]

# get list of function names
funcs = list(clustering_coefficients['CanParl'].keys())

# sort by total run time
clustering_coefficients_sorted = dict((sorted(clustering_coefficients.items(), key=sum_of_dict)) )
  # list(clustering_coefficients_sorted.keys())
some_cc_datasets = ['enron', 'wikipedia', 'CanParl', 'reddit', 'lastfm', ] #['reddit', 'lastfm', 'enron', 'CanParl']


# get total runtime
cc_total = {}
for ds in datasets:
    cc_total[ds] = np.sum(list(clustering_coefficients_sorted[ds].values()))


# make plottable dict {'functionName': [values]}
cc_plot = {}
cc_relative_plot = {}
for func in funcs:
    cc_plot[func] = []
    cc_relative_plot[func] = []
    for ds in datasets:
        cc_plot[func].append(clustering_coefficients_sorted[ds][func])
        cc_relative_plot[func].append(clustering_coefficients_sorted[ds][func]/cc_total[ds])
cc_plot_sorted = dict((sorted(cc_plot.items(), key=sum_list, reverse=True)) )
# print(cc_relative_plot)
# print(cc_plot)

some_cc_plot = {}
for func in funcs:
    some_cc_plot[func] = []
    for ds in some_cc_datasets:
        some_cc_plot[func].append(clustering_coefficients_sorted[ds][func])
some_cc_plot_sorted = dict((sorted(some_cc_plot.items(), key=sum_list, reverse=True)) )







# print("==========================================")
# print(some_cc_plot_sorted)

# print ( clustering_coefficients_sorted) 
# print(datasets)

# print(cc_plot)



# print(cc_plot_sorted)