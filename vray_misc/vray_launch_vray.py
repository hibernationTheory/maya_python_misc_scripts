import maya.cmds as cmds
import maya.mel as mel

renderers = ["mayaSoftware", "vray"]
myRenderer = renderers[1]
mel.eval("setCurrentRenderer %s" %myRenderer)