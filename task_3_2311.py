# Сложность O(n)^2

def uniquePathsWithObstacles(obstacleGrid):

    dp = [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))] #создаю матрицу, как сказано в задании 
    dp[0][0] = 1 #1 элемент 

    for i in range(len(obstacleGrid)): #проходимся циклом, по списку 
        for j in range(len(obstacleGrid[0])): #проходимся циклом :)

            if obstacleGrid[i][j] == 1: #если наткнулись на припятсвие, на камень 
                dp[i][j] = 0 # отмечаем, что нашли камень 
            elif i > 0 or j > 0: # если индекс больше 0
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]# то прибавляем кол-во путей в матрицу

    return dp[-1][-1] # выводим последний элемент матрицы
