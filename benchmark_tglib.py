import tglib.tglib_cpp.build.src.python_binding.Release.pytglib as tgl  # tglib
import scipy.stats as ss  # for Kendall's tau correlation
from tqdm import tqdm
import time
import numpy as np
import random


class testname():
    def do_benchmark(inPath, pathsSize, do_paths = True):
        results = {}
        
# Load Graph
        start = time.time()
        directed = True
        g = tgl.load_ordered_edge_list(inPath, directed)
        end = time.time()

        print(f"Time taken to read graph {end-start} seconds")
        results["loadTime"] = end-start

# Get statistcs
        start = time.time()
        stats = tgl.get_statistics(g)
        end = time.time()

        results["stats"] = end-start
        print(f"Time taken to get stats {end-start} seconds \n")
        print(stats)


        start = time.time()
        stats2 = tgl.get_node_statistics(g)
        results["stats"] = end-start
        print(f"Time taken to get node stats {end-start} seconds \n")
        # print(stats2)

# Paths
        incidents = tgl.to_incident_lists(g)

        # from_nodes = [2265, 2265, 2267, 7560, 7241, 2186, 2176, 2174, 2164, 2157, 1723, 1716]
        # to_nodes =   [980, 973, 992, 341, 993, 979, 988, 948, 995, 981, 271, 995]
        # paths = []

        # if do_paths:
        #     start = time.time()
        #     for fro in tqdm(from_nodes):
        #         for to in (to_nodes):
        #             temp = tgl.minimum_transition_time_path(incidents, fro, to, g.getTimeInterval())
        #             paths.append(temp)
        #     end = time.time()
        #     results["paths"] = end-start
        #     print(f"Time taken to get shortest paths {end-start} seconds")
        

# clustering coefficient
        
        start = time.time()

        tgl.temporal_clustering_coefficient(incidents, g.getTimeInterval())

        end = time.time()
        results["clusteringCoefficient"] = end-start
        print(f"Time to get clustering coefficient: {end - start}")
# Pagerank
        start = time.time()

        pr = tgl.temporal_pagerank(g, 1.0,1.0,1.0)

        end = time.time()
        results["pagerank"] = end-start
        print(f"Time to get Pagerank: {end - start}")


# Traingles and triplets

        # print("==================================================================================")
        # print(np.random.choice(paths, size=20))
        return results
    
    do_benchmark("../Code/Data/tgbl-wiki_edgelist_final.txt", 10, do_paths = True)

# VectorTemporalEdge[(2265 660 457519 1), (660 678 632686 1), (678 337 756363 1), (337 233 811793 1), (233 717 1663063 1), (717 980 2433174 1)]
# VectorTemporalEdge[(2265 660 457519 1), (660 678 632686 1), (678 337 756363 1), (337 233 811793 1), (233 17 1839174 1), (17 367 1942183 1), (367 973 2108004 1)]
# VectorTemporalEdge[(2267 324 459909 1), (324 184 828483 1), (184 418 915629 1), (418 727 930819 1), (727 373 1061539 1), (373 281 1272833 1), (281 68 1382669 1), (68 992 2532796 1)]
# VectorTemporalEdge[(7560 537 2308992 1), (537 68 2365526 1), (68 385 2483394 1), (385 346 2502526 1), (346 388 2526904 1), (388 255 2566269 1), (255 341 2607278 1)]
# VectorTemporalEdge[(7241 571 2176221 1), (571 220 2179953 1), (220 281 2213710 1), (281 68 2277266 1), (68 385 2483394 1), (385 346 2502526 1), (346 537 2530865 1), (537 993 2668126 1)]
# VectorTemporalEdge[(2186 66 430540 1), (66 281 974358 1), (281 68 1382669 1), (68 347 1666461 1), (347 40 1696726 1), (40 898 1755451 1), (898 509 1924527 1), (509 979 2653911 1)]
# VectorTemporalEdge[(2176 456 1387924 1), (456 445 1541063 1), (445 205 1623411 1), (205 71 1632211 1), (71 608 1796575 1), (608 39 2427238 1), (39 623 2553226 1), (623 988 2642124 1)]
# VectorTemporalEdge[(2174 47 427620 1), (47 44 578920 1), (44 42 1015647 1), (42 40 1378303 1), (40 22 1672011 1), (22 476 1903552 1), (476 292 1962330 1), (292 624 2010162 1), (624 344 2123116 1), (344 233 2197719 1), (233 948 2268146 1)]
# VectorTemporalEdge[(2164 119 425613 1), (119 184 595040 1), (184 418 915629 1), (418 727 930819 1), (727 78 1181246 1), (78 18 1190218 1), (18 17 1210506 1), (17 16 1290879 1), (16 22 1291466 1), (22 292 1344888 1), (292 624 1508561 1), (624 344 1511774 1), (344 233 1675459 1), (233 995 2447750 1)]
# VectorTemporalEdge[(2157 150 424055 1), (150 88 439799 1), (88 76 553926 1), (76 502 570221 1), (502 249 793503 1), (249 242 823670 1), (242 184 904858 1), (184 418 915629 1), (418 727 930819 1), (727 373 1061539 1), (373 281 1272833 1), (281 68 1382669 1), (68 417 1750109 1), (417 285 1982289 1), (285 981 2196583 1)]
# VectorTemporalEdge[(1723 364 562961 1), (364 310 588273 1), (310 17 759263 1), (17 68 774571 1), (68 233 983398 1), (233 51 1060973 1), (51 109 1076873 1), (109 506 1325170 1), (506 443 1697182 1), (443 271 2224560 1)]
# VectorTemporalEdge[(1716 242 678327 1), (242 184 758769 1), (184 418 915629 1), (418 727 930819 1), (727 78 1181246 1), (78 18 1190218 1), (18 17 1210506 1), (17 16 1290879 1), (16 22 1291466 1), (22 292 1344888 1), (292 624 1508561 1), (624 344 1511774 1), (344 233 1675459 1), (233 995 2447750 1)]


