cmake_minimum_required(VERSION 2.8.12)
project(getopt)

include(conanbuildinfo.cmake)
conan_basic_setup()

file(GLOB SOURCES getopt.c)
file(GLOB HEADERS getopt.h)

add_library(${PROJECT_NAME} ${SOURCES} ${HEADERS})
set_target_properties(${PROJECT_NAME} PROPERTIES
  PUBLIC_HEADER "${HEADERS}"
  WINDOWS_EXPORT_ALL_SYMBOLS ON)

install(TARGETS ${PROJECT_NAME}
  ARCHIVE DESTINATION "lib"
  LIBRARY DESTINATION "lib"
  RUNTIME DESTINATION "bin"
  PUBLIC_HEADER DESTINATION "include"
  COMPONENT library
)
