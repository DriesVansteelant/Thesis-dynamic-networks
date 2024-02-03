
#include <iostream>
#include <catch2/catch_test_macros.hpp>
#include "../../src/core/BasicTypes.h"
#include "../../src/core/OrderedEdgeList.h"
#include "../../src/core/TRSGraph.h"
#include "../TemporalGraphsInstances.h"
#include <set>
#include <algorithm>

using namespace tglib;


TEST_CASE("timing", "[timing]") {
    std::cout << "test-timing";
    TemporalEdge e1{ 0,1,1,1 };
    TemporalEdge e2{ 0,1,2,1 };

    REQUIRE(e1 < e2);
    REQUIRE(e1 != e2);
    REQUIRE(e1 == e1);
}