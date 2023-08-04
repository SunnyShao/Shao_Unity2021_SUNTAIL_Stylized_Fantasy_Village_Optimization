# Shao_Unity2021_SUNTAIL_Stylized_Fantasy_Village_Optimization

## UPR Asset Checker 介绍
- **看下去，很简单**
- 用于本地资源检测，帮助开发者尽早发现资源文件中存在的问题
- 支持所有版本的Unity项目
- 不依赖Unity Editor，无需安装绿色运行
- 检测速度极快，可在UPR中查阅检测结果
- 支持命令行模式，可与CI/CD工具轻松集成，实现自动化检测
- 规则库持续更新
- 支持AssetBundle冗余检测
- 支持静态代码分析

---

## 获取Asset Checker
- [下载Unity资源检测工具](https://upr.unity.cn/instructions/assetchecker#UserManual)
- 下载到一个压缩包，解压缩即可![](https://upload-images.jianshu.io/upload_images/2356692-dabbb8d2ec12c5d3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 命令行窗口访问到这个解压缩后的目录，然后使用**assetcheck.exe -h**查看帮助信息(爱看不看)![](https://upload-images.jianshu.io/upload_images/2356692-758b102e242c9821.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 生成配置文件(爱生不生)
> assetcheck.exe generate-config
![](https://upload-images.jianshu.io/upload_images/2356692-2b670b5cafc7c0a7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
