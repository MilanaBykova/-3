# TODO Напишите функцию find_common_participants
def find_common_participants(gr1,gr2,x=','):
    gr12=set(gr1.split(x))
    gr22=set(gr2.split(x))
    together=sorted(gr12.intersection(gr22))
    return together

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
itog = find_common_participants(participants_first_group, participants_second_group,'|')
print(itog)
