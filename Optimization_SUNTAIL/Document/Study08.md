# Shao_Unity2021_SUNTAIL_Stylized_Fantasy_Village_Optimization

## 一、Unity中的物理解决方案

*   Box2D
*   Nvidia PhysX
*   Unity Physics (基于DOTS)
*   Havok Physics for Unity

---

## 二、碰撞矩阵
- 删除不必要的碰撞矩阵![](https://upload-images.jianshu.io/upload_images/2356692-4c655d46d543e1f5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

---

## 三、Physics设置

- Auto Sync Transform：在Transform组件发生改变时，强制进行物理系统同步。相当于在修改Transform后，立即执行一次对物理对象的模拟更新，这样会增加物理运算覆盖，一般不开启。不开启不代表不更新，一般等到FixedUpdate的过程再更新

- Reuse Collision Callbacks：尽量开启，在物理引擎对所有碰撞进行回调时，会重用之前的Collision碰撞结果的实例，而不会为每个碰撞回调重新创建碰撞结果的实例，由于大多数情况碰撞结果实例只是数值上的变化，重用已经碰撞好的碰撞结果实例，可以降低托管堆上的GC开销

![](https://upload-images.jianshu.io/upload_images/2356692-926751666ee6b9e3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

---

## 四、Unity中的物理组件Collider部分的优化

*   Trigger与Collider
    *   Trigger对象的碰撞会被物理引擎所忽略，通过OnTriggerEnter/Stay/Exit函数回调
    *   Collider对象由物理引擎触发碰撞，通过OnCollisionEnter/Stay/Exit函数回调
    *   Trigger对象不需要RigidBody组件，Collider对象必须至少有一个Collider对象有RigidBody组件
    *   Trigger对象更高效

*   尽量少使用MeshCollider，可以用简单Collider代替，即使用多个简单Collider组合代替也要比复杂的MeshCollider来的高效
*   MeshCollider是基于三角形面的碰撞
*   MeshCollider生成的碰撞体网格占用内存也较高
*   MeshCollider即使要用也要尽量保障其是静态物体
*   可以通过PlayerSetting选项中勾选Prebake Collision Meshes选项来在构建应用时预先Bake出碰撞网格。
![](https://upload-images.jianshu.io/upload_images/2356692-30221be3b442f98f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 五、Unity中的物理组件RigidBody部分的优化

*   Kinematic与RigidBody
    *   Kinematic对象不受物理引擎中力的影响，但可以对其他RigidBody施加物理影响。
    *   RigidBody完全由物理引擎模拟来控制，场景中RigidBody数量越多，物理计算负载越高
    *   勾选了Kinematic选项的RigidBody对象会被认为是Kinematic的，不会增加场景中的RigidBody个数
    *   场景中的RigidBody对象越少越好

## 六、Unity中的RayCast与Overlap部分的优化

*   Unity物理中RayCast与Overlap都有NoAlloc版本的函数，在代码中调用时尽量用NoAlloc版本，这样可以避免不必要的GC开销
*   尽量调用RayCast与Overlap时要指定对象图层进行对象过滤，并且RayCast要还可以指定距离来减少一些太远的对象查询
*   此外如果是大量的RayCast操作还可以通过RaycastCommand的方式批量处理，充分利用JobSystem来分摊到多核多线程计算。
