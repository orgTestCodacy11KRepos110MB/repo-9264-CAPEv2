#!/usr/bin/env python
# Copyright (C) 2018 phdphuc
# This software may be modified and distributed under the terms
# of the MIT license. See the LICENSE file for details.

from os import system

from lib.core.packages import Package


class Doc(Package):
    """LibreOffice document."""

    def prepare(self):
        system(f'/bin/chmod +x "{self.target}"')
        self.args = [self.target] + self.args
        self.target = "/usr/bin/libreoffice --writer"
