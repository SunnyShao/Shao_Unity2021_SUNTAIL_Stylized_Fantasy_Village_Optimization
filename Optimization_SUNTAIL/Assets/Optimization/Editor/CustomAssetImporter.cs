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

            //����Read/Write Enabled����,����ѡ
            importer.isReadable = false;

            // Assets/Artworks�����������ȫ����ͼ�����ű�������ò�ͬ���ߴ�
            if (assetPath.StartsWith("Assets/Artworks"))
            {
                // ��Ч��ͼ
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
                // ������ͼ
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
            // UI��ͼ��Դ�����ú�ָ���İ�׿��ʽ
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
                //����UI����Generate Mipmaps
                importer.mipmapEnabled = false;
                //����UI����WrapMode
                importer.wrapMode = TextureWrapMode.Clamp;
            }
        }

        bool IsAllowTextureFormat(TextureImporterFormat format)
        {
            return format == TextureImporterFormat.ASTC_4x4 || format == TextureImporterFormat.ASTC_8x8 || format == TextureImporterFormat.ETC2_RGBA8;
        }
    }
}