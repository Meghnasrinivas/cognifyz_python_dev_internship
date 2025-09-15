def check_palindrome(str):
    a=str[::-1]
    if a==str:
        print(str,'is palindrome')
    else:
        print(str,'is not a palindrome')

str=input('enter a polindrome string : ')
check_palindrome(str)