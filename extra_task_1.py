types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}
tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
} 

def del_doubles(tickets):
    sum_list = tickets[1]  # временный суммирующий список для контроля всех дубликатов
    for i in range(1,6):
        values_unique = list(dict.fromkeys(tickets[i]))  # удаление дубликатов в списке
        tickets[i] = values_unique # перезапись только уникальные значения
    for j in range(2,6):
        values_unique = []
        for v in tickets[j]:
            if v not in sum_list:
                values_unique.append(v)
        tickets[j] = values_unique # перезапись только уникальные значения
        sum_list += values_unique 
    return tickets
  

def merge_tickets(types, tickets):
    tickets_by_type = {}
    for k in range(1,6):
        tickets_by_type[types[k]] = tickets[k]
    return tickets_by_type


tickets = del_doubles(tickets)
tickets_by_type = merge_tickets(types, tickets)
for key, values in tickets_by_type.items(): print(key, ':', values)  