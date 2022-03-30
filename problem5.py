t = float(input("Enter a temperature: "))
c = input("Convert to (F)ahrenheit or (C)elsius? ")

Tf = 0
if( c == 'C'):
    Tc = (5/9)*(t - 32)
    print(t,"F =",Tc," C")
elif(c == 'F'):
    Tf = (9/5)*t + 32
    print(t, "C =", Tf," F")
else:
    print("다시 입력하십시오.")
