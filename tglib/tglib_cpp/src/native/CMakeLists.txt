# Copyright (C) 2022 Lutz Oettershagen - All Rights Reserved
#
# This file is part of TGLib which is released under MIT license.
# See file LICENSE.md or go to https://gitlab.com/tgpublic/tglib
# for full license details.

cmake_minimum_required(VERSION 3.6...3.18)
project(tglib)

set(NATIVE_SOURCES
	Main.cpp
        ../core/BasicTypes.h
        ../core/OrderedEdgeList.h

        ../core/AggregatedGraph.h
        ../core/IncidentLists.h
        ../core/TRSGraph.h
        ../core/DirectedLineGraph.h
        ../core/AggregatedGraph.h
        ../core/Transformations.h

        ../util/LabelPQ.h
        ../util/TopkResult.h
        ../util/UtilFunctions.h

        ../algorithms/TemporalBetweenness.h
        ../algorithms/TemporalClusteringCoefficient.h
        ../algorithms/TemporalKatz.h
        ../algorithms/TemporalPageRank.h
        ../algorithms/Burstiness.h
        ../algorithms/TemporalDistances.h
        ../algorithms/TemporalkhCore.h

        ../algorithms/TemporalCloseness.h
        ../algorithms/TemporalClosenessApproximation.h
        ../algorithms/TemporalWalkCentrality.h
        ../algorithms/TemporalEfficiency.h
        ../algorithms/TemporalDiameter.h        
	../algorithms/TemporalPaths.h
        ../algorithms/TopologicalOverlap.h
        ../algorithms/TopkTemporalCloseness.h
        ../algorithms/TemporalReachability.h

        ../util/InputOutput.h

        )

# find_package(pybind11 REQUIRED)
# pybind11_add_module(pytglib ${PYTHON_BINDING_SOURCES})
add_executable(nativetglib ${NATIVE_SOURCES})
