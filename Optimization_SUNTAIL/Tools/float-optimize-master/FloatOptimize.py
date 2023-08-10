import re
import os
import sys
from ModeModule import ModeBase, ModeDirectory, ModeFiles
from Tools import loadConfig,readLines


configStr ='''{
    "mode": "files",
    "precision": 5,
    "mode_files": {
        "projectpath": "F:/UnityProjectPath/",
        "filespath": "files.txt"
    },
    "mode_directory": {
        "directorypath": "F:/UnityProjectPath/samefloder",
        "include": [
            "anim",
            "playable"
        ]
    }
}
'''

helpinfo = '''\nHELPINFO:
use 'FloatOptimize.exe generate-config' to create Config.json
use 'FloatOptimize.exe run' to runing tool\n'''

# 优化一个文件
def optimizeFile(file, precision,back): 

    file = file.replace('\\',"/") 
    if os.path.exists(file)== False:
        if back :
            print("\rWARNING:",file,"is no exists!")
        else:
            print("WARNING:",file,"is no exists!")
        return False
    tag:bool = False # 标记这个文件是否修改过 
    old_lines =readLines(file)

    writeFile = open(file, "w", newline='\n')
    new_lines =[]
    for l in old_lines:  # 读取文件中的每一行
        line = l.rstrip()   # 对于读取到的每一行，去除行尾的换行符
    
        words = line.split(' ')     # 使用"空格"作为分隔符，分隔行内容
        for word in words:
            # 匹配科学计数法
            reg = re.match("-?\d[\.][\d]+[Ee]-?[\d]+", word) 
            if reg:
                    value = reg.group(0) # 获得匹配后的字符串
                    floatValue = float(value)
                    new_lines.append(word.replace(value, str(round(floatValue, 4))))
                    if tag == False :
                        tag = True
        
            else:
                match = re.match("-?\d+\.{1}\d{5,}", word)    # 对于分隔后的每一个内容，使用正则表达式查询是否包含浮点数据，这里只匹配只有一个“.”的，避免有些把字符串的当作浮点型来处理

                # 如果包含浮点数据，则使用四舍五入法保留小数点3位。如果不包含浮点数据，则直接写入到输出文件
                if match:
                    value = match.group(0) # 获得匹配后的字符串
                    floatValue = float(value)
                    new_lines.append(word.replace(value, str(round(floatValue, precision))))
                    if tag == False :
                        tag = True
                else:
                    new_lines.append(word)
    
            if word != words[-1]:
                new_lines.append(' ')
    
        new_lines.append('\n')
    writeFile.writelines(new_lines)
    writeFile.close()
    return tag


def optimize():
    back = False
    try:
        config =  loadConfig()
        if config == None:
            print("Error:no Config.json use 'FloatOptimize.exe generate-config' to create Config.json")
            return

    except FileExistsError:
        print("Error:no Config.json use 'FloatOptimize.exe generate-config' to create Config.json")
        return

    print('\n开始 处理模式：{}'.format(config['mode']))

    precision = config['precision']
    mode: ModeBase
    if config['mode'] == "files":
        mode = ModeFiles(config['mode_files']) 
    elif config['mode'] == "directory":
        mode = ModeDirectory(config['mode_directory']) 
    else:
        print("Config Error,no {} mode,Valid values are files or directory".format(config['mode']))
        return

    # 开始优化
    file_list = mode.getFilesPath()

    if len(file_list) == 0:
        print('没有可处理的文件，完成！')
        return

    print('预处理文件个数：'+ str(len(file_list)) ,end='\n')
    
    pro = 0 # 进度计数
    change = 0 # 更改文件的计数
    for p in file_list:
        pro+=1
        if optimizeFile(p,precision,back):
            change +=1
        print('\r进度:{:.0%} \t处理个数({})\t修改个数({})'.format(pro/len(file_list),pro,change), end='', flush=True)
        back = True
       
    print('\n结束!\n')


        
def main(argv):
    if argv == 'generate-config': # 创建配置文件
            f=open('Config.json','w')
            f.write(configStr)
            f.close()
            print ('generate Config.json complete')
            sys.exit()
    elif argv == '-h' or argv=='--help':
        print (helpinfo)
        sys.exit()
    elif argv == 'run':
        optimize()
        sys.exit()
    else:
        print (helpinfo)
        sys.exit()
  
   
if __name__=='__main__':
    if len(sys.argv) !=2 :
         print (helpinfo)
         sys.exit()
    main(sys.argv[1])


