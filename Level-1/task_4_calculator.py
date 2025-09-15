def calculator():

    print('\n______Simple Calculator________\n')
    num1=float(input('Enter first number : '))
    op=input('Enter an operation (+ , -  , * , /) : ')
    num2=float(input('Enter second number : '))
    if op=='+':
        print('Result : ',num1+num2)
    elif op=='-':
        print('Result : ',num1-num2)
    elif op=='*':
        print('Result : ',num1*num2)
    elif op=='/':
        if num2!=0:
          print('Result : ',num1/num2)     
        else:
          print('Error: Division by zero')
    else:
        print('Invalid operation')

calculator()
