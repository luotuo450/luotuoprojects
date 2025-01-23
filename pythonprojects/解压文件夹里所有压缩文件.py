import os
import zipfile
import rarfile


def extract_all_files(folder_path):
    # 遍历文件夹中的所有文件
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            # 检查文件是否为压缩文件
            if file.endswith(".zip"):
                try:
                    with zipfile.ZipFile(file_path, "r") as zip_ref:
                        zip_ref.extractall(root)
                    os.remove(file_path)
                    print(f"Extracted and removed: {file_path}")
                except Exception as e:
                    print(f"Failed to extract {file_path}: {e}")
            elif file.endswith(".rar"):
                try:
                    with rarfile.RarFile(file_path, "r") as rar_ref:
                        rar_ref.extractall(root)
                    os.remove(file_path)
                    print(f"Extracted and removed: {file_path}")
                except Exception as e:
                    print(f"Failed to extract {file_path}: {e}")
            # 你可以在这里添加对其他压缩格式的支持


if __name__ == "__main__":
    folder_path = input("请输入要处理的文件夹路径：")
    extract_all_files(folder_path)
