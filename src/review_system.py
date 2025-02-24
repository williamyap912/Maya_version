import maya.cmds as cmds

def add_comment(comment_text, target_object):
    """Attach a comment to a Maya object."""
    if not cmds.objExists(target_object):
        cmds.confirmDialog(title="Error", message="Object not found!")
        return

    if not cmds.attributeQuery("reviewComment", node=target_object, exists=True):
        cmds.addAttr(target_object, ln="reviewComment", dt="string")

    cmds.setAttr(f"{target_object}.reviewComment", comment_text, type="string")

def get_comment(target_object):
    """Retrieve the comment from a Maya object."""
    if cmds.objExists(f"{target_object}.reviewComment"):
        return cmds.getAttr(f"{target_object}.reviewComment")
    return "No comment found."