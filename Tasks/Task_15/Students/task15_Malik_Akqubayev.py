n = input()

reversed_n = n[::-1]
result = ""
for i in range(0, len(reversed_n), 3):
    result += reversed_n[i:i+3] + ","
result = result[::-1]
print(result.strip(','))
