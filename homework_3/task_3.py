#task_3
#Сложность O(n^2)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = [root] #создаем очередь 
        l = [] #создает список

        while queue: #проходимся циклом по очереди
            l.append(sum([node.val for node in queue] )/ 
float(len(queue))) #добавляем в список, сумму уровня деленное на 
количество в этом уровне 
            
            new_queue = [] #создаем новую очередь

            for node in queue: #проходимся циклом по очереди 
                if node.left: new_queue.append(node.left) #если в лево, в 
новую очередь добавляем левый символ
                if node.right: new_queue.append(node.right) #если в право, 
в новую очередь добавляем право символ
            queue = new_queue #в простую очередь добавляем значение новой 
очереди
        return l # возвращаем список l
