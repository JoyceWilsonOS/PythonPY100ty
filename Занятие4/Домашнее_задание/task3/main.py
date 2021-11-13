# """Напишите программу Python для разделения заданного словаря списков на список словарей с помощью функции map().
# Пример:
# INPUT:  {"Наука": [88, 89, 62, 95], "Язык": [77, 78, 84, 80]}
#
# OUTPUT: [{'Наука': 88, 'Язык': 77}, {'Наука': 89, 'Язык': 78}, {'Наука': 62, 'Язык': 84}, {'Наука': 95, 'Язык': 80}]
# """
#
#
# def divide_func(some_tup):
#     some_dict = {some_tup[0]: some_tup[1]}
#     current_dict = {}
#     current_list = []
#     for key, value in some_dict.items():
#         current_dict[key] = value[0]
#         current_list = [key, value[0]]
#         break
#     return current_list
#
#
# def make_dict_from_lists(list_of_lists):
#     output_list_final_2 = []
#     for el in list_of_lists:
#         new_dict = {}
#         for elem in el:
#             new_dict[elem[0]] = elem[1]
#         output_list_final_2.append(new_dict)
#     return output_list_final_2
#
#
# if __name__ == "__main__":
#     # Write your solution here
#     incoming_dict = {"Наука": [88, 89, 62, 95, 80], "Язык": [77, 78, 84, 80, 789]}
#     print(f'incoming_dict {incoming_dict}')
#     #  Тут получаем количесво численых показателей - ти есть количество итераций
#     list_ = [k for k in incoming_dict.values()]
#     num_of_iterations = len(list_[0])
#
#     #  Создаем пустой список, через map создаем вложеные списки пар всех ключей с первыми элементами, потом 2ми и тд
#     output_list = []
#     for i in range(num_of_iterations):
#         output_list.append(list(map(divide_func, incoming_dict.items())))
#         for v in incoming_dict.values():
#             v.pop(0)
#     print(f'output_list {output_list}')
#     output_list_final = make_dict_from_lists(output_list)
#     print(f'output_list_final {output_list_final}')
#     pass
#
#
# def list_of_dicts(marks):
#     # print(marks)
#     list_ = []
#     for key, value in marks.items():
#         print(f'key, value, {key, value}')
#         for val in value:
#             print(f'val, {val}')
#             list_.append((key, val))
#     print(f'tul_, {list_}')
#     print()
#     print(*zip(*list_))
#
#     result = map(dict, zip(*[[(key, val) for val in value] for key, value in marks.items()]))
#
#     return list(result)
#
#
# if __name__ == "__main__":
#     marks = {'Наука': [88, 89, 62, 95], 'Язык': [77, 78, 84, 80]}
#
#     print(marks)
#
#     print(list_of_dicts(marks))


# def list_of_dicts(marks):
#     vals = zip(*[marks[k] for k in marks])
#     result = [dict(zip(marks, v)) for v in vals]
#     return result

def list_of_dicts(marks):
    vals = zip(*[marks[k] for k in marks])
    result = [dict(zip(marks, v)) for v in vals]
    return result

if __name__ == "__main__":
    marks = {'Наука': [88, 89, 62, 95], 'Язык': [77, 78, 84, 80]}
    # print(marks)
    print('2', list_of_dicts(marks))

