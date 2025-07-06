times = ['1h 45m', '360s', '25m', '30m 120s', '2h 60s']
count = 0  #создали счетчик минут

for time in times:       # рассмотрим поочередно каждый элемент списка
    t = time.split(' ')  # преобразуем каждый элемент первоначального списка в список с разделением пробелом
    for time_byte in t:  # расмотрим каждый элемент h m s и переведем в минуты
        if 'h' in time_byte:
            count += 60 * int(time_byte.replace('h', ''))
        if 'm' in time_byte:
            count += int(time_byte.replace('m', ''))
        if 's' in time_byte:
            count += int(time_byte.replace('s', '')) / 60
 
print("Общее количество минут:", int(count))