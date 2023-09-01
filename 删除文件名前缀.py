import os

folder_path = input("输入文件夹路径：")
prefix = input("输入要删除的开头字符串：")

for filename in os.listdir(folder_path):
    if filename.startswith(prefix):
        new_filename = filename[len(prefix):]

        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_filename)

        os.rename(old_path, new_path)
