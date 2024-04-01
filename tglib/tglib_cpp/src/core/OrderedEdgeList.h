/* Copyright (C) 2022 Lutz Oettershagen - All Rights Reserved
 *
 * This file is part of TGLib which is released under MIT license.
 * See file LICENSE.md or go to https://gitlab.com/tgpublic/tglib
 * for full license details.
 */

 /** @file OrderedEdgeList.h
  *  @brief Contains the ordered edge list representation data structure for temporal graphs
  */

#ifndef CPP_TEMPORALGRAPHSTREAM_H
#define CPP_TEMPORALGRAPHSTREAM_H


#define TRACY_ENABLE


#include <string>
#include <iostream>

#include <limits>
#include <utility>
#include <vector>
#include <string>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <algorithm> 
#include <set>
#include <omp.h>
#include "BasicTypes.h"


namespace tglib {

	/**
	 * @brief The ordered edge list contains all temporal edges in chronological order
	 */
	template<typename E>
	class OrderedEdgeList {

	public:

		/**
		 * @brief Default constructor
		 */
		OrderedEdgeList() = default;

		/**
		 * @brief Constructor
		 * @param num_nodes_ The number of nodes
		 * @param edges_ The temporal edges
		 * @param ti_ The time interval
		 */
		OrderedEdgeList(size_t num_nodes_, std::vector<E> edges_, TimeInterval ti_) :
			num_nodes(num_nodes_), edges(edges_), ti(std::move(ti_)) {};

		/**
		 * @brief Constructor
		 * @param num_nodes_ The number of nodes
		 * @param edges_ The temporal edges
		 * @param ti_ The time interval
		 * @param node_mapping_ The node mapping
		 */
		OrderedEdgeList(size_t num_nodes_, std::vector<E> edges_, TimeInterval ti_,
			std::unordered_map<NodeId, NodeId> node_mapping_) :
			num_nodes(num_nodes_), edges(edges_), ti(std::move(ti_)) {
			node_map = std::move(node_mapping_);
			reverse_node_map.resize(node_map.size(), 0);
			for (auto p : node_map) {
				reverse_node_map[p.second] = p.first;
			}
		};

		/**
		 * @brief Getter for number of nodes
		 * @return The number of nodes.
		 */
		[[nodiscard]] size_t getNumberOfNodes() const {
			return num_nodes;
		}

		/**
		* @brief Getter for number of edges
		* @return The number of edges.
		*/
		[[nodiscard]] size_t getNumberOfEdges() const {
			return edges.size();
		}

		/**
		 * @brief Getter for edges
		 * @return Const reference to edges.
		 */
		const std::vector<E>& getEdges() const {
			return edges;
		}

		/**
		 * @brief Getter for number of the time interval spanned by the temporal graph
		 * @return The time interval.
		 */
		[[nodiscard]] TimeInterval getTimeInterval() const {
			return ti;
		}

		/**
		  * @brief Getter for mapping from new ids to the original ids used in input file
		  * @return The mapping
		  */
		const std::vector<NodeId>& getReverseNodeMap() const {
			return reverse_node_map;
		}

		/**
		  * @brief Getter for mapping from new ids to the original ids used in input file
		  * @return The mapping
		  */
		const std::unordered_map<NodeId, NodeId>& getNodeMap() const {
			return node_map;
		}

		const std::vector<std::map<std::string, int>> getDegreeList() {
			OrderedEdgeList<E> const& tgs = *this;
			return get_degrees(tgs);
		}

		const TemporalGraphStatistics getStats() {
			OrderedEdgeList<E> const& tgs = *this;
			return get_statistics(tgs);
		}
		const TemporalGraphStatistics getStatsOmp(int num_threads) {
			OrderedEdgeList<E> const& tgs = *this;
			return get_statistics_omp(tgs, num_threads);
		}

	private:

		/**
		 * @brief The number of nodes.
		 */
		size_t num_nodes{};

		/**
		 * @brief The chronological ordered temporal edges. Ties are broken arbitrarily.
		 */
		std::vector<E> edges;

		/**
		 * @brief The time interval spanned by the temporal graph
		 */
		TimeInterval ti;

		/**
		 * @brief The mapping from new ids to the original ids used in input file
		 */
		std::vector<NodeId> reverse_node_map;

		/**
		  * @brief The mapping from the original ids used in input file to the new node ids in [0, num_nodes-1]
		  */
		std::unordered_map<NodeId, NodeId> node_map;



		static bool comparePaires(std::pair<NodeId, int> e1, std::pair<NodeId, int> e2) {
			return e1.second < e2.second;
		}

		static bool compareInDegrees(std::map<std::string, int> e1, std::map<std::string, int>e2) {
			return e1["in_degree"] < e2["in_degree"];
		}
		static bool compareOutDegrees(std::map<std::string, int> e1, std::map<std::string, int>e2) {
			return e1["out_degree"] < e2["out_degree"];
		}

