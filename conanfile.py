#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
from conans.errors import ConanInvalidConfiguration
import os


class GetOptConan(ConanFile):
    name = "getopt"
    version = "2.0"
    description = "Port of GNU getopt to Win32"
    topics = ("conan", "getopt", "command line", "options")
    url = "https://github.com/bincrafters/conan-getopt"
    homepage = "https://github.com/skandhurkat/Getopt-for-Visual-Studio"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "MIT", "BSD-2-Clause"
    exports = ["LICENSE.md"]
    no_copy_source = True
    _source_subfolder = "source_subfolder"

    def configure(self):
        if not tools.os_info.is_windows:
            raise ConanInvalidConfiguration("This project is ONLY supported for Windows")

    def source(self):
        commit_id = "2a6e4fb7f501b863c5bc32dd6e7277f110f1e14b"
        sha256 = "b5a23f87cd755561daf465eed5824021d18a462c24ee05e4fd5932dc29f4a468"
        tools.get("{}/archive/{}.zip".format(self.homepage, commit_id), sha256=sha256)
        extracted_dir = 'Getopt-for-Visual-Studio-' + commit_id
        os.rename(extracted_dir, self._source_subfolder)

    def _extract_license(self):
        content = tools.load(os.path.join(self.source_folder, self._source_subfolder, "getopt.h"))
        license_contents = content[content.find("/**", 3):content.find("#pragma")]
        tools.save("LICENSE", license_contents)

    def package(self):
        self._extract_license()
        self.copy(pattern="LICENSE", dst="licenses")
        self.copy("getopt.h", dst="include", src=self._source_subfolder)

    def package_id(self):
        self.info.header_only()
