# Shao_Unity2021_SUNTAIL_Stylized_Fantasy_Village_Optimization

## Unity模型导出导入流程
##### 下图主要是美术需要在建模软件进行导出，并在Unity进行导入相关的流程，导出导入很重要，关乎在Unity的使用是否正常
![](https://upload-images.jianshu.io/upload_images/2356692-0ea173e2327634af.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


---

## DCC工具导出设置
##### Unity 支持多种标准和专有模型文件格式（DCC）。Unity 内部使用 .fbx 文件格式作为其导入链
1. 导出FBX![](https://upload-images.jianshu.io/upload_images/2356692-546e2db6a017d5c4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

---

2. 优化原始导入模型文件，删除不需要的数据
- 统一单位，这样可以保证在DCC中和Unity中的单位统一时也让资源目录难以管理
- 如果需要导入Blend shape normals时，必须指定光滑组Smooth groups，当然也不是任何时候都需要这样
- 建议导出时不携带如摄像机、灯光、材质等场景信息

---

3. 原始模型影响性能点
- 最小化面数，不需要微三角形面(一个三角面包含个位像素)，三角面尽量分布均与
- 合理的拓扑结构与平滑组，尽可能是闭包
- 尽量少的材质个数
- 尽可能少的蒙皮网格
- 导出的网格必须是多边形拓扑，不能是贝塞尔曲线、样条曲线、细分曲面、NURBS([非均匀有理B样条](https://baike.baidu.com/item/NURBS/550944?fr=ge_ala))、NURMS等，因为这些在导入Unity后都不支持
- 在导出之前确保所有变形体(Deformers)都烘培到网格模型上，如骨骼的形变烘培到蒙皮的权重上
- 不建议模型使用的纹理随模型导出，这会降低Unity导入效率，同
- 尽可能少的骨骼数量
- FK与IK节点分离，导出时删除IK骨骼节点

---

4. 模型优化
- 尽可能的将网格合并到一起
- 尽可能使用共享材质
- 不要使用网格碰撞体
- 不必要不要开启网格读写
- 使用合理的LOD级别
- Skin Weights受骨骼影响个过多
- 合理压缩网格
- 不需要rigs和BlendShapes尽量关闭
-  如果可能，禁用法线或切线

---

## 模型导入设置
![](https://upload-images.jianshu.io/upload_images/2356692-d9dce894d038a548.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- Mesh Compression ：一般我们在保证网格准确的情况下，可以启用更激进的压缩方式，可以使网格磁盘空间占用的更小，注意运行时内存不会减少。开启后需要自行测试下
- Read/Write：启动此选项会在内存中额外复制一份此网格，一个副本会保存在内存中，另一个副本会保存在GPU显存中。只有在运行时需要动态修改网格数据时才需要开启此选项。Skinmesh如果绑定骨骼动画也需要开启此选项
- Optimize Mesh/Generate Colliders：一般保持默认，除非需要禁止优化或做网格级碰撞

![](https://upload-images.jianshu.io/upload_images/2356692-8dfdde9f5329e94b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 无动画时，取消勾选ImportAnimation

![](https://upload-images.jianshu.io/upload_images/2356692-40f23286c0114590.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 无附加材质时，选择为None

---

## UPR优化建议
- 检查读/写标志：开启FBX资源的读/写标志会导致双倍的内存占用![](https://upload-images.jianshu.io/upload_images/2356692-1c275ccae79e45a3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- 检查动画资源压缩方式：动画资源使用最佳压缩方式可以提高加载效率，对于不需要动画的模型来说，AnimationType直接选择None![](https://upload-images.jianshu.io/upload_images/2356692-8322ad446170e3ef.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![](https://upload-images.jianshu.io/upload_images/2356692-61ab46b911478163.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- 检查FBX资源顶点数：这个需要根据实际情况和美术沟通![](https://upload-images.jianshu.io/upload_images/2356692-33a3bde666bc03df.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- 检查FBX资源骨骼数：这个需要根据实际情况和美术沟通![](https://upload-images.jianshu.io/upload_images/2356692-5522256592b78cfa.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- 检查动画资源的OptimizeGameObjects选项：如果AnimationType选择的是Humanoid，则应该勾选Optimize Game Objects![](https://upload-images.jianshu.io/upload_images/2356692-3687b012a2767665.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![](https://upload-images.jianshu.io/upload_images/2356692-d6767b2c3f4491be.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

---

## PlayerSetting设置
![](https://upload-images.jianshu.io/upload_images/2356692-4f7fdecf1537e2ff.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- Vertex Compression：设置每个通道的顶点压缩，可为模型除位置、光照贴图、UV之外所有内容启动压缩
- Optimize Mesh Data：可根据网格所启用的材质删除不必要的数据，如材质中没有使用到的切线、法线、颜色以及UV等

---

## Memonry视图

![](https://upload-images.jianshu.io/upload_images/2356692-48edaaabe8c68a45.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- Mesh占用为449.2M







