import maya.cmds as mc
import maya.mel as mel

re_dict = {"diffuseChannel": ("DIFFUSE", "rawdiffuse",),
"reflectChannel" : ("REFLECTION", "reflect",),
"refractChannel" : ("REFRACTION", "refract",),
"sampleRateChannel" : ("SAMPLE_RATE", "sampleRate",), 
"selfIllumChannel": ("SELF_ILLUM", "selfIllum",),
"shadowChannel" : ("SHADOW", "shadow",),
"specularChannel": ("SPECULAR", "specular",),
"lightingChannel" : ("LIGHTING", "lighting",),
"giChannel" : ("GI", "gi",),
"rawGiChannel" : ("RAW_GI", "rawgi",),
"rawLightChannel" : ("RAW_LIGHTING", "rawlight",),
"reflectionFilterChannel" : ("REFLECTION_FILTER", "reflectionfilter",),
"rawReflectionChannel" : ("RAW_REFLECTION", "rawreflection",),
"refractionFilterChannel" : ("REFRACTION_FILTER", "refractionfilter",),
"rawRefractionChannel" : ("RAW_REFRACTION", "rawrefraction",),
"matteShadowChannel" : ("MATTE_SHADOW", "matteshadow",),
"normalsChannel" : ("NORMALS", "normals",),
"bumpNormalsChannel" : ("BUMP_NORMALS", "bumpnormals",),
"zdepthChannel" : ("ZDEPTH", "zdepth",),
 "FastSSS2Channel" : ("SSS", "sss",)
}
 
x = cmds.ls(type="VRayRenderElement")
for i in x:
    cmds.delete(i)

for item in re_dict.iteritems():
    mel.eval("vrayAddRenderElement %s;" %item[0])
    selected = mc.ls(sl=True)[0]
    mc.rename(selected, item[1][0])
    selected = mc.ls(sl=True)[0]
    print selected
    if selected == "ZDEPTH":
        cmds.setAttr("%s.vray_depthClamp" %(selected), 0)
        cmds.setAttr("%s.vray_depthWhite" %(selected), 1)
    cmds.setAttr("%s.vray_name_%s" %(selected, item[1][1]), item[1][0], type="string")