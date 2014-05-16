import maya.cmds as mc
import maya.mel as mel


dirt = mc.shadingNode("VRayDirt", asTexture=True)
txtPlacement = mc.shadingNode("place2dTexture", asTexture=True)
mc.connectAttr("%s.outUvFilterSize" %txtPlacement, "%s.uvFilterSize" %dirt)

#dirt settings
mc.setAttr("%s.subdivs" %dirt, 12)

extraTex = mel.eval("vrayAddRenderElement ExtraTexElement;")
mc.connectAttr("%s.outColor" %dirt, "%s.vray_texture_extratex" %extraTex, force = True)
mc.setAttr("%s.vray_considerforaa_extratex" %extraTex, 0)

name = "OCCLUSION"
extraTex = mc.rename(extraTex, name)
mc.setAttr("%s.vray_name_extratex" %extraTex, name, type="string")
mc.setAttr("%s.vray_explicit_name_extratex" %extraTex, name, type="string")