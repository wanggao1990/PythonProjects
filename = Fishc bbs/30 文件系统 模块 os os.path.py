# 文件系统
import random   
secret = random.randint(1,10)
print(secret)

import os   # 包含子模块 os.path
'''
getcwd()	返回当前工作目录
chdir(path)	改变工作目录
listdir(path='.')列举指定目录中的文件名,结果为list（'.'表示当前目录，'..'表示上一级目录）
mkdir(path)	创建单层目录，如该目录已存在抛出异常
makedirs(path)	递归创建多层目录，如该目录已存在抛出异常，注意：'E:\\a\\b'和'E:\\a\\c'并不会冲突
remove(path)	删除文件
rmdir(path)	删除单层目录，如该目录非空则抛出异常
removedirs(path)递归删除目录，从子目录到父目录逐层尝试删除，遇到目录非空则抛出异常
rename(old, new)将文件old重命名为new
system(command	运行系统的shell命令
walk(top)	遍历top路径以下所有的子目录，返回一个三元组：(路径, [包含目录], [包含文件]) 

os.curdir	指代当前目录（'.'）
os.pardir	指代上一级目录（'..'）
os.sep	输出操作系统特定的路径分隔符（Win下为'\\'，Linux下为'/'）
os.linesep	当前平台使用的行终止符（Win下为'\r\n'，Linux下为'\n'）
os.name	指代当前使用的操作系统（包括：'posix',&nbsp;&nbsp;'nt', 'mac', 'os2', 'ce', 'java'）

basename(path)	去掉目录路径，单独返回文件名
dirname(path)	去掉文件名，单独返回目录路径
join(path1[, path2[, ...]])	将path1, path2各部分组合成一个路径名（中间会加一个sep）
split(path)	分割文件名与路径，返回(f_path, f_name)元组。如果完全使用目录，它也会将最后一个目录作为文件名分离，且不会判断文件或者目录是否存在（以最后一个sep分割）
splitext(path)	分离文件名与扩展名，返回(f_name, f_extension)元组 （若是文件，name为整个字符串，extension为空）
getsize(file)	返回指定文件的尺寸，单位是字节
getatime(file)	返回指定文件最近的访问时间（浮点型秒数，可用time模块的gmtime()或localtime()函数换算）
getctime(file)	返回指定文件的创建时间（浮点型秒数，可用time模块的gmtime()或localtime()函数换算）
getmtime(file)	返回指定文件最新的修改时间（浮点型秒数，可用time模块的gmtime()或localtime()函数换算）

exists(path)	判断指定路径（目录或文件）是否存在（判断目录，后面的sep可有可无）
isabs(path)	判断指定路径是否为绝对路径
isdir(path)	判断指定路径是否存在且是一个目录
isfile(path)	判断指定路径是否存在且是一个文件
islink(path)	判断指定路径是否存在且是一个符号链接（win 快捷方式）
ismount(path)	判断指定路径是否存在且是一个挂载点（win 盘符）
samefile(path1, paht2)	判断path1和path2两个路径是否指向同一个文件
'''
