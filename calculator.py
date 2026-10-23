sign = input('Choose an operation:\n(+,-,/,*,%): ')
num1 = float(input('Dear user , enter first number: '))
num2 = float(input('Dear user , enter second number: '))

if sign == '+':
    print(num1 ,'+' ,num2, '=',num1+num2)
elif sign == '-':
    print(num1, '-', num2 ,'=',num1-num2)
elif sign == '/':
    if num2 != 0 :
        print(num1 ,'/' ,num2 ,'=',num1/num2)
    else:
        print('Error')
elif sign == '*':
    print(num1, '*' ,num2 ,'=',num1*num2)
elif sign == '%':
    if num2 != 0 :
        print(num1 ,'%', num2 ,'=',num1%num2)
    else:
        print('Error')
else:
    print('Dear user,please enter one of the operators in the front')
