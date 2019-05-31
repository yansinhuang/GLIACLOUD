def sumOfMultiples(num1, num2, limit):
    sum = 0
    for i in range(limit):
        if i%num1 == 0 or i%num2 == 0:
            sum += i
    return sum


print(sumOfMultiples(3, 5, 1000))