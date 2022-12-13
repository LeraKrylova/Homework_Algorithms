#task_1
#Cложность O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = [] #создаем список, в него мы будем класть наши символы
        while head: #проходимся циклом по списку
            l.append(head.val) #добавляем в список символ 
            head = head.next #идем к следующему символу 
        return l == l[::-1] #первый символ равен последнему # возвращаю 
true или false (если палиндром или если нет)
