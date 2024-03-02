#imports
from math import sqrt
import matplotlib.pylab as plt
import numpy as np
import pprint

class BasicPlots:
    def plot_basic(results, datasets, structs, title):
        fig, ax = plt.subplots()
        width = 0.5
        offset = {structs[0]: 0}#,  structs[1]: 0.5*width} 
        color = {structs[0]: (0.65, 0.3, 0.3)}#, structs[1]: (0.8, 0.8, 0.8)}  
        labels = {structs[0]: structs[0]}#, structs[1]:structs[1]} 
        label_location = np.arange(len(datasets))

        for struct in structs:
            nums = [results[struct][d] for d in results[struct]]
            ax.bar(label_location + offset[struct], nums, width, label=labels[struct], color=color[struct])

        ax.set_title(title)
        ax.set_xticks(label_location)
        ax.set_xticklabels(datasets)
        ax.set_yscale('log')
        ax.set_ylabel('#')
        fig.tight_layout()
        fig.set_figheight(6)
        fig.set_figwidth(9)
        plt.tight_layout(pad=0.2)
        plt.legend()
        fig.savefig('plots/' + title+'.png', format='png')
        plt.show()

    def plot_basic_2(results, datasets, structs, title):
        fig, ax = plt.subplots()
        width = 0.15
        offset = {structs[0]: -0.5*width,  structs[1]: 0.5*width} 
        color = {structs[0]: (0.65, 0.3, 0.3), structs[1]: (0.8, 0.8, 0.8)}  
        labels = {structs[0]: structs[0], structs[1]:structs[1]} 
        label_location = np.arange(len(datasets))

        for struct in structs:
            nums = [results[struct][d] for d in results[struct]]
            ax.bar(label_location + offset[struct], nums, width, label=labels[struct], color=color[struct])

        ax.set_title(title)
        ax.set_xticks(label_location)
        ax.set_xticklabels(datasets)
        ax.set_yscale('log')
        ax.set_ylabel('#')
        fig.tight_layout()
        fig.set_figheight(6)
        fig.set_figwidth(9)
        plt.tight_layout(pad=0.2)
        plt.legend()
        fig.savefig('plots/' + title+'.png', format='png')
        plt.show()

    def plot_basic_3(results, datasets, structs, title):
        fig, ax = plt.subplots()
        width = 0.15
        offset = {structs[0]: -width, structs[1]: 0, structs[2]: width}
        color = {structs[0]: (0.65, 0.3, 0.3), structs[1]: (0, 0.75, 0), structs[2]: (0.8, 0.8, 0.8)} 
        labels = {structs[0]: structs[0], structs[1]: structs[1], structs[2]:structs[2]}
        label_location = np.arange(len(datasets))

        for struct in structs:
            nums = [results[struct][d] for d in results[struct]]
            ax.bar(label_location + offset[struct], nums, width, label=labels[struct], color=color[struct])

        ax.set_title(title)
        ax.set_xticks(label_location)
        ax.set_xticklabels(datasets)
        ax.set_yscale('log')
        ax.set_ylabel('Time (s)')
        fig.tight_layout()
        fig.set_figheight(6)
        fig.set_figwidth(9)
        plt.tight_layout(pad=0.2)
        plt.legend()
        fig.savefig('plots/' + title+'.png', format='png')
        plt.show()

    def plot_per_quant(results, quant, datasets, structs, title, show_data_sets = True, times_density = False, density = []):

        fig, ax = plt.subplots()

        color = {'dynetx': '#2ca02c', 'tglib': '#1f77b4', 'raphtory': '#ff7f0e'}

        sorted_quant = sorted(quant.items(), key=lambda x: x[1])
        # print(sorted_quant)
        for struct in structs:
            if(times_density): ys = [density[d[0]] * results[struct][d[0]] for d in sorted_quant]
            else: ys = [results[struct][d[0]] for d in sorted_quant]
            # print(struct )
            # print(ys)
            xs = [x[1] for x in sorted_quant]
            # print(xs)
            # print(ys)
            plt.plot(xs, ys, label = struct, color=color[struct])
            plt.scatter(xs,ys, color=color[struct])
        
        # print(quant)
        # print(sorted_quant)
        if(show_data_sets):
            for i, txt in enumerate([d[0] for d in sorted_quant]):
                ax.annotate(txt, (xs[i], ys[i]))

        # pprint.pprint(sorted_quant)

        ax.set_title(title)
        ax.set_xscale('log')
        ax.set_yscale('log')
        ax.set_ylabel('Time (s)')
        fig.set_figheight(6)
        fig.set_figwidth(9)
        plt.legend()
        fig.savefig('plots/' + title + '.png', format='png')
        plt.show()

from vtune import allData, cc_plot, cc_plot_sorted, cc_datasets, some_cc_datasets, some_cc_plot_sorted, stats_datasets, stats_plot_sorted, some_stats_plot_sorted, some_stats_datasets,cc_relative_plot

class VtunePlots:
    def vtune_plot_clusteringCoefficient(all = True, rel=False):
        if(all and not rel):
            sets = cc_datasets
            plot = cc_plot_sorted
        elif(not all and not rel):
            sets = some_cc_datasets
            plot = some_cc_plot_sorted
        elif(all and rel):
            sets = cc_datasets
            plot = cc_relative_plot


        width = 0.5

        fig, ax = plt.subplots()
        bottom = np.zeros(len(sets))

        for boolean, weight_count in plot.items():
            p = ax.bar(sets, weight_count, width, label=boolean, bottom=bottom)
            bottom += weight_count

        ax.set_title("clustering coefficient")
        ax.legend()
        plt.xticks(rotation=45)
        # ax.set_yscale('log')

        plt.show()
        
    def vtune_plot_stats(all=True):
        if(all):
            sets = stats_datasets
            plot = stats_plot_sorted
        else:
            sets = some_stats_datasets
            plot = some_stats_plot_sorted

        width = 0.5

        fig, ax = plt.subplots()
        bottom = np.zeros(len(sets))

        for boolean, weight_count in plot.items():
            p = ax.bar(sets, weight_count, width, label=boolean, bottom=bottom)
            bottom += weight_count

        ax.set_title("get statistics")
        ax.legend()
        plt.xticks(rotation=45)
        # ax.set_yscale('log')

        plt.show()

VtunePlots.vtune_plot_clusteringCoefficient(True, True)
# VtunePlots.vtune_plot_stats()