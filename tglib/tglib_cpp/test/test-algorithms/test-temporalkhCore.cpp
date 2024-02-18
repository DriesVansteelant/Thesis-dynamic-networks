///* Copyright (C) 2022 Lutz Oettershagen - All Rights Reserved
// *
// * This file is part of TGLib which is released under MIT license.
// * See file LICENSE.md or go to https://gitlab.com/tgpublic/tglib
// * for full license details.
// */
//
//#include <iostream>
//#include <catch2/catch_test_macros.hpp>
//#include <catch2/catch_approx.hpp>
//#include "../TemporalGraphsInstances.h"
//#include "../../src/core/Transformations.h"
//#include "../../src/algorithms/TemporalkhCore.h"
//
//using namespace tglib;
//using namespace std;
//
//TEST_CASE( "temporal kcore", "[temporal_khcore]" ) {
//    auto tgs = getExampleTgh();
//
//    auto g = to_aggregated_edge_list(tgs);
//
//    auto c = compute_kcores(g);
//
//    for (auto v : c) {
//        std::cout << v << std::endl;
//    }
//}
//
