# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Release")
  file(REMOVE_RECURSE
  "CMakeFiles\\kobe_autogen.dir\\AutogenUsed.txt"
  "CMakeFiles\\kobe_autogen.dir\\ParseCache.txt"
  "kobe_autogen"
  )
endif()
