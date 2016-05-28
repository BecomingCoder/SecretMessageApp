import os


def rename_files():
    # 1 Get file names from a folder
    file_list = os.listdir(r"/Users/hus/Desktop/gitRepos/FullStackNanodegree/SecretMessage/prank")
    # print(file_list)
    saved_path = os.getcwd()
    print("Current working directory is " + saved_path)
    os.chdir(r"/Users/hus/Desktop/gitRepos/FullStackNanodegree/SecretMessage/prank")

    # 2 for each file, rename filename
    for file_name in file_list:
        print("Old Name - " + file_name)
        print("New Name - " + file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, '0123456789'))
    os.chdir(saved_path)

rename_files()
