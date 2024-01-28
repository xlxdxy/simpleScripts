import os

folder = r"D:\My\Downloads\Edge"
postfix = " (Z-Library)"

for fullFileName in os.listdir(folder):
    filePath = os.path.join(folder, fullFileName)
    if not os.path.isfile(filePath):
        continue
    fileName, extension = os.path.splitext(fullFileName)
    if fileName.endswith(postfix):
        newFileName = fileName[:-len(postfix)]
        newFullFileName = newFileName + extension
        newFilePath = os.path.join(folder, newFullFileName)
        os.rename(filePath, newFilePath)
        print(f"已重命名成 {newFullFileName}")