import maya.cmds as mc
import maya.mel as mel

samplerInfo = mc.shadingNode("samplerInfo", asUtility=True)

extraTex = mel.eval("vrayAddRenderElement ExtraTexElement;")
mc.connectAttr("%s.uvCoord.uCoord" %samplerInfo, "%s.vray_texture_extratex.vray_texture_extratexR" %extraTex, force = True)
mc.connectAttr("%s.uvCoord.vCoord" %samplerInfo, "%s.vray_texture_extratex.vray_texture_extratexG" %extraTex, force = True)

mc.setAttr("%s.vray_considerforaa_extratex" %extraTex, 0)
mc.setAttr("%s.vray_filtering_extratex" %extraTex, 0)

name = "UV"
extraTex = mc.rename(extraTex, name)
mc.setAttr("%s.vray_name_extratex" %extraTex, name, type="string")
mc.setAttr("%s.vray_explicit_name_extratex" %extraTex, name, type="string")