		/**
		 * @brief return vector of nodeIds and in degrees
		 * @tparam E The edge type
		 * @param tgs The temporal graph
		 * @return The rank statistics
		 */
		template<typename E>
		std::vector<std::map<std::string, int>> get_degrees(OrderedEdgeList<E> const& tgs) {
			std::map<NodeId, std::pair<int, int>> degrees;


			std::vector<NodeId> nodes = tgs.getReverseNodeMap();
			for (auto& it : nodes) {
				degrees[it] = std::pair<int, int>(0, 0);
			}
			for (auto& e : tgs.getEdges()) {
				degrees[e.v].first++;
				degrees[e.u].second++;
			}

			std::vector< std::map<std::string, int>> degreeVector;
			for (auto& e : degrees) {
				degreeVector.push_back({ {"node_id",e.first}, {"in_degree", e.second.first}, {"out_degree", e.second.second} });
			}

			std::sort(degreeVector.begin(), degreeVector.end(), compareInDegrees);

			int actual_rank = 0;
			int rank = 1;
			for (int e = 0; e < degreeVector.size(); e++) {
				rank++;
				if (e > 0) {
					if (degreeVector[e]["in_degree"] > degreeVector[e - 1]["in_degree"]) {
						actual_rank = rank;
						//std::cout << "switch want: " << degreeVector[e]["in_degree"] << " > " << degreeVector[e - 1]["in_degree"] << "\n";
					}
				}
				//if (rank <= 150) {

					//std::cout << "indegree: " << degreeVector[e]["in_degree"] << ", rank: " << rank << ", actual_rank: " << actual_rank << ", node: " << degreeVector[e]["node_id"] << "\n";
				//}
				degreeVector[e].insert({ "in_degree_rank", actual_rank });
			}

			std::sort(degreeVector.begin(), degreeVector.end(), compareOutDegrees);
			int i = 1;
			for (int e = 0; e < degreeVector.size(); e++) {
				if (e > 0) {
					if (degreeVector[e]["out_degree"] > degreeVector[e - 1]["out_degree"]) {
						i++;
					}
				}
				degreeVector[e].insert({ "out_degree_rank", i });
			}

			return degreeVector;
		}
	};

	/**
	 * @brief == operator OrderedEdgeList<E>
	 * @tparam E
	 * @param e1
	 * @param e2
	 * @return
	 */
	template<typename E>
	inline bool operator==(const OrderedEdgeList<E>& e1, const OrderedEdgeList<E>& e2) {
		return e1.getNumberOfNodes() == e2.getNumberOfNodes() &&
			e1.getEdges() == e2.getEdges() &&
			e1.getTimeInterval() == e2.getTimeInterval();
	}

	/**
	 * @brief != operator OrderedEdgeList<E>
	 * @tparam E
	 * @param e1
	 * @param e2
	 * @return
	 */
	template<typename E>
	inline bool operator!=(const OrderedEdgeList<E>& e1, const OrderedEdgeList<E>& e2) {
		return !(e1 == e2);
	}


	// todo add edge, remove edge
	/**
	 * @brief Computes the basic statistics of a temporal graph
	 * @tparam E The edge type
	 * @param tgs The temporal graph
	 * @return The basic statistics
	 */
	template<typename E>
	TemporalGraphStatistics get_statistics(OrderedEdgeList<E> const& tgs) {
		TemporalGraphStatistics statistics{};
		statistics.minTemporalInDegree = inf;
		statistics.minTemporalOutDegree = inf;
		statistics.maxTemporalInDegree = 0;
		statistics.maxTemporalOutDegree = 0;
		statistics.maximalTimeStamp = 0;
		statistics.minimalTimeStamp = inf;
		statistics.maximalTransitionTime = 0;
		statistics.minimalTransitionTime = inf;

		std::vector<long> inDegree(tgs.getNumberOfNodes(), 0);// counter list for in degrees
		std::vector<long> outDegree(tgs.getNumberOfNodes(), 0);
		std::unordered_set<Time> times;
		std::unordered_set<Time> transition_times;
		std::set<std::pair<NodeId, NodeId>> static_edges;

		auto edgeVect = tgs.getEdges();

		for (int i = 0; i < edgeVect.size(); i++) {
			auto& e = edgeVect[i];
			inDegree[e.v]++;
			outDegree[e.u]++;
			times.insert(e.t);
			transition_times.insert(e.tt);
			static_edges.insert({ e.u, e.v });

			if (statistics.maximalTimeStamp < e.t) {
				statistics.maximalTimeStamp = e.t;
			}
			if (statistics.minimalTimeStamp > e.t) {
				statistics.minimalTimeStamp = e.t;
			}
			if (statistics.maximalTransitionTime < e.tt) {
				statistics.maximalTransitionTime = e.tt;
			}
			if (statistics.minimalTransitionTime > e.tt) {
				statistics.minimalTransitionTime = e.tt;
			}
		}

		for (size_t nid = 0; nid < tgs.getNumberOfNodes(); ++nid) {
			if (statistics.minTemporalInDegree > inDegree[nid]) statistics.minTemporalInDegree = inDegree[nid];
			if (statistics.minTemporalOutDegree > outDegree[nid]) statistics.minTemporalOutDegree = outDegree[nid];
			if (statistics.maxTemporalInDegree < inDegree[nid])  statistics.maxTemporalInDegree = inDegree[nid];
			if (statistics.maxTemporalOutDegree < outDegree[nid])  statistics.maxTemporalOutDegree = outDegree[nid];
		}

		statistics.numberOfNodes = tgs.getNumberOfNodes();
		statistics.numberOfEdges = tgs.getEdges().size();
		statistics.numberOfStaticEdges = static_edges.size();
		statistics.numberOfTimeStamps = times.size();
		statistics.numberOfTransitionTimes = transition_times.size();

		return statistics;
	}
	
