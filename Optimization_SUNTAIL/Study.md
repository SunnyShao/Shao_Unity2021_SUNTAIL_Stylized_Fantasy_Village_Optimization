# Shao_Unity2021_SUNTAIL_Stylized_Fantasy_Village_Optimization
优化大纲

一、熟悉项目，查看项目资源构成
    1. 看材质、模型、纹理、音视频、字体、shader、逻辑脚本
    2. 看场景中的灯光(数量会光照复杂度和阴影复杂度)
    3. 看场景中的相机(数量会影响整体渲染流程的复杂度)

二、对应平台设置
    Quality设置
    1. 看编辑器平台设置和目标优化平台设置的差异
    2. 渲染管线在目标平台的设置主要看使用到管线的类型，以及使用了哪些RenderFeature，开启了哪些中间纹理和管线内置功能
       例) 比如 SuntailUniversalRenderPipelineAsset_Renderer 中的 RenderingPath 设置成了延迟渲染(Deferred)，可能会给移动平台带来带宽和显存的压力

三、运行时信息