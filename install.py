# Maya Plugin Installer
import sys
import os
import maya.utils

PLUGIN_PATH = os.path("C:/Users/USER/Documents/maya/2022/scripts/Maya_version/src")
if PLUGIN_PATH not in sys.path:
    sys.path.append(PLUGIN_PATH)

maya.utils.executeDeferred("import main; main.launch_ui()")
