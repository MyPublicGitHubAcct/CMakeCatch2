cmake_minimum_required(VERSION 3.30)
project(CMakeCatch2 VERSION 0.0.1 LANGUAGES C CXX)

# Update the submodules here
#include(cmake/UpdateSubmodules.cmake)

set(CMAKE_CXX_STANDARD 20)

enable_testing() # need to create CTestTestfile.cmake files for each project

###------ Executable ------###


add_executable(CMakeCatch2 main.cpp)


###------ Tests ------###
