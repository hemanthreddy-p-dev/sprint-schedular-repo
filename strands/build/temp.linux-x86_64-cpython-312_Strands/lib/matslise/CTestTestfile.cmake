# CMake generated Testfile for 
# Source directory: /workspaces/sprint_ceremony_scheduler/strands/lib/matslise
# Build directory: /workspaces/sprint_ceremony_scheduler/strands/build/temp.linux-x86_64-cpython-312_Strands/lib/matslise
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(MatsliseTesting "/workspaces/sprint_ceremony_scheduler/strands/build/temp.linux-x86_64-cpython-312_Strands/lib/matslise/test/matslise_test")
set_tests_properties(MatsliseTesting PROPERTIES  _BACKTRACE_TRIPLES "/workspaces/sprint_ceremony_scheduler/strands/lib/matslise/CMakeLists.txt;8;add_test;/workspaces/sprint_ceremony_scheduler/strands/lib/matslise/CMakeLists.txt;0;")
subdirs("matslise")
subdirs("test")
