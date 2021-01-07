#Task 17
def my_func(n):
  sum = 0 
  for i in range (1, n):
    if n%i == 0:
      sum += i
  return sum == n


number = int(input())

print(my_func(number))
