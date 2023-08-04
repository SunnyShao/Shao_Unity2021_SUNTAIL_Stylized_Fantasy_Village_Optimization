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

---

## 使用Asset Checker 检测Unity工程
>输入命令：assetcheck.exe --project=<project_path> --projectId=<project_id>
project_path替换项目真实路径
project_id替换为UPR后台创建应用后获得的ProjectID
##检测结果
![](https://upload-images.jianshu.io/upload_images/2356692-f22d8dec332d7a79.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

---

## 音乐音效优化
#####音乐音效一般不会成为性能瓶颈，但优化音乐音效可以减少对内存的使用与包体大小

###### 1.0 音频文件类型
- 一般情况下可使用未压缩的wav文件作为音频源文件，通过不同平台支持的压缩格式控制压缩比
- MP3：是一种有损压缩数字音频格式，适用于较长的音效，适合移动平台
- WAV：音质要强于MP3格式，资源大，无压缩音频导入，适用于较短的音效
- OGG：压缩比高，适合人声和适用于较长的音效
- AIFF：无压缩音频导入，适用于较短的音效
---

###### 1.1 UPR资源检测建议。通过下图可以看到，工具检查了84个资源，对其中的75个提出了改进建议
- 音频应该启用forceMono，以节省存储和内存
- default 的短音效应使用DecompressOnLoad
- default 的常规音效应使用CompressedInMemory
- default 的音乐应该使用Streaming
- 默认平台的音频剪辑格式不适用于安卓

![](https://upload-images.jianshu.io/upload_images/2356692-9ccc8068fa992537.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![](https://upload-images.jianshu.io/upload_images/2356692-55346437f47634cc.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![](https://upload-images.jianshu.io/upload_images/2356692-b3af8a7733588d2c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![](https://upload-images.jianshu.io/upload_images/2356692-eb78d50815989532.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

---

###### 1.2 启用Force to Mono
被建议的音频是双声道音频，且左右两声道的音乐完全相同，可以用勾选ForceToMono的方式强制将此音频修改为单声道，内容不丢失的情况下可以减少它的使用内存和大小。特别是在移动平台下几乎听不出任何区别。如果左右声道内容不同，开启ForceToMono会导致听到的声音错误
![](https://upload-images.jianshu.io/upload_images/2356692-2289a58639dd14b0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

---

###### 1.3 音频信息详情
如下图，分别显示的是音频原始资源大小 、资源压缩后的大小 、和整体压缩比 
![](https://upload-images.jianshu.io/upload_images/2356692-29fe39bdac470e1a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

---

###### 1.4 音乐加载类型
- Decompress On Load：该选项一般对应音频压缩后大小<200kb的音效文件。音频文件在加载完毕后，会被全部解压到内存中，这种方式会占据大量的内存，然而在播放时由于音频之前已经被解压，所以其对CPU的开销很小。请注意在加载后解压缩如果是Vorbis编码，会使用它压缩时大约10倍的内存，如果是ADPCM编码大约使用3.5倍的内存，所以请不要降此选项用于大文件
- Compressed In Memory：该选项一般对应音频压缩后大于200kb的音效文件。音频文件以压缩格式存放于内存中，一边播放一边进行解压。这种模式的内存开销会比前一种稍小，但是播放时的CPU开销会较之更大。
- Streaming流加载：该选项一般对应背景音乐文件，或较大较长的音效文件。音频文件不会被加载到内存，只有即将播放的一小段才会被读取到内存中。这种模式的内存开销最低，但是CPU开销也最大，因为其伴随着大量的磁盘读写操作和解压缩，可以避免载入时卡顿
- 此外，当游戏需要静音时，不要将音量设置为0，应该销毁音频audiosource组件把它从内存中完全卸载
- 综上所述，UPR推荐我们不同大小文件要选择好正确的加载类型

![](https://upload-images.jianshu.io/upload_images/2356692-2d6c8840fbd2d0ca.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

--- 

###### 1.5 Compression Format 压缩格式
- PCM：完全不压缩格式，占据的硬盘和内存相对会较大，由于运行时不需要解压，所以它的CPU开销最小，所以非常适合使用在很短的音效上面
- Vorbis/MP3：常见的压缩格式，主流平台全部支持的格式，压缩比较高，但是运行时的解压缩开销较大，对于音质的损耗更加严重，所以多了个Quality可以调节质量改变文件大小1-100。在iOS平台上一般设置为MP3，因为iOS支持MP3格式的硬解码。如果音乐不循环可以使用MP3格式。
- ADPCM：一种古老的压缩格式，相对于PCM的压缩比为3.5:1，但是运行时的解压开销很小，对于音质有一定损耗。这个格式适用于需要大量使用的音效上面，比如脚步 爆破和子弹发射，所以适合简短常用的音效
- **综上所述，URP建议我们在安卓平台修改为Vorbis/MP3格式，在IOS平台修改为MP3格式。音频压缩策略需要考虑不同压缩格式在不同平台下的特点，以及音乐音效文件在不同用途下使用不同的压缩格式**
- 

![](https://upload-images.jianshu.io/upload_images/2356692-855d314c5421c372.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

---

###### 1.6 采样率
- 通常在移动平台都会选择对音质影响最小的最低设置，一般移动平台音频采样率经验数据建议设置为22050Hz。如下图，可以看到该音频源文件的音频采样率是36046Hz，在移动平台上完全没有必要，只会徒增文件大小和内存占用。
![](https://upload-images.jianshu.io/upload_images/2356692-4db2ccc4597a4770.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- 如果要修改默认的音频采样频率，可以通过Sample Rate Setting下拉菜单选择 Override Sample Rate，并修改采样频率为22050Hz。与上面的音频信息对比可以发现导入后的大小也会缩减，越低采样频率生产的音频文件会越小。
![](https://upload-images.jianshu.io/upload_images/2356692-3f5bb0215566e706.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 实际打包对比
- 优化音频前![](https://upload-images.jianshu.io/upload_images/2356692-e75920e3bbcf07c8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- 优化音频后
![](https://upload-images.jianshu.io/upload_images/2356692-614a20cecf1486b1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- 通过图直观看到，优化后内存的占用比之前要少了70兆   ，而Cpu的负载仅提高了3%。这是因为一部分音频loadtype改成了streaming，额外产生了一些cpu开销。与内存方面相比，这个优化是非常值得的。
