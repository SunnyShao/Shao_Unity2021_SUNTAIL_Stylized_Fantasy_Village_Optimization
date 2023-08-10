# FloatOptimize

## 介绍

FloatOptimize(浮点型优化)用于优化Unity项目中的资源文件.

动画曲线精度过高会增加动画占用内存; 此规则仅面向以文本格式序列化的*.anim文件中的浮点精度.

什么是文本格式序列化的*.anim文件？

能够用记事本打开的，非二进制文件，如你看到的应该是YAML文件（**有些同样是.anim结尾的文件，但是它们是二进制文件，不能使用这个工具来优化**）

用文本编辑器打开.anim动画文件，修改如下文本中 ```value: 0.0023443000120``` 的浮点精度，保留5位小数，手动一个个改是不现实的，因此开发此工具批量修改。

```yaml
%YAML 1.1
%TAG !u! tag:unity3d.com,2011:
--- !u!74 &7400000
...
  m_FloatCurves:
  - curve:
      serializedVersion: 2
      m_Curve:
      - serializedVersion: 2
        time: 0
        value: 0
        inSlope: 0
        outSlope: 0
        tangentMode: 0
   m_Curve:
      - serializedVersion: 2
        time: 0
        value: 0.0023443000120
        inSlope: -0.0064123000001
        outSlope: -0.0066
        tangentMode: 0
```

## 注意事项

该工具可修改：普通数值类型和科学计数类型
但是在优化 playable 类型的文件时，由于timeline的文件格式就是 playable，在配置timelines时，应注意不要配置类似小数类型的字符串：如：0.1、0.2、12.103231等，可能会被工具当作小数来优化


## 快速开始

该工具需用命令行运行，步骤如下
- 使用命令创建配置文件
- 打开配置文件修改
- 使用命令运行工具

### 创建配置文件

在工具根目录下，打开cmd命令工具，使用命令 ```FloatOptimize.exe generate-config``` 创建配置文件
创建成功后，在根目录下生成 ```Config.json``` 文件

### 修改配置文件

修改根目录下的配置文件 **Config.json**，配置优化的规则

* 模式配置(mode)，支持**files** 和 **directory** 两种模式
  * filles：文件模式，通过直接配置要处理的文件的路径来处理
  * directory：目录模式，通过配置Unity项目中某个文件夹的路径，处理该文件夹下所匹配的文件
* 精度(precision)：优化的精度，保留小数点位数
* files模式的配置
  * projectpath ：项目工程路径，项目路径+文件相对路径=文件的绝对路径
  * filespath：存储文件路径的文本的路径，工具读取这个路径，获取内容，内容就是文件的相对路径，每行为一个文件的路径。详细见path.text,
* directory模式的配置
  * directorypath：Unity项目中某个文件夹的绝对路径，处理这个文件夹所有的匹配的文件（这种比较慢）
  * include：匹配的后缀, 如anim, playable

```json
{

    "mode": "files",//模式
    "precision": 5, //优化精度，保留小数点位数
   
     // files 模式的配置
    "mode_files": {
        "projectpath": "D:/UnityProject/",//工程路径
        "filespath": "path.text"//保存路径文本的路径

    },

    // 目录模式的配置
    "mode_directory": {
        "directorypath": "D:/animation", //项目中文件夹的路径
        "include": ["anim", "playable"]// 匹配后缀, 如anim, playable
    }
}

```

path.text：存储要优化文件的路径，通过Unity 优化工具 UPR,我们很容易得到要优化的路径，只需要复制保存即可。

```text
Assets\Animation\role.anim
Assets\Animation\enem.anim
Assets\Animation\anim1.anim
Assets\Animation\anim2.anim
Assets\Animation\anim3.anim
Assets\Animation\anim4.anim
Assets\Animation\anim5.anim
Assets\Animation\anim6.anim

```

### 运行


使用的命令 ```FloatOptimize.exe run``` 运行

