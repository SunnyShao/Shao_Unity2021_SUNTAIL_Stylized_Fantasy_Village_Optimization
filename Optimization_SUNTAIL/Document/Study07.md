# Shao_Unity2021_SUNTAIL_Stylized_Fantasy_Village_Optimization

## 一、Canvas Batch
一个Canvas绘制Mesh的过程中，如果每个UI元素都绘制一次（DrawCall），则耗时会很长。因此Canvas会先对其UI元素按照材质和渲染顺序排序，将能够一起绘制的UI元素合并到一个Mesh中，然后绘制。这样可以有效减少DrawCall

---

## 二、ReBuild
- ReBuild是Canvns ReBatch过程中完成的

- ReBuild是重建UI元素时的操作，它会改变UI的Mesh信息，进而触发ReBatch。当修改了UI元素的缩放，尺寸，材质，旋转等信息时都会触发重建

*   在WillRenderCanvases事件调用PerformUpdate::CanvasUpdateRegistry接口
    *   通过ICanvasElement.Rebuild方法重新构建Dirty的Layout组件
    *   通过ClippingRegistry.Cullf方法，任何已注册的裁剪组件Clipping Compnents(Such as Masks)的对象进行裁剪剔除操作
    *   任何Dirty的 Graphics Compnents都会被要求重新生成图形元素

*   Layout Rebuild
    *   UI元素位置、大小、颜色发生变化
    *   优先计算靠近Root节点，并根据层级深度排序

*   Graphic Rebuild
    *   顶点数据被标记成Dirty
    *   材质或贴图数据被标记成Dirty

---

## 三、Canvas和Graphic
- Canvas负责管理UGUI元素，负责UI渲染网格的生成与更新，并向GPU发送DrawCall指令
- UI组件的基类是Graphic，Graphic核心是组织Mesh和Material传到底层（CanvasRenderer）
- CanvasRenderer将Mesh和Material传递给Canvas，Canvas做合批。CanvasRenderer的两个核心SetMesh和SetMaterial。每个Graphic有一个CanvasRenderer，保存了保存当前元素的Mesh和材质。一个Graphic为dirty，Canvas就要重新合批![](https://upload-images.jianshu.io/upload_images/2356692-e910242813fc6ec5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

---

## 四、UGUI渲染细节

*   UGUI中渲染是在Transparent半透明渲染队列中完成的，半透明队列的绘制顺序是从后往前画，由于UI元素做Alpha Blend,我们在做UI时很难保障每一个像素不被重画，UI的Overdraw太高，这会造成片元着色器利用率过高，造成GPU负担。
*   UI SpriteAtlas图集利用率不高的情况下，大量完全透明的像素被采样也会导致像素被重绘，造成片元着色器利用率过高；同时纹理采样器浪费了大量采样在无效的像素上，导致需要采样的图集像素不能尽快的被采样，造成纹理采样器的填充率过低，同样也会带来性能问题。

---

## 五、Unity UI性能的四类问题

1.1  Canvas Re-batch 时间过长

- 指Canvas分析其UI节点信息，生成最优批次的过程

- 耗时：节点数量，层级深度，元素重叠，材质数量等

- 触发时机：当Canvas中的UI节点的Mesh改变时（SetActive，transform，颜色……..）

- 触发过程：根据UI元素深度关系进行排序、检查UI元素的覆盖关系、检查UI元素材质并进行合批

- 触发结果：重新Batch一次，无论当前Mesh的改变是否影响了父节点（也就是说一个很小的变化，就会让当前Canvas重新Batch一次）

- 解决方案：
  01)  可以用多个同级Canvas或者Canvas套Cnavas的方法，来将复杂层级划分到不同Canvas中去，需要注意的是每个Canvas都至少有一个DrawCall（当有子UI元素时），这样可能会增加DrawCall 
  02) 使用 动静Canvas分离的方案可以将ReBatch的范围限制在动态Canvas中
  03) 减少层级复杂度，少用嵌套的树形UI结构，同时将材质相同的UI尽量放到同一层级

