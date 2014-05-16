import maya.cmds as mc
import maya.mel as mel

velocity = mel.eval("vrayAddRenderElement velocityChannel;")
mc.setAttr("%s.vray_clamp_velocity" %velocity, 0)
mc.setAttr("%s.vray_filtering_velocity" %velocity, 0)

name = "VELOCITY"
velocity = mc.rename(velocity, name)
mc.setAttr("%s.vray_filename_velocity" %velocity, name, type="string")