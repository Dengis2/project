#Задача 1
file_1 = open('nginx_logs.txt', 'r', encoding="utf-8")
for line in file_1:
    line = line.replace(' "', ' ')
    line = line.split(" ")
    remote_addr = line[0]
    request_type = line[5]
    requested_resource = line[6]
    result = remote_addr, request_type, requested_resource
    print(result)
file_1.close()

#Задача 3
from itertools import islice, zip_longest
import json

file_1 = open("users.csv", "r", encoding="utf-8")
file_2 = open("hobby.csv", "r", encoding="utf-8")
result_1 = file_1.readlines()
result_2 = file_2.readlines()
result_3 = []
result_4 = []
for line in result_1:
    line = line.split(",")
    line = " ".join(line)
    line = line.replace('\n', '')
    result_3.append(line)
for line in result_2:
    line = line.replace('\n', '')
    result_4.append(line)
result = dict(zip_longest(result_3, result_4, fillvalue='None'))

with open("result.json", "w", encoding="utf-8") as f:
    if result_3 < result_4:
        print(1)
    else:
        json.dump(result, f, ensure_ascii=False)