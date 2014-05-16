import maya.cmds as mc
import maya.mel as mel

mats = mc.ls(sl=True)
for mat in mats:
    mel.eval("vrayAddRenderElement MaterialSelectElement;")
    matsRE = mc.ls(sl=True)[0]
    mc.connectAttr("%s.outColor" %mat, "%s.vray_mtl_mtlselect" %matsRE, force = True)
    mc.select(matsRE)
    mc.rename(matsRE, "MAT_SELECT_%s" %mat)
    matsRE = mc.ls(sl=True)[0]
    mc.setAttr("%s.vray_explicit_name_mtlselect" %matsRE, matsRE, type="string")
    mc.setAttr("%s.vray_name_mtlselect" %matsRE, matsRE, type="string")