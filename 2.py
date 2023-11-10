import matplotlib.pyplot as plt
import numpy as np
import os
from scipy import signal

mas = np.ones((1, 5))
print(mas)
a = np.array([1, 2, 3, 4, 5])

mas = np.append(mas, [a], axis=0)
print(mas)
print(np.sum(mas, axis=0))


print(chr(92))


main_folder = r"C:\Users\Nik\Desktop\Projects\programa\data"
main_folder = main_folder.replace(chr(92), "/")
print(main_folder)
folders_list = np.array(os.listdir(main_folder))
print(folders_list)

for a in range(len(folders_list)):
    current_folder = main_folder + "/" + folders_list[a] + "/"
    print(current_folder)
    file_list = np.array(os.listdir(current_folder))
    print(file_list[a][-1])
    print(current_folder + file_list[a])
