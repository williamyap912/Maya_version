import maya.cmds as cmds
import os
import datetime

SAVE_PATH = os.path.expanduser("~/maya/version_control/")

def get_scene_name():
    """Get the current Maya scene name."""
    return cmds.file(q=True, sn=True, shortName=True) or "untitled"

def save_new_version():
    """Save the current Maya file as a new version."""
    if not os.path.exists(SAVE_PATH):
        os.makedirs(SAVE_PATH)

    scene_name = get_scene_name()
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    versioned_file = f"{SAVE_PATH}{scene_name}_v{timestamp}.ma"

    cmds.file(rename=versioned_file)
    cmds.file(save=True, type="mayaAscii")
    return versioned_file

def load_last_version():
    """Load the last saved version of the Maya file."""
    if not os.path.exists(SAVE_PATH):
        cmds.confirmDialog(title="Error", message="No previous versions found!")
        return

    files = sorted(os.listdir(SAVE_PATH), reverse=True)
    if files:
        latest_file = os.path.join(SAVE_PATH, files[0])
        cmds.file(latest_file, open=True, force=True)
        cmds.confirmDialog(title="Loaded", message=f"Loaded {latest_file}")
    else:
        cmds.confirmDialog(title="Error", message="No previous versions available!")
