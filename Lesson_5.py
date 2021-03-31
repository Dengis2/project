<<<<<<< HEAD
Home Work Lesson 5
=======
# 1 Задача
def odd_nums(num):
    for num in range(1, num + 1, 2):
        yield num
odd_to_15 = odd_nums(15)
print(*odd_to_15, sep=', ')

#or
num_gen = (num for num in range(1, 15 + 1, 2))
print(next(num_gen), next(num_gen), next(num_gen), next(num_gen), next(num_gen), next(num_gen), next(num_gen), next(num_gen), next(num_gen))

# 3 Задача
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']
if len(tutors) != len(klasses):
    klasses.append(None)

#List Comprehensions
result_com = [item for item in zip(tutors, klasses)]
print(type(result_com), result_com)

from itertools import islice
#Generator
def result_gen():
    for item in zip(tutors, klasses):
        yield item
result = result_gen()
print(type(result), *islice(result, 7))

# 4 Задача
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result_1 = []
for i in range(len(src)-1):
    if src[i+1] > src[i]:
        result_1.append(src[i+1])
print(result_1)

# 5 Задача
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result_uniq = set()
result_all = set()
for el in src:
    if el not in result_all:
        result_uniq.add(el)
    else:
        result_uniq.discard(el)
    result_all.add(el)
result_finish = [el for el in src if el in result_uniq]
print(result_finish)
>>>>>>> 5e84c58 (HW_Lesson_5)
