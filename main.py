#  Задача 1
print ('Задача "Список с визитами"')
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

for visit in geo_logs:
    value = list(visit.values())[0][1]
    if value == 'Россия':
        print(visit)
print()

#  Задача 2
print ('Задача "Уникальные гео-ID"')
ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
my_set = set()
for geo_ids in ids.values():
    my_set |= set(geo_ids)
print(list(my_set))
print()
        
#  Задача 3
print ('Задача "Распределение количества слов в списке"')
queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
    'нетология'
]
number_words = [len(query.split()) for query in queries]
result = dict.fromkeys(set(number_words), 0)
for count_word in result:
    result[count_word] = number_words.count(count_word)
for word in result.items():
    print(f'Запросов с {word[0]} словами(словом) -  {round((word[1] * 100 / len(queries)), 2)}%')
print()

#  Задача 4
print ('Задача "Статистика рекламных каналов по объемам продаж"')
stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
new_stats = sorted(stats.items(), key=lambda x: x[1], reverse=True)
print('Максимальный объем продаж у', new_stats[0][0])
#print(new_stats[0][0])    
print()

#  Задача 5
print ('Задача "Преобразование списка в словарь"')
lst = ['2018-01-01', 'yandex', 'cpc', 100]
lst = list(reversed(lst))
new_dict = lst[0]
for e in lst[1:]:
    new_dict = {e: new_dict}

print(new_dict)
