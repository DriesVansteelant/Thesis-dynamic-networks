/* Copyright (C) 2022 Lutz Oettershagen - All Rights Reserved
 *
 * This file is part of TGLib which is released under MIT license.
 * See file LICENSE.md or go to https://gitlab.com/tgpublic/tglib
 * for full license details.
 */

 /** @file TemporalClusteringCoefficient.h
  *  @brief Contains function for computing the temporal clustering coefficient.
  */

#ifndef TGLIB_TEMPORALCLUSTERINGCOEFFICIENT_H
#define TGLIB_TEMPORALCLUSTERINGCOEFFICIENT_H

#include "../core/BasicTypes.h"
#include "../core/IncidentLists.h"
#include <iostream>
#include <thread>
#include <future>
#include <algorithm>

namespace tglib {

	/**
	 * @brief Computes the temporal clustering coefficient for one node
	 *
	 * The temporal clustering coefficient is defined as
	 * \f[
	 * C_C(u) = \frac{\sum_{t\in T(\mathcal{G})} \pi_t(u)}{|T(\mathcal{G})|{|N(u)| \choose 2}},
	 * \f]
	 * where \f$\pi_t(u)=|\{(v,w,t,\lambda)\in\mathcal{E}\mid v,w\in N(u)\}|\f$
	 * and \f$N(u)\f$ the neighbors of \f$u\f$ [1].
	 *
	 * [1] Tang, John, et al. "Temporal distance metrics for social network analysis."
	 * Proceedings of the 2nd ACM workshop on Online social networks. 2009.
	 *
	 * @tparam N Node type
	 * @param tg The temporal graph
	 * @param nid The node for which the temporal clustering coefficient is computed
	 * @param ti A restrictive time interval
	 * @return The temporal clustering coefficient for node with node id nid with respect to the time interval ti
	 */
	template<typename N, typename E>
	double temporal_clustering_coefficient(IncidentLists<N, E> const& tg, NodeId nid, TimeInterval ti) {

		std::set<NodeId> neighbors;
		for (auto& e : tg.getNode(nid).outEdges) {
			if (e.t < ti.first || e.t > ti.second) continue;
			neighbors.insert(e.v);
		}

		double count = 0;
		for (auto& v : neighbors) {
			for (auto& e : tg.getNode(v).outEdges) {
				if (neighbors.find(e.v) != neighbors.end()) {
					count += 1;
				}
			}
		}

		if (count == 0) return 0;

		auto timesteps = ti.second - ti.first;
		auto m = (double)(neighbors.size() * (neighbors.size() - 1));
		double result = (1.0 / (double)timesteps) * (count / m);

		return result;
	}


	/**
	 * @brief Computes the temporal clustering coefficient for all nodes
	 *
	 * The temporal clustering coefficient is defined as
	 * \f[
	 * C_C(u) = \frac{\sum_{t\in T(\mathcal{G})} \pi_t(u)}{|T(\mathcal{G})|{|N(u)| \choose 2}},
	 * \f]
	 * where \f$\pi_t(u)=|\{(v,w,t,\lambda)\in\mathcal{E}\mid v,w\in N(u)\}|\f$
	 * and \f$N(u)\f$ the neighbors of \f$u\f$ [1].
	 *
	 * [1] Tang, John, et al. "Temporal distance metrics for social network analysis."
	 * Proceedings of the 2nd ACM workshop on Online social networks. 2009.
	 *
	 * @tparam N Node type
	 * @param tg The temporal graph
	 * @param ti A restrictive time interval
	 * @return The temporal clustering coefficients for all nodes with respect to the time interval ti
	 */
	template<typename N, typename E>
	std::vector<double> temporal_clustering_coefficient(IncidentLists<N, E> const& tg, TimeInterval ti) {

		std::vector<double> result(tg.getNumberOfNodes(), 0);
		auto timesteps = ti.second - ti.first;

		for (size_t nid = 0; nid < tg.getNumberOfNodes(); ++nid) {
			std::set<NodeId> neighbors;

			for (auto& e : tg.getNode(nid).outEdges) {
				if (e.t < ti.first || e.t > ti.second) continue;
				neighbors.insert(e.v);
			}

			double count = 0;
			for (auto& v : neighbors) {
				for (auto& e : tg.getNode(v).outEdges) {
					if (e.t < ti.first || e.t > ti.second) continue;
					if (neighbors.find(e.v) != neighbors.end()) {
						count += 1;
					}
				}
			}

			if (neighbors.empty() || neighbors.size() == 1) {
				result[nid] = 0.0;
			}
			else {
				auto m = (double)(neighbors.size() * (neighbors.size() - 1));
				result[nid] = (1.0 / (double)timesteps) * (count / m);
			}
		}

		return result;
	}

	// =====================================================================================================================================================================

