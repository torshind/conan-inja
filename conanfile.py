from conans import ConanFile, CMake, tools


class InjaConan(ConanFile):
    name = "inja"
    version = "2.1.0"
    license = "MIT"
    url = "https://pantor.github.io/inja/"
    description = "A Template Engine for Modern C++"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake_find_package"
    exports_sources = "*"
    requires = "nlohmann_json/3.6.1@torshind/stable"

    def source(self):
        git = tools.Git()
        git.clone("https://github.com/pantor/inja.git", "v" + self.version)

    def build(self):
        pass

    def package(self):
        cmake = CMake(self)
        cmake.definitions["INJA_USE_EMBEDDED_JSON"] = "OFF"
        cmake.definitions["BUILD_TESTING"] = "OFF"
        cmake.definitions["BUILD_BENCHMARK"] = "OFF"
        cmake.configure()
        cmake.install()

    def package_info(self):
        self.info.header_only()
