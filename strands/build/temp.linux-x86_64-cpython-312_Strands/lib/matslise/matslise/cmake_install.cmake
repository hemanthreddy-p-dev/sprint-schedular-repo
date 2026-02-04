# Install script for directory: /workspaces/sprint-schedular-repo/strands/lib/matslise/matslise

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/workspaces/sprint-schedular-repo/strands/build/lib.linux-x86_64-cpython-312/strands")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set path to fallback-tool for dependency-resolution.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE STATIC_LIBRARY FILES "/workspaces/sprint-schedular-repo/strands/build/temp.linux-x86_64-cpython-312_Strands/lib/matslise/matslise/libmatslise.a")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/matslise" TYPE FILE FILES
    "/workspaces/sprint-schedular-repo/strands/lib/matslise/matslise/matslise.h"
    "/workspaces/sprint-schedular-repo/strands/lib/matslise/matslise/matscs.h"
    "/workspaces/sprint-schedular-repo/strands/lib/matslise/matslise/matsliseNd.h"
    "/workspaces/sprint-schedular-repo/strands/lib/matslise/matslise/formula_constants.h"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/matslise/util" TYPE FILE FILES
    "/workspaces/sprint-schedular-repo/strands/lib/matslise/matslise/util/y.h"
    "/workspaces/sprint-schedular-repo/strands/lib/matslise/matslise/util/eigen.h"
    "/workspaces/sprint-schedular-repo/strands/lib/matslise/matslise/util/sectorbuilder.h"
    "/workspaces/sprint-schedular-repo/strands/lib/matslise/matslise/util/rectangle.h"
    "/workspaces/sprint-schedular-repo/strands/lib/matslise/matslise/util/scoped_timer.h"
    )
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
if(CMAKE_INSTALL_LOCAL_ONLY)
  file(WRITE "/workspaces/sprint-schedular-repo/strands/build/temp.linux-x86_64-cpython-312_Strands/lib/matslise/matslise/install_local_manifest.txt"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
endif()
