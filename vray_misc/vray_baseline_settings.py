import maya.cmds as cmds
myRenderer = "vraySettings"

settings = {"sRGBOn":(1,),
"vfbOn":(1,),
"globopt_light_doDefaultLights": (0,),
"globopt_mtl_limitDepth": (1,),
"globopt_mtl_maxDepth": (5, ("globopt_mtl_limitDepth",)),
"samplerType": (1,),
"aaFilterType": (6,),
"aaFilterSize": (2,),
"dmcLockThreshold": (1, ("samplerType",)),
"cmap_type": (1,),
"cmap_gamma": (2.2,),
"cmap_subpixelMapping": (1,),
"cmap_adaptationOnly": (1,),
"cmap_clampOutput": (1,),
"cmap_clampLevel": (6, ("cmap_clampOutput",)),
"giOn": (1,),
"primaryEngine": (2, ("giOn",)),
"dmc_depth": (2, ("giOn",)),
"ddisplac_maxSubdivs": (4,),
"sys_rayc_dynMemLimit": (26000,),
"sys_regsgen_xc":(16,),
"dmcs_timeDependent":(1,),
}

for item in settings.iteritems():
    if len(item[1]) == 1:
        cmds.setAttr("%s.%s" %(myRenderer, item[0]), item[1][0])
    else:
        dependency = item[1][1][0]
        dependencyValue = settings[dependency][0]
        cmds.setAttr("%s.%s" %(myRenderer, dependency), dependencyValue)
        cmds.setAttr("%s.%s" %(myRenderer, item[0]), item[1][0])