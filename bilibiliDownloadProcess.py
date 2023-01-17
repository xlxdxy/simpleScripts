'''
批量处理从 哔哩哔哩UWP 下载下来的剧集，更改文件让普通播放器也能播放并且重命名和保存到其他位置。
'''

import os

basePath = r'D:\My\Videos\bilibili\ss28510'
savePath = r'D:\Temp\aaa'

with open(basePath+r'\desktop.ini', 'r') as f:
    for line in f.readlines():
        if line[:7] == 'InfoTip':
            seriesName = line[8:]
            print(f'剧集标题是 {seriesName}')
            break

folders = [f for f in os.listdir(basePath) if os.path.isdir(os.path.join(basePath,f))]
folders = [os.path.join(basePath,f) for f in folders]

for folder in folders:
    with open(folder+r'\desktop.ini', 'r') as iniFile:
        for line in iniFile.readlines():
            if line[:7] == 'InfoTip':
                episodeName = line[8:-1]
                print(f'现在处理的集是 {episodeName}')
                break
    for fileName in os.listdir(folder+r'\1'):
        if fileName[-3:] == 'mp4':
            with open(folder+'\\1\\'+fileName, 'rb') as mp4File:                          
                start = mp4File.read(3)
                if start == b'\xff\xff\xff':
                    with open(savePath+'\\'+episodeName+'.mp4', 'wb') as newMp4File:
                        newMp4File.write(mp4File.read())