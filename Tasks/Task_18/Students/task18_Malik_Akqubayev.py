num1 = int(input())
num2 = int(input())
num3 = int(input())
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max_num(num1, num2, num3))
