import maya.cmds as mc
import maya.mel as mel

lgts = mc.ls(sl=True)

for lgt in lgts:
    lgtSelect = mel.eval("vrayAddRenderElement LightSelectElement;")
    mc.setAttr("%s.vray_type_lightselect" %lgtSelect, 2)
    lgtSelect = mc.rename(lgtSelect, "LGT_%s" %lgt)
    
    specSelect = mel.eval("vrayAddRenderElement LightSelectElement;")
    mc.setAttr("%s.vray_type_lightselect" %specSelect, 3)
    specSelect = mc.rename(specSelect, "SPEC_%s" %lgt)
    
    mc.sets(lgt, forceElement="%s" %(lgtSelect), edit=True)
    mc.sets(lgt, forceElement="%s" %(specSelect), edit=True)