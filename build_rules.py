#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Build rules for the makeprojects suite of build tools.

This file is parsed by the cleanme, buildme, rebuildme and makeprojects
command line tools to clean, build and generate project files.

When any of these tools are invoked, this file is loaded and parsed to
determine special rules on how to handle building the code and / or data.
"""

# pylint: disable=unused-argument

from __future__ import absolute_import, print_function, unicode_literals

import sys
from burger import clean_directories, clean_files, clean_xcode

# If set to True, Don't parse directories in this folder when ``-r``
# is active.
# Can be overridden above
NO_RECURSE = True

# Process these folders before processing this folder
# Can be overridden above
DEPENDENCIES = None

# If any IDE file is present, cleanme and buildme will process them.
# Can be overridden above
PROCESS_PROJECT_FILES = False

########################################


def clean(working_directory):
    """
    Delete temporary files.

    This function is called by ``cleanme`` to remove temporary files.

    On exit, return 0 for no error, or a non zero error code if there was an
    error to report.

    Args:
        working_directory
            Directory this script resides in.

    Returns:
        None if not implemented, otherwise an integer error code.
    """

    clean_directories(working_directory,
    (".vscode",
     "temp",
     "ipch",
     "bin",
     ".vs",
     "*_Data",
     "* Data",
     "__pycache__"))

    clean_files(working_directory,
    (".DS_Store",
     "*.suo",
     "*.user",
     "*.ncb",
     "*.err",
     "*.sdf",
     "*.layout.cbTemp",
     "*.VC.db",
     "*.pyc",
     "*.pyo"))

    clean_xcode(working_directory)
    return 0


# If called as a command line and not a class, perform the build
if __name__ == "__main__":
    sys.exit(0)
