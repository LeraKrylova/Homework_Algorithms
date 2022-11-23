# Сложность 2 * (O(n) * O(m)).

def countSquares(matrix):
    count = 0 # создаем счетчик, который равен #чтобы считать сколько у нас есть квадратов в матрице.
    
    for i in range(len(matrix)): #проходимся циклом, итым элементом по длине матрицы 
        for j in range(len(matrix[0])): # проходимся циклом по каждому элементу 

            if matrix[i][j] == 1: #проверяем на маленькие квадраты(то есть, каждая единица - это маленький квадрат)
                count += 1 
            if i == 0 or j == 0: #если символы равны нулю, идем дальше и ищем квадраты 
                continue
            
            matrix_ = matrix[i][j] #к переменной присваиваем матрицу 
            matrix[i][j] = min(matrix[i - 1][j - 1], matrix[i][j - 1],matrix[i - 1][j]) + 1 if matrix[i][j] == 1 else 0
            #в 23 строке, мы считаем квадраты вокруг маленьких квадратов(маленькие квадраты - это просто единицы)(средние квадраты)
            count = count + matrix[i][j] - matrix_ #находим один большой квадрат(он состоит из маленьких и средних квадратов)

    return count #выводим счетчик 