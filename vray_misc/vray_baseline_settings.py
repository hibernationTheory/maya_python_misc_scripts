import maya.cmds as cmds
myRenderer = "vraySettings"

settings = [
("sRGBOn", 1),
("vfbOn", 1),
("globopt_light_doDefaultLights", 0),
("globopt_mtl_limitDepth", 1),
("globopt_mtl_maxDepth", 5),
("samplerType", 1),
#("aaFilterType", 6),
#("aaFilterSize", 2),
("dmcLockThreshold", 1),
("cmap_type", 1),
("cmap_gamma", 2.2),
("cmap_subpixelMapping", 1),
("cmap_adaptationOnly", 1),
("cmap_clampOutput", 1),
("cmap_clampLevel", 6),
("giOn", 1,),
("primaryEngine", 2),
("dmc_depth", 2),
("dmcs_timeDependent", 1),
("ddisplac_maxSubdivs", 4),
("sys_rayc_dynMemLimit", 18000),
("sys_regsgen_xc", 16),
]

for item in settings:
    cmds.setAttr("%s.%s" %(myRenderer, item[0]), item[1])