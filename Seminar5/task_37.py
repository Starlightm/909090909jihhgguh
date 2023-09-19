"""
Задача №37. Решение в группах
15 минут
Дано натуральное число N и
последовательность из N элементов.
Требуется вывести эту последовательность в
обратном порядке.
Примечание. В программе запрещается
объявлять массивы и использовать циклы
(даже для ввода и вывода).
Input: 2 -> 3 4
Output: 4 3
"""

# 1230 - 0321

def reverse(num):
    if num < 10:
        return str(num)
    return str(num % 10) + reverse(num // 10)

print(reverse(1230))


"""
'0' + reverse(123)
        |
      '3' + reverse(12)
              |
             '2' + reverse(1)
                     |
                     '1'

"""

