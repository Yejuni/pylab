import random
a = 1
b = 0

while True:
    operand1 = (random.randint(1, 10))
    operand2 = (random.randint(1, 10))

    q=print("%d X %d"%(operand1,operand2))
    u=int(input("정답: "))
    if (u == (operand1 * operand2)):

        b+=1

    d = input("Y || N?")
    if d =="Y":
        a+=a
        continue
    elif d =="N":
        print("정답률:%d" %(b / a * 100))
        break