	template<typename N, typename E>
	std::vector<double> do_cc(IncidentLists<N, E> const& tg, TimeInterval ti, size_t startNid, size_t endNid) { //, std::vector<double> result) {
		std::chrono::time_point<std::chrono::system_clock> start, end;
		start = std::chrono::system_clock::now();

		std::vector<double> result(endNid - startNid, 0);
		auto timesteps = ti.second - ti.first;
		for (size_t nid = startNid; nid < endNid; ++nid) {
			std::set<NodeId> neighbors;

			for (auto& e : tg.getNode(nid).outEdges) {
				if (e.t < ti.first || e.t > ti.second) continue;
				neighbors.insert(e.v);
			}

			double count = 0;
			for (auto& v : neighbors) {
				for (auto& e : tg.getNode(v).outEdges) {
					if (e.t < ti.first || e.t > ti.second) continue;
					if (neighbors.find(e.v) != neighbors.end()) {
						count += 1;
					}
				}
			}

			if (neighbors.empty() || neighbors.size() == 1) {
				result[nid - startNid] = 0.0;
			}
			else {
				auto m = (double)(neighbors.size() * (neighbors.size() - 1));
				result[nid - startNid] = (1.0 / (double)timesteps) * (count / m);
			}
		}
		end = std::chrono::system_clock::now();
		std::chrono::duration<double> elapsed_seconds = end - start;
		std::cout << "Done at " << startNid << " in time " << elapsed_seconds.count() << ", size: " << result.size() << "\n";
		return result;
	}

	template<typename N, typename E>
	std::vector<double> temporal_clustering_coefficient_multi(IncidentLists<N, E> const& tg, TimeInterval ti) {
		auto numNodes = tg.getNumberOfNodes();
		std::vector<double> result;
		auto timesteps = ti.second - ti.first;
		auto numThreads = 4;
		long long incr = numNodes / numThreads;
		std::vector<std::future<std::vector<double>>> result_futures;

		for (size_t i = 0; i < numThreads; i++) {
			auto startNid = i * incr;
			auto endNid = 0;
			if (i == numThreads - 1) {
				endNid = numNodes;
			}
			else {
				endNid = startNid + incr;
			}
			std::cout << "total: " << numNodes << ", start: " << startNid << ", end: " << endNid << " at: " << std::chrono::system_clock::now() << "\n";
			result_futures.push_back(std::async(do_cc<N, E>, std::ref(tg), ti, startNid, endNid));
		}

		for (auto& res : result_futures) {
			auto temp = res.get();
			result.insert(result.end(), temp.begin(), temp.end());
		}
		return result;
	}

	// ==========================================================================================================================================================

	inline bool operator<(const TGNode& a, const TGNode& b)
	{
		return a.id < b.id;
	}

	inline bool operator==(const TGNode& a, const TGNode& b)
	{
		return a.id == b.id;
	}

	template<typename N, typename E>
	void count_edges(/*IncidentLists<N, E> const& tg,*/ std::vector<std::set<N>> neighborsVector, TimeInterval ti, NodeId startNid, NodeId endNid, std::vector<double> result) {
		for (size_t nid = startNid; nid < endNid; ++nid) {
			double count = 0;
			auto timesteps = ti.second - ti.first;
			auto neighbors = neighborsVector[nid];
			for (auto& v : neighbors) {
				for (auto& e : v.outEdges) {//tg.getNode(v).outEdges) {
					if (e.t < ti.first || e.t > ti.second) continue;
					if (neighbors.find(TGNode(e.v)) != neighbors.end()) {
						count += 1;
					}
				}
			}
			if (neighbors.empty() || neighbors.size() == 1) {
				result[nid] = 0.0;
			}
			else {
				auto m = (double)(neighbors.size() * (neighbors.size() - 1));
				result[nid] = (1.0 / (double)timesteps) * (count / m);
			}
		}
	}

	template<typename N, typename E>
	std::vector<double> temporal_clustering_coefficient_andere_multi(IncidentLists<N, E> const& tg, TimeInterval ti) {

		std::vector<double> result(tg.getNumberOfNodes(), 0);
		//auto timesteps = ti.second - ti.first;

		std::vector<std::set<TGNode>> neighborsVector;
		for (size_t nid = 0; nid < tg.getNumberOfNodes(); ++nid) {
			std::set<TGNode> neighbors;
			for (auto& e : tg.getNode(nid).outEdges) {
				if (e.t < ti.first || e.t > ti.second) continue;
				neighbors.insert(tg.getNode(e.v));
			}
			neighborsVector.push_back(neighbors);
		}

		/*for (size_t nid = 0; nid < tg.getNumberOfNodes(); ++nid) {
			auto neighbors = neighborsVector[nid];
			count_edges(tg, neighbors, ti, nid, result);

		}*/

		auto numThreads = 4;
		auto numNodes = tg.getNumberOfNodes();
		long long incr = numNodes / numThreads;

		std::vector<std::thread> threads;

		for (size_t i = 0; i < numThreads; i++) {
			auto startNid = i * incr;
			auto endNid = 0;
			if (i == numThreads - 1) {
				endNid = numNodes;
			}
			else {
				endNid = startNid + incr;
			}
			std::cout << "total: " << numNodes << ", start: " << startNid << ", end: " << endNid << " at: " << std::chrono::system_clock::now() << "\n";
			threads.push_back(std::thread(count_edges<N, E>, /*std::ref(tg),*/ neighborsVector, ti, startNid, endNid, result));
			//count_edges(tg, neighborsVector, ti, startNid, endNid, result);
		}
		for (auto& thr : threads) {
			thr.join();
		}

		return result;
	}

}

#endif //TGLIB_TEMPORALCLUSTERINGCOEFFICIENT_H
