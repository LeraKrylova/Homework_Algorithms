#Сложность O(n)
#N не равен 0, значит, проверяем четное ли это число или нет.
#Если четное то делим на два и прибавляем к счетчику 1.
#Если не четное то вычитаем из N 1 и все равно к счетчику 1. 
#Потом возращаем количество шагов. Запускаем функцию 

def numberOfSteps(n): 
    result = 0 # создаем счетчик, который равен нулю.
    while n: # далее пишем функцию 
        if n % 2 == 0: # если n четное то 
            n = n // 2 # делим его на два 
            result += 1 # прибавляем к счетчику один 
        else: # иначе 
            n -= 1 # вычитаем из n 1 
            result += 1 # прибавляем к счетчику 1
    return result # выводим результат 


print(numberOfSteps(14))