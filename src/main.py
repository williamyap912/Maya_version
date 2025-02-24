import maya.cmds as cmds
from ui import VersionControlUI

def launch_ui():
    """Launch the Version Control UI in Maya."""
    global tool_ui
    try:
        tool_ui.close()  # Close existing UI if open
    except:
        pass
    tool_ui = VersionControlUI()
    tool_ui.show()