
#include <iostream>
#include <catch2/catch_test_macros.hpp>
#include "../../src/core/BasicTypes.h"
#include "../../src/core/OrderedEdgeList.h"
#include "../../src/core/TRSGraph.h"
#include "../../src/util/InputOutput.h"
#include "../TemporalGraphsInstances.h"
#include "../../src/core/Transformations.h"
#include "../../src/algorithms/TemporalClusteringCoefficient.h"
#include "../../src/algorithms/TemporalPageRank.h"
#include <set>
#include <algorithm>

using namespace tglib;


std::string map_to_string(std::map<std::string, int>& m) {
	std::string output = "";
	std::string convrt = "";
	std::string result = "";

	for (auto it = m.cbegin(); it != m.cend(); it++) {

		convrt = std::to_string(it->second);
		output += (it->first) + ":" + (convrt)+", ";
	}

	result = output.substr(0, output.size() - 2);

	return result;
}

OrderedEdgeList<TemporalEdge> test_load_ime(std::string inPath) {
	auto tgs = load_ordered_edge_list<TemporalEdge>(inPath);
	return  tgs;
}

TemporalGraphStatistics test_get_stats(OrderedEdgeList<TemporalEdge> tgs) {
	auto stats = tgs.getStats();
	return stats;
}

std::vector<double> test_clustering_coefficient(OrderedEdgeList<TemporalEdge> tgs) {
	auto tg = to_incident_lists<TGNode>(tgs);
	auto cc = temporal_clustering_coefficient(tg, tg.getTimeInterval());

	return cc;
}

std::vector<double> test_page_rank(OrderedEdgeList<TemporalEdge> tgs) {
	auto pr = temporal_pagerank<TemporalEdge>(tgs, 0.5, 0.5, 0.5);

	return pr;
}

std::vector<std::map<std::string, int>> test_degree_list(OrderedEdgeList<TemporalEdge> tgs) {
	auto deg = tgs.getDegreeList();

	return deg;
}

TEST_CASE("timing", "[timing]") {
	std::string inPath = "C:/Users/dries/Documents/GitHub/Code/Data/Flights.txt";

	auto tgs = test_load_ime(inPath);

	auto stats = test_get_stats(tgs);

	auto cc = test_clustering_coefficient(tgs);

	//std::cout << cc << "\n";

	auto pr = test_page_rank(tgs);

	//auto deg = test_degree_list(tgs);

}
