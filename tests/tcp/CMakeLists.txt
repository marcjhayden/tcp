project(test_libtcp LANGUAGES CXX)

find_package(Boost REQUIRED)

add_executable(${PROJECT_NAME} 
  test-tcp.cpp
)

target_compile_definitions(${PROJECT_NAME} 
  PRIVATE
  BOOST_TEST_DYN_LINK
)

target_include_directories(${PROJECT_NAME} 
  PRIVATE
  ${Boost_INCLUDE_DIRS}
  ${PROJECT_SOURCE_DIR}/../../include
)

target_link_libraries(${PROJECT_NAME} 
  PRIVATE
  libtcp
  Boost::unit_test_framework
)

install(TARGETS ${PROJECT_NAME} DESTINATION "."
  RUNTIME DESTINATION bin
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
)