1.2  Canvas Over-dirty, Re-batch次数过多
- 每当UI元素的Mesh改变时，都会触发ReBatch来重新计算，因此我们要尽量减少UI元素Mesh的改变
- 两个按钮中不叠加时，合批为2![](https://upload-images.jianshu.io/upload_images/2356692-c144ab902b8a4f79.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 当第一个按钮文字和第二个按钮背景重叠时，合批为4![](https://upload-images.jianshu.io/upload_images/2356692-80968826dc284eba.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

1.3  生成网格顶点时间过长
- 可以看到Cumulative Vertex Count数量，越多耗时越久![](https://upload-images.jianshu.io/upload_images/2356692-481bd3c69a9ebb97.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


1.4  片元利用率高 - Fill-rate overutilization 
- 一个像素被多次绘制，称为片元利用率高，一次绘制中，如果一个像素被反复绘制N次，这样会导致GPU利用率过高![](https://upload-images.jianshu.io/upload_images/2356692-8b516e3c587fcd0d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![](https://upload-images.jianshu.io/upload_images/2356692-277e4fea957ee396.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![](https://upload-images.jianshu.io/upload_images/2356692-ff939974c7838f8c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![](https://upload-images.jianshu.io/upload_images/2356692-3567c94c02e7e643.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![](https://upload-images.jianshu.io/upload_images/2356692-5fe167c646d4c884.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

---

## 六、使用Canvas的基本准则：

*   将所有可能打断合批的层移到最下边的图层，尽量避免UI元素出现重叠区域
*   可以拆分使用多个同级或嵌套的Canvas来减少Canvas的Rebatch复杂度
*   拆分动态和静态对象放到不同Canvas下。
*   尽量不使用Layout组件
*   Canvas的RenderMode尽量Overlay模式，减少Camera调用的开销

---

## 七、Raycast优化：

*   必要的需要交互UI组件才开启“Raycast Target”
*   开启“Raycast Targets”的UI组件越少，层级越浅，性能越好
*   对于复杂的控件，尽量在根节点开启“Raycast Target”
*   对于嵌套的Canvas，OverrideSorting属性会打断射线，可以降低层级遍历的成本

---

## 八、UI字体

*   避免字体框重叠，造成合批打断

*   字体网格重建
    *   UIText组件发生变化时
    *   父级对象发生变化时
    *   UIText组件或其父对象enable/disable时

*   TrueTypeFontImporter
    *   支持TTF和OTF字体文件格式导入
  ![](https://upload-images.jianshu.io/upload_images/2356692-0442ce373ccfb21f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

*   动态字体与字体图集

    *   运行时，根据UIText组件内容，动态生成字体图集，只会保存当前Actived状态的 UIText控件中的字符
    *   不同的字体库维护不同的Texture图集
    *   字体Size、大小写、粗体、斜体等各种风格都会保存在不同的字体图集中（有无必要，影响图集利用效率，一些利用不多的特殊字体可以采用图片代替或使用Custom Font，Font Assets Creater创建静态字体资源）
    *   当前Font Texture不包含UIText需要显示的字体时，当前Font Texture需要重建
    *   如果当前图集太小，系统也会尝试重建，并加入需要使用的字形，文字图集只增不减
    *   利用Font.RequestCharacterInTexture可以有效降低启动时间

##  九、UI控件优化注意事项
*   不需要交互的UI元素一定要关闭Raycast Target选 项
*   如果是较大的背景图的UI元素建议也要使用Sprite的九宫格拉伸处理，充分减小UI Sprite大小，提高UI Atlas图集利用率
*   对于不可见的UI元素，一定不要使用材质的透明度控制显隐，因为那样UI网格依然在绘制，也不要采用active/deactive UI控件进行显隐，因为那样会带来gc和重建开销
*   使用全屏的UI界面时，要注意隐藏其背后的所有内容，给GPU休息机会。
*   在使用非全屏但模态对话框时，建议使用**OnDemandRendering**接口，对渲染进行降频。
*   优化裁剪UI Shader，根据实际使用需求移除多余特性关键字。

##  十、滚动视图Scroll View优化
-  使用RectMask2d组件裁剪
- 使用基于位置的对象池作为实例化缓存


## 参考文章
https://zhuanlan.zhihu.com/p/343524911
https://zhuanlan.zhihu.com/p/343978391
