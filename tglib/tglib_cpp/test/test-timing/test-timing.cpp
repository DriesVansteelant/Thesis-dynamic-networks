
#include <iostream>
#include <catch2/catch_test_macros.hpp>
#include "../../src/core/BasicTypes.h"
#include "../../src/core/OrderedEdgeList.h"
#include "../../src/core/TRSGraph.h"
#include "../../src/util/InputOutput.h"
#include "../TemporalGraphsInstances.h"
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

TEST_CASE("timing", "[timing]") {
    
    std::cout << "start test timing \n";
       



    auto tgs = load_ordered_edge_list<TemporalEdge>(
        "../../../../../Code/Data/flights.txt");

    auto deg = tgs.getDegreeList();
    //for (auto d : deg) {

    //    //std::cout << map_to_string(d) << "\n";
    //}

}
