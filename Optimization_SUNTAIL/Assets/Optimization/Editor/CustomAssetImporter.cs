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
            if (assetPath.StartsWith("Assets/Artworks"))
            {
                // 特效贴图
                if (assetPath.StartsWith("Assets/Artworks/VFX"))
                {
                    string fileName = Path.GetFileNameWithoutExtension(assetPath);
                    if (fileName.EndsWith("_1024"))
                        importer.maxTextureSize = 1024;
                    else if (fileName.EndsWith("_512"))
                        importer.maxTextureSize = 512;
                    else
                        importer.maxTextureSize = 256;
                }
                // 场景贴图
                else if (assetPath.StartsWith("Assets/Artworks/Scenes"))
                {
                    importer.maxTextureSize = 1024;
                }
                else
                {
                    string fileName = Path.GetFileNameWithoutExtension(assetPath);
                    if (fileName.EndsWith("_1024"))
                        importer.maxTextureSize = 1024;
                    else
                        importer.maxTextureSize = 512;
                }

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