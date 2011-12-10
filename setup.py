from distutils.core import setup
import py2exe
import sys

# If run without args, build executables, in quiet mode.
if len(sys.argv) == 1:
    sys.argv.append("py2exe")
    sys.argv.append("-q")

class Target:
    def __init__(self, **kw):
        self.__dict__.update(kw)
        # for the versioninfo resources
        self.version = "0.2.0.1"
        self.company_name = "oedalpha"
        #self.copyright = ""
        self.name = "Hangul Unzip"


hunzip = Target(
    # used for the versioninfo resource
    description = "hunzip: Hangul Unzip",

    # what to build
    script = "hunzip.py",
##    icon_resources = [(1, "icon.ico")],
    dest_base = "hunzip")

################################################################

setup(
    options = {"py2exe": {"compressed": 1,
                          "optimize": 2,
                          "ascii": 1,
                          "bundle_files": 1,
                          "packages": "encodings",
                          }},
#    data_files=[(".", ["README", "LICENSE"])],
    zipfile = None,
    console = [hunzip],
    )

