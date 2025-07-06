world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}

world_champions['2022'] = 'Аргентина' # Добавили год и страну в словарь
for key, values in world_champions.items(): # вывели на экран всех чемпионов
    print(key, '-', values)

country = 'Италия'
if country in world_champions.values():  # Проверка страны
    print(f'{country} cтановилась чемпионом мира по футболу в 21 веке!')
else:
    print(f'{country} не выигрывала чемпионат мира по футболу в 21 веке.')