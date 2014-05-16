import maya.cmds as mc
import maya.mel as mel

mats = mc.ls(sl=True)

for mat in mats:
    name = "CUSTOM_MATTE"
    object_id = mc.getAttr("%s.objectID" %mat)
    version = object_id/3
    
    last = (version+1)*3
    mid = last-1
    first = last -2
    
    name = name + "_" + str(version)
    exists = mc.ls(name, type="VRayRenderElement")
    if not exists:
        multiMatte = mel.eval("vrayAddRenderElement MultiMatteElement;")
        multiMatte = mc.rename(multiMatte, name)
        mc.setAttr("%s.vray_name_multimatte" %multiMatte, name, type="string") 
        mc.setAttr("%s.vray_redid_multimatte" %multiMatte, first)
        mc.setAttr("%s.vray_greenid_multimatte" %multiMatte, mid)
        mc.setAttr("%s.vray_blueid_multimatte" %multiMatte, last)