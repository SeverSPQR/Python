from math import factorial
'''class Solution:
    """
      На входе массив
      Возвращаемое значение: нет
      """
    def reverse_string(self, s):
        list(''.join(s)[::-1])

    """
    На вход массив чисел и целевое значение
    На выходе массив из двух индексов
    """
    def two_sum(self, nums, target):
        length = len(nums)
        for i in range(length):
            if target - i in nums:
                return [i, nums.index[target - i]]


    """
    Функция принимает на вход n (int)
    Возвращает int
    """

    def climb_stairs(self, n):
        DoubleStepAmount = n // 2
        StepAmount = n // 2 + 1
        OptionAmount = 0
        while DoubleStepAmount != 0:
            OptionAmount += (factorial(StepAmount))/(factorial(DoubleStepAmount)*factorial(StepAmount-DoubleStepAmount))
            ++StepAmount
            --DoubleStepAmount
        return OptionAmount'''

def climb_stairs(n):
    DoubleStepAmount = n // 2
    StepAmount = n // 2 + (n % 2)
    OptionAmount = 0
    while DoubleStepAmount != 0:
        OptionAmount += (factorial(StepAmount)) / (
                    factorial(DoubleStepAmount) * factorial(StepAmount - DoubleStepAmount))
        StepAmount += 1
        DoubleStepAmount -= 1
    OptionAmount += 1
    return OptionAmount


