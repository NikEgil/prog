import matplotlib.pyplot as plt
import numpy as np
import os

mas = np.ones((1, 5))
print(mas)
a = np.array([1, 2, 3, 4, 5])

mas = np.append(mas, [a], axis=0)
print(mas)
print(np.sum(mas, axis=0))


print(chr(92))


path_folder = r"C:\Users\Nik\Desktop\Projects\programa\data2"
path_folder = path_folder.replace(chr(92), "/")
print(path_folder)
file_list = np.array(os.listdir(path_folder))
print(file_list)
