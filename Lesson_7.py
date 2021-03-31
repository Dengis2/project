#Задача 7.1
import os
dir_name = 'my_project'
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

subfolder_names = ['settings', 'mainapp', 'adminapp', 'authapp']
for subfolder_name in subfolder_names:
        if not os.path.exists(subfolder_name):
            os.makedirs(os.path.join(dir_name, subfolder_name))

all_folders = [item
for item in os.listdir(dir_name)
if os.path.isdir(os.path.join(dir_name, item))]
print(all_folders)

#Задача 7.4
import os

folder = r'C:\Users\rulsvd\Documents\Работа\Компании\Росгосстрах\Статистика'
size_threshold = [0]
small_files = []
result = []
for i in range(2, 6):
    size_threshold.append(10**i)
for num in size_threshold:
    small_files.append(len([item for item in os.scandir(folder) if item.stat().st_size < num]))
    for i in range(len(small_files)):
        if i == 0:
            result.append(0)
        if i != 0:
            result.append(small_files[i] - small_files[i - 1])
result_1 = [item for item in zip(size_threshold, result)]
for key, val in result_1:
    if key == 100:
        print(f'Тут {val} файлов размером не более {key} байт;')
    if key > 100:
        print(f'{val} файла больше {int(key / 10)}  и не больше {key} байт;')
print(result_1)

#Задача 7.3 (не доделал)
import os
import shutil
from collections import defaultdict
from os.path import relpath
import django

root_dir = r'C:\Users\rulsvd\virt\pythonProject\my_project\templates' #django.__path__[0]
authapp = r'C:\Users\rulsvd\virt\pythonProject\my_project\templates\authapp\base.html'
shutil.copy2(authapp, root_dir)
authapp = r'C:\Users\rulsvd\virt\pythonProject\my_project\templates\authapp\index.html'
shutil.copy2(authapp, root_dir)
mainapp = r'C:\Users\rulsvd\virt\pythonProject\my_project\templates\mainapp\base.html'
shutil.copy2(mainapp, root_dir)
mainapp = r'C:\Users\rulsvd\virt\pythonProject\my_project\templates\mainapp\index.html'
shutil.copy2(mainapp, root_dir)