import maya.cmds as mc
import maya.mel as mel

counter = int(raw_input("enter_a_number"))
try:
    counter = int(counter)
except ValueError:
    print "enter a number!!!"
    counter = None

if counter:
    objs = mc.ls(sl=True)
    
    for obj in objs:
        mc.select(obj)
        mel.eval("vray objectProperties add_multiple;")
        vrop = cmds.listConnections(type="VRayObjectProperties")[0]
        mc.setAttr("%s.objectIDEnabled" %vrop, 1)
        mc.setAttr("%s.objectID" %vrop, counter)
        counter += 1