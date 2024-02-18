cmake_minimum_required(VERSION 3.4...3.18)
project(tglib)

set(TEST_SOURCES
        test-timing.cpp

        )

target_sources(custom-main-tests PRIVATE ${TEST_SOURCES})