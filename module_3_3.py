# Самостоятельная работа по уроку "Распаковка позиционных параметров".
def print_params(a, b, c):
    print(a, b, c)


print_params(1, 'строка', True)
#print_params ()                    проверка без аргументов
#print_params (1)                   проверка с 1 аргументом
#print_params (1, True)             проверка с 2 аргументами
#print_params ( b=25 )
#print_params ( c = [1, 2, 3])

values_list = (2, 'Строка2', False) # создаем список значений
print_params(*values_list)


values_dict = {"a" : "any text", "b" : True, "c" : 427} # Создаем словарь значений

print_params( **values_dict)


values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)