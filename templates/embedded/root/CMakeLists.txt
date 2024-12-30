cmake_minimum_required(VERSION 3.30)
project(PROJECTNAME VERSION 0.0.1 LANGUAGES C CXX)

# Update the submodules here
#include(cmake/UpdateSubmodules.cmake)

set(CMAKE_CXX_STANDARD 20)

enable_testing() # need to create CTestTestfile.cmake files for each project

###------ Executable ------###
add_executable(PROJECTNAME drivers/driver.c PROJECTNAME.cc)

###------ Tests ------###
add_executable(PROJECTNAME_tests drivers/driver.c tests/driver_test.cpp)
