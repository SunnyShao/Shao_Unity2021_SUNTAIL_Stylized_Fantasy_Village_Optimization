# Shao_Unity2021_SUNTAIL_Stylized_Fantasy_Village_Optimization

## 前言
本系列文章结合一款实际项目进行优化，毕竟纸上得来终觉浅。
文章包含自我整理好的大纲和结合实际项目的数据来进行学习验证

## 优化大纲(持续完善)
#### 一 、熟悉项目，查看项目资源构成
- 看材质、模型、纹理、音视频、字体、shader、逻辑脚本
- 看场景中的灯光(数量会光照复杂度和阴影复杂度)
- 看场景中的相机(数量会影响整体渲染流程的复杂度)

#### 二 、对应平台设置
- Quality设置
    1) 看编辑器平台设置和目标优化平台设置的差异
    2) 渲染管线在目标平台的设置主要看使用到管线的类型，以及使用了哪些RenderFeature，开启了哪些中间纹理和管线内置功能
       >比如 SuntailUniversalRenderPipelineAsset_Renderer 中的 RenderingPath 设置成了延迟渲染(Deferred)，可能会给移动平台带来带宽和显存的压力
       ![](https://upload-images.jianshu.io/upload_images/2356692-ae8564ea15d82733.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### 三 、运行时信息
- 电脑启动游戏查看Status信息：场景平均面数、面数峰值、渲染批次
>平均三角形面数(trils)：1.5M-2M  
            面数峰值: 2.3M 
            渲染批次(Batches): 1500 - 1800
            SetPass calls：200多
>![](https://github.com/SunnyShao/Shao_Unity2021_SUNTAIL_Stylized_Fantasy_Village_Optimization/assets/21049639/9d19325b-3fd4-4f56-836f-0a2f9eb0b6e3)


- 手机启动游戏查看信息：
>生成的APK大小621M
            小米MIX4手机平均FPS 15FPS
            小米MIX4手机内存 1.31GB
            小米MIX4手机纹理资源 444M
            小米MIX4手机Mesh 449M
            小米MIX4手机音效 76M
>![](https://github.com/SunnyShao/Shao_Unity2021_SUNTAIL_Stylized_Fantasy_Village_Optimization/assets/21049639/df22624c-3f96-4f9c-8d7e-2bc0c58744dc)
