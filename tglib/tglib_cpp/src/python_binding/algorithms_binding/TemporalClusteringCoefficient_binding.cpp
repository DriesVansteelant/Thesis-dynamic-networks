/* Copyright (C) 2022 Lutz Oettershagen - All Rights Reserved
 *
 * This file is part of TGLib which is released under MIT license.
 * See file LICENSE.md or go to https://gitlab.com/tgpublic/tglib
 * for full license details.
 */

/**
 * @file TemporalClusteringCoefficient_binding.cpp
 * @brief This file provides the python binding code.
 *
 */

#include <sstream>
#include "../../algorithms/TemporalClusteringCoefficient.h"
#include <pybind11/pybind11.h>

namespace tglib_python_binding {

using namespace tglib;

void bind_TemporalClusteringCoefficient(pybind11::module_ &m) {

    m.def("temporal_clustering_coefficient",
          pybind11::overload_cast<IncidentLists<TGNode, TemporalEdge> const&, TimeInterval>(&temporal_clustering_coefficient<TGNode, TemporalEdge>));

    m.def("temporal_clustering_coefficient",
          pybind11::overload_cast<IncidentLists<TGNode, TemporalEdge> const&, NodeId, TimeInterval>(&temporal_clustering_coefficient<TGNode, TemporalEdge>));

}

}