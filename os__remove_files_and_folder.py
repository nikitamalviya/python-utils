import os
import shutil

def remove_files_inside_the_folder(folder):
    for filename in os.listdir(folder):
        # print("filename : ", filename)
        file_path = os.path.join(folder, filename)
        print("file_path : ", file_path)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    os.remove(folder)

folderdata = 'D:\\data'
remove_files_inside_the_folder(folderdata)
