from conan import ConanFile
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain, cmake_layout
from conan.tools.files import copy
import os


class TcpConan(ConanFile):
    name = "tcp"
    version = "0.0.1"
    author = "Marc Hayden marc.j.hayden@protonmail.com"
    description = "tcp library"
    settings = "os", "compiler", "build_type", "arch"

    options = {
        "shared": [True, False],
        "fPIC": [True, False]
    }
    default_options = {
        "shared": True,
        "fPIC": True
    }

    def layout(self):
        cmake_layout(self)

    def generate(self):
        for dep in self.dependencies.values():
            print(dep.cpp_info.includedirs[0])
            try:
                copy(
                    self, "*.so*", dep.cpp_info.libdirs[0], os.path.join(self.build_folder, "lib"))
            except:
                pass
            try:
                copy(
                    self, "*.a", dep.cpp_info.libdirs[0], os.path.join(self.build_folder, "lib"))
            except:
                pass
            try:
                copy(
                    self, "*.so.*", dep.cpp_info.libdirs[0], os.path.join(self.build_folder, "lib"))
            except:
                pass

        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self, generator="Ninja")
        tc.variables["CMAKE_EXPORT_COMPILE_COMMANDS"] = True
        tc.variables["CMAKE_POSITION_INDEPENDENT_CODE"] = self.options.fPIC
        tc.variables["BUILD_SHARED_LIBS"] = self.options.shared
        tc.generate()
        pass

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        pass

    def configure(self):
        self.options["*"].shared = self.options.shared
        self.options["*"].fPIC = self.options.fPIC
        pass

    def requirements(self):
        self.requires("boost/1.85.0")
        pass
