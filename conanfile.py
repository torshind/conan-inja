from conans import ConanFile, CMake


class InjaConan(ConanFile):
    name = "inja"
    version = "2.1.0"
    license = "MIT"
    homepage = "https://pantor.github.io/inja/"
    url = "https://github.com/torshind/conan-inja/"
    description = "A Template Engine for Modern C++"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake_find_package"
    exports_sources = "*"
    requires = "nlohmann_json/3.6.1@torshind/stable"

    def source(self):
        self.run("git clone --branch v"
                 + self.version
                 + " https://github.com/pantor/inja.git")

    def build(self):
        pass

    def package(self):
        cmake = CMake(self)
        cmake.definitions["INJA_USE_EMBEDDED_JSON"] = "OFF"
        cmake.definitions["BUILD_TESTING"] = "OFF"
        cmake.definitions["BUILD_BENCHMARK"] = "OFF"
        cmake.configure(source_folder="inja")
        cmake.install()

    def package_info(self):
        self.info.header_only()
