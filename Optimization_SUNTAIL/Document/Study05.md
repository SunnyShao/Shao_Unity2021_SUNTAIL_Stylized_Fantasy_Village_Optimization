# Shao_Unity2021_SUNTAIL_Stylized_Fantasy_Village_Optimization

## 一、模型Rig标签
![](https://upload-images.jianshu.io/upload_images/2356692-6c8efe36196216bc.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

1. Animation Type
    - None 无动画
    - Legacy 旧版动画，不要用
    - Generic 通用骨骼框架
    - Humanoid 人形骨骼框架
    
2. Animation Type选择原则
      - 无动画选择None
      - 非人形动画选择Generic
      - 人形动画
            人形动画需要Kinematices或Animation Retargeting功能，或者没有有自定义骨骼对象时选择Humanoid Rig
            其他都选择Generic Rig，在骨骼数差不多的情况下,Generic Rig会比Humanoid Rig省30%甚至更多的CPU的时间。 

3. Skin Weights
    默认4根骨头，但对于一些不重要的动画对象可以减少到1根，节省计算量

4. Optimize Bones
     建议开启，在导入时自动剔除没有蒙皮顶点的骨骼

5. Optimize Game Objects
    在Avatar和Animatior组件中删除导入游戏角色对象的变换层级结构，而使用Unity动画内部结构骨骼，消减骨骼transform带来的性能开销。可以提高角色动画性能, 但有些情况下会造成角色动画错误，这个选项可以尝试开启但要看表现效果而定。注意如果你的角色是可以换装的，在导入时不要开启此选项，但在换装后在运行时在代码中通过调用AnimatorUtility.OptimizeTransformHierarchy接口仍然可以达到此选项效果
---

## 模型Animation标签
![](https://upload-images.jianshu.io/upload_images/2356692-65135b5071bcc48e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- Resmple Curves
  将动画曲线重新采样为四元数数值，并为动画每帧生成一个新的四元数关键帧，仅当导入动画文件包含尤拉曲线时才会显示此选项

- Anim.Compression
  Off：不压缩,质量最高，内存消耗最大
  Keyframe Reduction：减少冗余关键帧，减小动画文件大小和内存大小
  Keyframe Reduction and Compression：减小关键帧的同时对关键帧存储数据进行压缩，只影响文件大小
  Optimal：仅适用于Generic与Humanoide动画类型，Unity决定如何进行压缩

- Animation Custom Properties
  导入用户自定义属性，一般对应DCC工具中的extraUserProperties字段中定义的数据

---

## 动画曲线数据信息
![](https://upload-images.jianshu.io/upload_images/2356692-a54611c9ce579d81.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- Curves Pos：位置曲线
- Quaternion：四元数曲线 Resample Curves开启会有
- Euler：尤拉曲线
- Scale：缩放曲线
- Muscles：肌肉曲线，Humanoid类型下会有
- Generic：一般属性动画曲线，如颜色，材质等
- PPtr：精灵动画曲线，一般2D系统下会有
- Curves Total：曲线总数（数值越大性能越差）
- Constant：优化为常数的曲线
- Dense：使用了密集数据（线性插值后的离散值）存储
- Stream：使用了流式数据（插值的时间和切线数据）存储

>优化建议
看效果差异（与原始制作动画差异是否明显）
看曲线数量（总曲线数量与各种曲线数显，常量曲线比重大更好）
看动画文件大小（以移动平台为例，动画文件在小几百k或更少为合理，查过1M以上的动画文件考虑是否进行了合理优化）
---

## UPR优化建议
- 检查动画曲线精度：动画曲线精度过高会增加动画占用内存; 此规则仅面向以文本格式序列化的*.anim文件中的浮点精度
Custom Parameters: precision : 5
 > 用文本编辑器打开.anim动画文件，修改m_EditorCurves::curve::m_Curve下的float值的精度。建议用脚本直接将此文件中所有float精度都调小。

![](https://upload-images.jianshu.io/upload_images/2356692-e695c031e306d821.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![](https://upload-images.jianshu.io/upload_images/2356692-ed674322b770cde2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

--- 

## 动画曲线精度优化工具
介绍：通过上文看到一个个的去修改动画文件里的值不太现实，所以提供了一个动画曲线精度优化工具给大家使用
GitHub地址：[动画曲线精度优化工具](https://github.com/SunnyShao/Shao_Unity2021_SUNTAIL_Stylized_Fantasy_Village_Optimization/tree/master/Optimization_SUNTAIL/Tools/float-optimize-master)
使用方式：配置好 Config.json 后双击 Run.bat 即可
使用后效果：
![](https://upload-images.jianshu.io/upload_images/2356692-5317c8cde5b7bf7f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)