	template<typename E>
	TemporalGraphStatistics get_statistics_omp(OrderedEdgeList<E> const& tgs, int num_threads) {
		TemporalGraphStatistics statistics{};
		statistics.minTemporalInDegree = inf;
		statistics.minTemporalOutDegree = inf;
		statistics.maxTemporalInDegree = 0;
		statistics.maxTemporalOutDegree = 0;
		statistics.maximalTimeStamp = 0;
		statistics.minimalTimeStamp = inf;
		statistics.maximalTransitionTime = 0;
		statistics.minimalTransitionTime = inf;

		std::vector<long> inDegree(tgs.getNumberOfNodes(), 0);// counter list for in degrees
		std::vector<long> outDegree(tgs.getNumberOfNodes(), 0);
		std::unordered_set<Time> times;
		std::unordered_set<Time> transition_times;
		std::set<std::pair<NodeId, NodeId>> static_edges;

		auto edgeVect = tgs.getEdges();

		omp_set_num_threads(num_threads);
		omp_lock_t setTtLock;
		omp_init_lock(&setTtLock);
		omp_lock_t setTsLock;
		omp_init_lock(&setTsLock);
		omp_lock_t insertLock;
		omp_init_lock(&insertLock);
#pragma omp parallel for
		for (int i = 0; i < edgeVect.size(); i++) {
			auto& e = edgeVect[i];
			inDegree[e.v]++;
			outDegree[e.u]++;
			omp_set_lock(&insertLock);
			times.insert(e.t);
			transition_times.insert(e.tt);
			static_edges.insert({ e.u, e.v });
			omp_unset_lock(&insertLock);

			if (statistics.maximalTimeStamp < e.t) {
				omp_set_lock(&setTsLock);
				statistics.maximalTimeStamp = e.t;
				omp_unset_lock(&setTsLock);
			}
			if (statistics.minimalTimeStamp > e.t) {
				omp_set_lock(&setTsLock);
				statistics.minimalTimeStamp = e.t;
				omp_unset_lock(&setTsLock);
			}
			if (statistics.maximalTransitionTime < e.tt) {
				omp_set_lock(&setTtLock);
				statistics.maximalTransitionTime = e.tt;
				omp_unset_lock(&setTtLock);
			}
			if (statistics.minimalTransitionTime > e.tt) {
				omp_set_lock(&setTtLock);
				statistics.minimalTransitionTime = e.tt;
				omp_unset_lock(&setTtLock);
			}
		}

		for (size_t nid = 0; nid < tgs.getNumberOfNodes(); ++nid) {
			if (statistics.minTemporalInDegree > inDegree[nid]) statistics.minTemporalInDegree = inDegree[nid];
			if (statistics.minTemporalOutDegree > outDegree[nid]) statistics.minTemporalOutDegree = outDegree[nid];
			if (statistics.maxTemporalInDegree < inDegree[nid])  statistics.maxTemporalInDegree = inDegree[nid];
			if (statistics.maxTemporalOutDegree < outDegree[nid])  statistics.maxTemporalOutDegree = outDegree[nid];
		}

		statistics.numberOfNodes = tgs.getNumberOfNodes();
		statistics.numberOfEdges = tgs.getEdges().size();
		statistics.numberOfStaticEdges = static_edges.size();
		statistics.numberOfTimeStamps = times.size();
		statistics.numberOfTransitionTimes = transition_times.size();

		return statistics;
	}

} // tglib

#endif //CPP_TEMPORALGRAPHSTREAM_H
