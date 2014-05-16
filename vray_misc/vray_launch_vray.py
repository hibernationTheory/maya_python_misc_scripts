import maya.cmds as cmds
import maya.mel as mel

cmds.loadPlugin("vrayformaya")

renderers = ["mayaSoftware", "vray"]

myRenderer = renderers[1]
mel.eval("setCurrentRenderer %s" %myRenderer)
print "renderer is set to %s" % myRenderer