num1=int(input('enter first number: '))
num2=int(input('enter second number: '))
op=input('enter operetor: ')
if op=='+':
    print('the addition is', num1+num2)
elif op=='-':
    print('the substration is', num1-num2)
elif op=='*':
    print('the multiplication is', num1*num2)
elif op=='/':
    print('the division is', num1/num2)
else:
    print('invalid operator.......try(+,-,*,/)')
