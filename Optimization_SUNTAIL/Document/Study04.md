# Shao_Unity2021_SUNTAIL_Stylized_Fantasy_Village_Optimization

## UPR优化建议
- 纹理资源大小2的幂次：大小非2的幂次的纹理资源将无法使用ETC1和PVRTC压缩格式。在导入时自动伸缩为2的幂次也可能会导致内存占用或者贴图质量问题。和美术协商按照2的幂次出图![](https://upload-images.jianshu.io/upload_images/2356692-9b3d4784df1e60fa.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- 纹理的原始大小不是2的幂次；导入时自动扩大成2的幂次会导致内存占用上升。和美术协商按照2的幂次出图 ![](https://upload-images.jianshu.io/upload_images/2356692-596be1e8f4838115.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- 纹理的原始大小不是2的幂次；导入时自动缩小成2的幂次可能会影响贴图质量。和美术协商按照2的幂次出图 ![](https://upload-images.jianshu.io/upload_images/2356692-5c659f06d83d0484.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- 纹理资源的读/写标志应被禁用：应禁用不需要读写标志的纹理资源![](https://upload-images.jianshu.io/upload_images/2356692-ba887abe754ba385.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![](https://upload-images.jianshu.io/upload_images/2356692-c9bb32f831575d6b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- 未压缩的纹理应该禁用mipmap：检查Inspector -> Advanced -> Generate Mip Maps选项![](https://upload-images.jianshu.io/upload_images/2356692-aca4c6065a4a9030.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)![](https://upload-images.jianshu.io/upload_images/2356692-5b5fc400ab83adb9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- Android平台纹理压缩格式
带有OpenGLES3或更高版本的Android的纹理格式应该是ASTC![](https://upload-images.jianshu.io/upload_images/2356692-04f930be77fd4850.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)![](https://upload-images.jianshu.io/upload_images/2356692-9c2955d1f817f501.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
对安卓平台使用默认值，但格式不是Automatic![](https://upload-images.jianshu.io/upload_images/2356692-c6b202b1af623777.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)![](https://upload-images.jianshu.io/upload_images/2356692-eccad6d80d787d25.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- 检查纹理资源的过滤模式
纹理的过滤模式一般不建议使用Trilinear，会占用较高的计算资源![](https://upload-images.jianshu.io/upload_images/2356692-a8f78ee872af4caa.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)![](https://upload-images.jianshu.io/upload_images/2356692-6baad97c30487f1f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- 检查纹理资源alpha通道
如果纹理的alpha通道全部为0，或者全部为255，可以认为其中不包含有效信息，此时应禁用'Alpha源'标志，否则会浪费这部分的内存![](https://upload-images.jianshu.io/upload_images/2356692-12342e55a9728a32.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)![](https://upload-images.jianshu.io/upload_images/2356692-7a33fdab42919463.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- 检查纯色纹理
纯色纹理的使用可能可以由一些设置来代替。由于某些情况下纯色纹理是必不可少的，此警告仅会在所使用的纹理较大(大于设定值, 默认为16x16)时才会触发![](https://upload-images.jianshu.io/upload_images/2356692-b683a0431c5f3705.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- 检查重复纹理![](https://upload-images.jianshu.io/upload_images/2356692-f48221f9356e1592.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- 检查纹理是否过大
过大的纹理资源会更多的消耗内存![](https://upload-images.jianshu.io/upload_images/2356692-2fb9fe3723e5b887.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- 检查纹理重复环绕模式
Repeat Wrap模式可能会导致纹理上出现意外的边缘![](https://upload-images.jianshu.io/upload_images/2356692-24557e1345bc4eec.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- 检查精灵图纹理填充率
  填充率是精灵图分割后的有效面积与总面积的比率，较低的精灵图纹理填充率会导致显存的浪费。Custom Parameters: fillRateThreshold : 0.5onlyCheckSprite : True![](https://upload-images.jianshu.io/upload_images/2356692-b235e1827effd664.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

---

## 自定义导入设置
可以看到上文有很多要优化的内容，一个一个找到修改真的费时费力，所以写了一个工具保证了资源的规范性。当然还是有很多不完善的后续一点点补充进来
~~~
using System.IO;
using UnityEditor;
using UnityEngine;

namespace Game.Editor
{
    public class CustomAssetImporter : AssetPostprocessor
    {
        private void OnPreprocessTexture()
        {
            var importer = assetImporter as TextureImporter;

            //设置Read/Write Enabled开关,不勾选
            importer.isReadable = false;

            // Assets/Artworks下是美术库的全部贴图，分门别类的设置不同最大尺寸
            if (assetPath.StartsWith("Assets/Suntail Village/Textures"))
            {
                string fileName = Path.GetFileNameWithoutExtension(assetPath);
                if (fileName.EndsWith("_1024"))
                    importer.maxTextureSize = 1024;
                else if (fileName.EndsWith("_2048"))
                    importer.maxTextureSize = 2048;
                else
                    importer.maxTextureSize = 512;

                var androidSetting = importer.GetPlatformTextureSettings(BuildTargetGroup.Android.ToString());
                androidSetting.maxTextureSize = importer.maxTextureSize;
                if (!IsAllowTextureFormat(androidSetting.format))
                {
                    androidSetting.format = TextureImporterFormat.ASTC_8x8;
                }
                androidSetting.overridden = true;
                importer.SetPlatformTextureSettings(androidSetting);
            }
            // UI大图资源，设置好指定的安卓格式
            if (assetPath.StartsWith("Assets/Main/SpriteBig"))
            {
                var androidSetting = importer.GetPlatformTextureSettings(BuildTargetGroup.Android.ToString());
                androidSetting.maxTextureSize = importer.maxTextureSize;
                if (!IsAllowTextureFormat(androidSetting.format))
                {
                    androidSetting.format = TextureImporterFormat.ASTC_8x8;
                }
                androidSetting.overridden = true;
                importer.SetPlatformTextureSettings(androidSetting);
            }
            if (importer.assetPath.StartsWith("Assets/Main/Sprites"))
            {
                //设置UI纹理Generate Mipmaps
                importer.mipmapEnabled = false;
                //设置UI纹理WrapMode
                importer.wrapMode = TextureWrapMode.Clamp;
            }
        }

        bool IsAllowTextureFormat(TextureImporterFormat format)
        {
            return format == TextureImporterFormat.ASTC_4x4 || format == TextureImporterFormat.ASTC_8x8 || format == TextureImporterFormat.ETC2_RGBA8;
        }
    }
}
~~~

---

## 优化对比
- Memory视图中，Texture2D内存优化了将近300M，如果大家觉得压缩太狠，可以调整合适自己的分辨率![](https://upload-images.jianshu.io/upload_images/2356692-c1bf820c2e3c2771.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- Profiler中整体内存峰值200M，纹理也是显示将近300M的优化![](https://upload-images.jianshu.io/upload_images/2356692-02198f2622b2e989.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)