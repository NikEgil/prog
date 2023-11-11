import matplotlib.pyplot as plt
import numpy as np
import os
from scipy import signal
import time
import re


def sorting(lest):
    a = np.array(0)
    b = np.array(0)
    print(type(a))
    print(type(b))
    for i in range(len(lest)):
        try:
            a = np.append(a, float(lest[i]))
        except:
            b = np.append(b, lest[i])
    print(type(a))
    print(type(b))
    a = np.sort(a)
    c = []
    for i in range(len(a)):
        c.append(str(a[i]))
    c = c + b
    return c


main_folder = r"C:\Users\Nik\Desktop\prog\data3"
main_folder = main_folder.replace(chr(92), "/")
print(main_folder)
folders_list = np.array(os.listdir(main_folder), dtype=int)
folders_list = np.sort(folders_list)
print(folders_list)
folders_list = np.array(folders_list, dtype=str)

# region переменные
crit = 0.1
# 153 884    измеряемый диапазон. 0-2136 диапазон данных
start = 400  # нм
end = 700  # нм
step = (884 - 153) / 2134

start_point = round((start - 153) / step)
end_point = start_point + int((end - start) / step)

print(step, start_point, end_point)
y = np.zeros(int((end - start) / step))

x = np.arange(start + step, end, step)
# endregion


def open_file(file):
    if file[-1] == "n":
        pass


def get_rmr(spec):
    spec = re.split(",", spec)
    for j in range(start_point, end_point):
        y[j - start_point] = float(spec[j + 11])
    return y


def get_txt(spec):
    spec = re.split("\n|\t", spec)

    for j in range(start_point, end_point - 5):
        y[j - 731] = spec[j * 2 + 15].replace(",", ".")
        # print(y[j - start_point])
    return y


plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
# начальное время
c = 0
start_time = time.time()
for folder in range(len(folders_list)):
    current_folder_path = main_folder + "/" + folders_list[folder] + "/"
    current_folder = folders_list[folder]
    print(current_folder_path)
    file_list = np.array(os.listdir(current_folder_path))

    y = np.zeros(int((end - start) / step))
    x = np.arange(start + step, end, step)
    mas = np.zeros((1, len(x)))
    crit = 0.1
    color_step = 1 / len(folders_list)

    if file_list[0][-1] == "n":
        for file in range(len(file_list)):
            spec = open(current_folder_path + file_list[file], "r", encoding="utf8")
            spec = spec.read()
            y = get_rmr(spec)

            mean = np.mean(y[len(y) - 50 : len(y) - 30])
            y = np.subtract(y, mean)
            if np.max(y) > crit:
                mas = np.append(mas, [y], axis=0)
    elif file_list[0][-1] == "t":
        for file in range(len(file_list)):
            spec = open(current_folder_path + file_list[file], "r", encoding="utf8")
            spec = spec.read()
            y = get_txt(spec)
            mean = np.mean(y[len(y) - 50 : len(y) - 30])
            y = np.subtract(y, mean)
            if np.max(y) > crit:
                mas = np.append(mas, [y], axis=0)

    if len(mas) > 1:
        c = c + 1
        a = len(mas) - 1
        print("number of graphs " + str(a))
        mas = np.sum(mas, axis=0)
        mas = np.divide(mas, a)
        mas = signal.savgol_filter(mas, 51, 3)

        ax.plot(
            x,
            mas,
            linewidth=1.5,
            label=current_folder,
            alpha=0.3,
            color=[0.2, color_step * c, 1 - color_step * c],
        )
        ax.legend(bbox_to_anchor=(1.01, 1), loc="upper left", borderaxespad=0.0)
        fig.canvas.draw()
        fig.canvas.flush_events()
    else:
        print("no graphs")
        pass


end_time = time.time()
elapsed_time = end_time - start_time
print("Elapsed time: ", elapsed_time)
plt.ioff()
plt.show()
