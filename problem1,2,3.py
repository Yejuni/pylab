
def sum(n):
    b = 0
    for i in range(1, n+1):
        b+=i
    return b

def even_sum(n):
    b = 0
    for i in range(1, n+1):
        if i%2==0:
            b+=i
    return b

def factorial(n):
    b = 1
    for i in range(1, n+1):
            b*=i
    return b


n = input("숫자를 입력하시오: ")
print("총 합: ", end='')
print(sum(int(n)))

print("짝수의 합: ", end='')
print(even_sum(int(n)))

print("총 곱: ", end='')
print(factorial(int(n)))
