#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class GetOptConan(ConanFile):
    name = "getopt"
    version = "1.0"
    description = "Port of GNU getopt() to Win32 for anyone who's tired of dealing with getopt() calls in " \
                  "Unix-to-Windows ports"
    topics = ("conan", "getopt", "command line", "options")
    url = "https://github.com/bincrafters/conan-getopt"
    homepage = "http://www.pwilson.net/sample.html"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "GNU LGPL"
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"

    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    # Custom attributes for Bincrafters recipe conventions
    _source_subfolder = "source_subfolder"
    _build_subfolder = "build_subfolder"

    def config_options(self):
        if self.settings.os == 'Windows':
            del self.options.fPIC

    def configure(self):
        del self.settings.compiler.libcxx

    def source(self):
        for name in ["getopt.c", "getopt.h"]:
            tools.download("https://gist.githubusercontent.com/ashelly/7776712/raw/"
                           "84a97c280a5889ccc01a608a1b918ead7b2c3661/%s" % name, name)

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(build_folder=self._build_subfolder)
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder)
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["getopt"]
        self.cpp_info.defines.append("__GNU_LIBRARY__")
