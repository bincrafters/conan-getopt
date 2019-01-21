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
    license = "LGPL-2.1"
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    _source_subfolder = "source_subfolder"
    _build_subfolder = "build_subfolder"

    def config_options(self):
        if self.settings.os == 'Windows':
            del self.options.fPIC

    def configure(self):
        del self.settings.compiler.libcxx

    def source(self):
        gist = "7776712"
        commit_id = "84a97c280a5889ccc01a608a1b918ead7b2c3661"
        source_url = "https://gist.github.com/ashelly"
        sha256 = "ecea1a70927e637f4e2ad84dc4905212d72f1cdeb1c3317a44597cb971bc2321"
        tools.get("{}/{}/archive/{}.zip".format(source_url, gist, commit_id), sha256=sha256)
        extracted_dir = gist + '-' + commit_id
        os.rename(extracted_dir, self._source_subfolder)

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(build_folder=self._build_subfolder)
        return cmake

    def _extract_license(self):
        content = tools.load(os.path.join(self._source_subfolder, "getopt.c"))
        license_contents = content[2:content.find("*/", 1)]
        tools.save("LICENSE", license_contents)

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        self._extract_license()
        self.copy(pattern="LICENSE", dst="licenses")
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["getopt"]
        self.cpp_info.defines.append("__GNU_LIBRARY__")
