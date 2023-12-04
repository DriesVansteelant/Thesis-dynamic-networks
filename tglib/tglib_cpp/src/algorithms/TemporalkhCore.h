/* Copyright (C) 2022 Lutz Oettershagen - All Rights Reserved
 *
 * This file is part of TGLib which is released under MIT license.
 * See file LICENSE.md or go to https://gitlab.com/tgpublic/tglib
 * for full license details.
 */

/** @file TemporalkhCore.h
 *  @brief Contains function for computing the temporal (k,h)-cores.
 */
#ifndef TGLIB_TEMPORALKHCORE_H
#define TGLIB_TEMPORALKHCORE_H

#include <vector>
#include <map>
#include <set>
#include "../core/AggregatedGraph.h"
#include "../core/OrderedEdgeList.h"
#include "../core/Transformations.h"

namespace tglib {


/**
 * Computes the k-core values for all nodes.
 * @param edges The aggregated graph as edge list.
 * @return Vector of core numbers.
 */
std::vector<int> compute_kcores(std::vector<StaticWeightedEdge> const &edges) {
    std::map<int, std::vector<StaticWeightedEdge>> g;

    NodeId mxnid = 0;
    for (auto &e : edges) {
        g[e.u].push_back(e); // todo assumption graph is undirected
        if (e.u > mxnid) mxnid = e.u;
        if (e.v > mxnid) mxnid = e.v;
    }

    std::set<std::pair<int, NodeId>, std::less<>> degrees;
    std::vector<int> c(mxnid+1, 0);
//    std::vector<uint> c(g.size(), 0);
    for (auto &p : g) {
        degrees.insert({p.second.size(), p.first});
        c[p.first] = p.second.size();
    }

    std::vector<bool> removed(mxnid+1, false);

    while (!degrees.empty() ) {

        // get next node
        auto next = degrees.begin();
        auto u = next->second;
        degrees.erase(next);

        if (removed[u]) continue;
        removed[u] = true;

        for (auto &e : g[u]) {
            if (removed[e.v]) continue;
            if (c[e.v] > c[e.u]) {
                --c[e.v];
                degrees.insert({c[e.v], e.v});
            }
        }
    }

    return c;
}


/**
 * The computes the (k,h)-core numbers as defined in:
 *
 * Wu, Huanhuan, et al. "Core decomposition in large temporal graphs." 2015 IEEE International Conference on Big Data (Big Data). IEEE, 2015.
 *
 * @tparam E Temporal edge type
 * @param tgs Ordered edge list
 * @param h Paramter h
 * @return The (k,h)-core numbers.
 */
template<typename E>
std::vector<int> compute_khcores(OrderedEdgeList<E> const &tgs, int h) {
    auto g = to_aggregated_edge_list<E>(tgs);
    std::vector<StaticWeightedEdge> edges;
    for (auto &e : g) {
        if (e.weight >= h) {
            edges.push_back(e);
        }
    }
    return compute_kcores(edges);
}

}

#endif //TGLIB_TEMPORALKHCORE_H
