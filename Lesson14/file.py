
lst = [
    'Андрей Говорухин                              2   9   2   9   5   5   7   6  10   7   10  8',
    'Василий Петров                                5   3   10  7   7   7   7   9   4   5   8   2',
    'Гавриил Варфоломеев                           8   2   4   6   8   10  1   7   9   10  1   6',
    'Игнат Тюльпанов                               9   3   10  6   9   6   10  5   10  1   5   8',
    'Илья Муромцев                                 7   3   8   8   2   9   1   7   5   4   10  5',
    'Кощей Бессмертный                             6   5   1   1   9   7   2   3   2   5   3   9',
    'Максим Мухин                                  8   2   3   5   10  4   6   7   6   9   6   6',
    'Маргарита Мартынова                           8   9   9   10  6   5   10  6   3   3   5   4',
    'Пётр Николаев                                 10  2   8   8   7   1   6   9   4   7   10  9',
    'Полина Гусева                                 10  5   9   4   6   3   4   4   9   10  7   7',
    'Спиридон Тереньтьев                           9   5   1   2   5   2   10  2   7   2   4   7',
    'Станислав Твердолюбов                         3   6   4   3   3   4   4   10  5   3   5   5'
]

file = open('pupils_list.txt', 'w', encoding='utf-8')
file_w = open('pupils_list_2.txt', 'w', encoding='utf-8')
for line in lst:
    file.write(line)
    file.write('\n')

lst = []
file = open('pupils_list.txt', encoding='utf-8')
lines = file.readlines()
total_sum = 0
total_cnt = 0
for line in lines:
    lst = line.strip('\n').split()
    name = lst[0]
    surname = lst[1]
    suma = sum([int(s) for s in lst[2:]])
    total_sum += suma
    cnt = len(lst[2:])
    total_cnt += cnt
    file_w.write('{name:<32}{avr:>7}\n'.format(
        name=lst[1] + ' ' + lst[0][0] + '.',
        avr=round(suma/cnt, 2)))

    if suma/cnt < 5:
        print('{name:<32}{avr:>7}'.format(
            name=lst[1] + ' ' + lst[0][0] + '.',
            avr=round(suma/cnt, 2)))

print('Средний балл по классу:', round(total_sum/total_cnt, 2))
























#
#
# # lst_name[i], k
#     #     print(lst_name[0], lst_marks[0])
#     # q = [sum(marks_int)/len(marks_int)]
#     # lst2 = list(map(list(zip(lst_name, q), lst_name)))
#
#     # print(lst2)
# # # print(lst_name[0],lst_name[3])
# # for _ in lst_name:
# #     # marks = lst_marks[idx].split()
# #     # idx += 1
# #     lst_surname = lst_name[idx].split()
# #     idx += 1
# #     # print('lst_surname.split(' ') - ', end='')
# #     print(lst_surname)
#
#     # s = s[::-1]
#     # print('s[::-1]- ', end='')
#     # print(s)
#     #
#     # s = ' '.join(s)
#     # print("' '.join(s) - ", end='')
#     # print(s)
#     # # lst_surname = ' '.join(lst_name[idx].split(' ')[::-1])
#     # # idx += 1
#     # print(lst_surname)
#
#
#
#
#
#
#
#
#
#     # print(marks[2])
#     # marks = marks.split()
#     # print(marks)
#     # for j in marks:
#     #     q = [int(x) for x in marks]
#     #     j += 1
#     # print(q)
# # for i in lst_marks:
# #     marks = lst_marks[i]
# #     for _ in lst_marks[i]:
# #         marks = lst_marks[marks].split()
# #         # lst_marks[i] += lst_marks[i+1]
# #     print(marks)
# #
# # q = list(map(lambda x: int(x) for x in lst), lst_marks))
#
#     # [int(x) for x in lst[1:: 2].split()]
# # marks = lst[1:: 2]
# # print(marks)
#
# # for idx in lst:
# #     while idx ==1 or idx ==3 or idx==5:
# #         idx = [int(x) for x in lst[idx].split()]
# #         # lst = lst.split()
# #         # idx = [int(x) for x in lst]
# #         # idx += 1
# #     print(idx, type)
# # print(lst)
# # # lst1 = list(int(lst[1]), lst))
# # # print(lst1)
# # lst1 = list(map())
# # lst1 = [x for x in lst if not int(x)%2]
# # print(lst1)
#
# # print(lst[0],lst[1])
# # lst_int = list(map(lambda ))
# # print(lst_int)
#
# # q = lst[1].split()
# # q = [int(x) for x in q]
# #
# # print(q, sum(q), sum(q)/len(q))