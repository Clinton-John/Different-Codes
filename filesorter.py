## automatic file sorter where the files ina given folder are sorted into their specific folders depending on their types
# check if there are specific folders, if not create. 
# check on the specific types of each file and save them in their respective directories

import os
import shutil

path = r"C:/Users/hp/Desktop/projects/python/unsorted files/"

file_names = os.listdir(path)

folder_names = ['csv files', 'docx files', 'images']
for loop in range(0,3):
    if not os.path.exists(path + folder_names[loop]):
        os.makedirs(path + folder_names[loop])
    # print(os.path.exists(path + folder_names[loop]))

for file in file_names:
    if ".csv" in file:
        shutil.move(path + file, path + "csv files/" + file)
    elif ".docx" in file:
        shutil.move(path + file, path + "docx files/" + file)
    elif ".jpg" or ".PNG" in file:
        shutil.move(path + file, path + "images/" + file)
    # else :
    #     print("The file type isnt included")