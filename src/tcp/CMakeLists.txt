project(libtcp VERSION 0.0.1 LANGUAGES CXX)

add_library(${PROJECT_NAME} SHARED)

target_sources(${PROJECT_NAME}
    PRIVATE
    impl/tcp.cpp

    PUBLIC
    FILE_SET HEADERS BASE_DIRS ${PROJECT_SOURCE_DIR}/../../include
    FILES
    ${PROJECT_SOURCE_DIR}/../../include/tcp/tcp.hpp
)

target_include_directories(${PROJECT_NAME}
    PRIVATE
    ${PROJECT_SOURCE_DIR}
)

target_link_libraries(${PROJECT_NAME}
    PRIVATE
    # empty
)

install(
  TARGETS ${PROJECT_NAME}
  FILE_SET HEADERS
)