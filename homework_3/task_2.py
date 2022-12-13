#task_2
#Сложность O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result = 0 #создаем счетчик 
        while head: #проходимся циклом по списку
            result = (2 * result) + head.val # результат будет равен, 2 
умноженное на данный результат и прибавить символ
            head = head.next #идем к следующему элементу
        return result #возвращаем 


