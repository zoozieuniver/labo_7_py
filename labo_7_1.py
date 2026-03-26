fib_nums = []
quantity = int(input("Скільки чисел фібоначі ви хочете взнати? "))

def fibonachi(n, how_many_nums):
    if how_many_nums > 2:
        n.insert(0,0)
        n.insert(1,1)
        for i in range( 2 , how_many_nums, 1):
            n.insert(i,n[i-1]+n[i-2])
    elif how_many_nums == 2:
        n.insert(0,0)
        n.insert(1,1)
    else:
        n.insert(0,0)
    return n

fibonachi(fib_nums, quantity)

print("Ось", quantity, "чисел фібоначчі:", fib_nums)


def fib_sum(n, how_many_nums):
    n.clear()
    numbers_for_sum = fibonachi(n, how_many_nums)

    sum_fibonachi=0

    for i in numbers_for_sum:
        sum_fibonachi += i 

    return sum_fibonachi

print("Сума наданих чисел=",fib_sum(fib_nums, quantity))

def fib_even(n, how_many_nums):
    n.clear()
    even_nums = fibonachi(n, how_many_nums)

    for i in range(len(even_nums)-1, -1, -1):
        if even_nums[i] % 2 != 0:
            del even_nums[i]


    return even_nums

print("Парні числа з ваших чисел:", fib_even(fib_nums, quantity))
