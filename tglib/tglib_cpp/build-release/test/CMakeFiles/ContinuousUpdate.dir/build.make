# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/dries/Documents/Thesis/code/tglib-main/tglib_cpp

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/dries/Documents/Thesis/code/tglib-main/tglib_cpp/build-release

# Utility rule file for ContinuousUpdate.

# Include the progress variables for this target.
include test/CMakeFiles/ContinuousUpdate.dir/progress.make

test/CMakeFiles/ContinuousUpdate:
	cd /home/dries/Documents/Thesis/code/tglib-main/tglib_cpp/build-release/test && /usr/bin/ctest -D ContinuousUpdate

ContinuousUpdate: test/CMakeFiles/ContinuousUpdate
ContinuousUpdate: test/CMakeFiles/ContinuousUpdate.dir/build.make

.PHONY : ContinuousUpdate

# Rule to build all files generated by this target.
test/CMakeFiles/ContinuousUpdate.dir/build: ContinuousUpdate

.PHONY : test/CMakeFiles/ContinuousUpdate.dir/build

test/CMakeFiles/ContinuousUpdate.dir/clean:
	cd /home/dries/Documents/Thesis/code/tglib-main/tglib_cpp/build-release/test && $(CMAKE_COMMAND) -P CMakeFiles/ContinuousUpdate.dir/cmake_clean.cmake
.PHONY : test/CMakeFiles/ContinuousUpdate.dir/clean

test/CMakeFiles/ContinuousUpdate.dir/depend:
	cd /home/dries/Documents/Thesis/code/tglib-main/tglib_cpp/build-release && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/dries/Documents/Thesis/code/tglib-main/tglib_cpp /home/dries/Documents/Thesis/code/tglib-main/tglib_cpp/test /home/dries/Documents/Thesis/code/tglib-main/tglib_cpp/build-release /home/dries/Documents/Thesis/code/tglib-main/tglib_cpp/build-release/test /home/dries/Documents/Thesis/code/tglib-main/tglib_cpp/build-release/test/CMakeFiles/ContinuousUpdate.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : test/CMakeFiles/ContinuousUpdate.dir/depend

