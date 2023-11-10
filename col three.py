import matplotlib.pyplot as plt
import numpy as np
import sys
import os
import statistics as st
from scipy import signal

main_folder = r"C:\Users\Nik\Desktop\Projects\programa\data"
main_folder = main_folder.replace(chr(92), "/")
print(main_folder)
folders_list = np.array(os.listdir(main_folder))
print(folders_list)
size = 1  # кол-во графиков
s = 0  # начальный файл
# 153 884    измеряемый диапазон. 0-2136 диапазон данных
start = 400  # нм
end = 700  # нм
step = (884 - 153) / 2134

start_point = round((start - 153) / step)
end_point = start_point + int((end - start) / step)

print(step, start_point, end_point)

plt.subplot(111)

s = 0
for k in range(4):
    pf = main_folder + "/set" + str(k) + "/"
    file_list = np.array(os.listdir(pf))
    n = len(file_list)
    print(n)
    y = np.zeros(int((end - start) / step))
    x = np.arange(start + step, end, step)
    mas = np.zeros((1, len(x)))
    crit = 0.1
    for i in range(len(file_list)):
        spec = open(str(pf + file_list[i]), "r", encoding="utf8")
        spec = spec.read().split(",")
        for j in range(start_point, end_point):
            y[j - start_point] = float(spec[j + 11])
        mean = np.mean(y[len(y) - 150 : len(y) - 100])
        y -= mean
        if np.max(y) >= crit:
            s += 1
            mas = np.append(mas, [y], axis=0)
    a = len(mas)
    mas = np.sum(mas, axis=0)
    mas /= len(mas)
    mas = signal.savgol_filter(mas, 51, 3)
    plt.plot(x, mas, linewidth=1, label=str(str(k + 17) + " " + str(a)))
    plt.legend(loc=1)


plt.show()
