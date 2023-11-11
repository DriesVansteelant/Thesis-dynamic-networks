import matplotlib.pylab as plt
import numpy as np
import pickle

def plot_result(structs, datasets):
    # details uit te vissen
    """
    STRUCTS: list of strings
    datasets: list of strings
    pickle loads dicts of {dataset: [vals]}?
    """
    print("start plot")
    memory_results = {}
    # print("structs", structs)
    # print("datasets",datasets)
    for struct in structs:
        for dataset_name in datasets:
            # print("inLoop: ", struct, dataset_name)
            memory_results.setdefault(struct, {})[dataset_name] = pickle.load(open(f'memory_results_{struct}_{dataset_name}.pkl', 'rb'))
    print("mem loaded")
    fig, ax = plt.subplots()
    width = 0.15
    offset = {'interval': 2 * width, 'snapshot': 1 * width, 'adjtree': 0 * width, 'tvg': -1 * width,'networkx': -2 * width}
    color = {'interval': (0.65, 0.3, 0.3), 'snapshot': (0, 0.75, 0), 'networkx': (0.8, 0.8, 0.8), 'adjtree': (0, 0, .75), 'tvg': (1, 1, 0)}
    labels = {'interval': 'IntervalGraph', 'snapshot': 'SnapshotGraph', 'networkx': 'NetworkX', 'adjtree': 'AdjTree', 'tvg': 'TVG'}
    label_location = np.arange(len(datasets))

    for struct in structs:
        nums = [memory_results[struct][d] for d in memory_results[struct]]
        ax.bar(label_location + offset[struct], nums, width, label=labels[struct], color=color[struct])

    # ax.set_title('Memory')
    ax.set_xticks(label_location)
    ax.set_xticklabels(datasets)
    ax.set_yscale('log')
    ax.set_ylabel('Memory (MB)')
    fig.tight_layout()
    fig.set_figheight(4)
    fig.set_figwidth(6)
    plt.tight_layout(pad=0.2)
    plt.legend()
    fig.savefig('memory.eps', format='eps')
    plt.show()
    print("done!")