import maya.cmds as mc
import maya.mel as mel

samplerInfo = mc.shadingNode("samplerInfo", asUtility=True)

extraTex = mel.eval("vrayAddRenderElement ExtraTexElement;")
mc.connectAttr("%s.pointWorld" %samplerInfo, "%s.vray_texture_extratex" %extraTex, force = True)
mc.setAttr("%s.vray_considerforaa_extratex" %extraTex, 0)
mc.setAttr("%s.vray_filtering_extratex" %extraTex, 0)

name = "PWORLD"
extraTex = mc.rename(extraTex, name)
mc.setAttr("%s.vray_name_extratex" %extraTex, name, type="string")
mc.setAttr("%s.vray_explicit_name_extratex" %extraTex, name, type="string")