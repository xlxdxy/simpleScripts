import os

folder_path_list = ["C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs", os.environ['APPDATA'] + "\\Microsoft\\Windows\\Start Menu\\Programs"]
uninstall_files = []

for folder_path in folder_path_list:
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.startswith("卸载") or file.startswith("Uninstall"):
                uninstall_files.append(os.path.join(root, file))
                print(os.path.join(root, file))

if len(uninstall_files) == 0:
    print("没有找到以 卸载 或 Uninstall 开头的文件")
else:
    choice = input("是否要删除这些文件？(y/n): ")
    if choice.lower() == "y":
        for file in uninstall_files:
            os.remove(file)
            print(f"{file} 已删除")
