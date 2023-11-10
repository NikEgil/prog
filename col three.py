import matplotlib.pyplot as plt
import numpy as np
import os
from scipy import signal
import time


main_folder = r"C:\Users\Nik\Desktop\Projects\programa\data2"
main_folder = main_folder.replace(chr(92), "/")
print(main_folder)
folders_list = np.array(os.listdir(main_folder))
print(folders_list)


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


plt.subplot(111)
# начальное время
start_time = time.time()
for folder in range(len(folders_list)):
    current_folder = main_folder + "/" + folders_list[folder] + "/"
    print(current_folder)
    file_list = np.array(os.listdir(current_folder))

    y = np.zeros(int((end - start) / step))
    x = np.arange(start + step, end, step)
    mas = np.zeros((1, len(x)))
    crit = 0.1

    for file in range(len(file_list)):
        spec = open(current_folder + file_list[file], "r", encoding="utf8")
        spec = spec.read().split(",")
        if file_list[0][-1] == "n":
            for j in range(start_point, end_point):
                y[j - start_point] = float(spec[j + 11])
        else:
            for j in range(start_point, end_point):
                y[j - start_point] = float(spec[j + 11])
        mean = np.mean(y[len(y) - 100 : len(y)])
        y = np.subtract(y, mean)

        if np.max(y) > crit:
            mas = np.append(mas, [y], axis=0)

    a = len(mas) - 1
    print(a)
    mas = np.sum(mas, axis=0)
    mas = np.divide(mas, a)
    mas = signal.savgol_filter(mas, 51, 3)
    plt.plot(x, mas, linewidth=1, label=current_folder)
    plt.legend(loc=1)


end_time = time.time()
elapsed_time = end_time - start_time
print("Elapsed time: ", elapsed_time)

plt.show()
