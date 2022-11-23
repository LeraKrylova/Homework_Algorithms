# Сложность O(n)

def getMaximumGenerated(n):

    if n <= 1:
        return n

    nums = [0, 1] #как сказано в задании создаем список последовательностей 
    count = 1 #создаем переменную, чтобы потом узнать максимум

    for i in range(2, n + 1): #проходимся циклом, не учитывая первый элемент, до n 
        if i % 2 == 0: #если i четное, то добавляем число из списка nums с индексом i//2
            nums.append(nums[i // 2])
        else:
            nums.append(nums[i // 2] + nums[i // 2 + 1]) # если i не четное, то добавляем сумму чисел из списка nums с индексами i // 2 и i//2 + 1
        count = max(count, nums[-1])

    return count 
