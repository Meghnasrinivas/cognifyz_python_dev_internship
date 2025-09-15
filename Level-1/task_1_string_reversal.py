
#Task-1

def reverse_str(text):
    return text[::-1]

while True:
    user_input=input('Enter a String : ')
    str_reverse=reverse_str(user_input)
    print(str_reverse)


    decision=input('Do you want to enter another string? (yes/no):').strip().lower()
    if decision !='yes':
        print('Goodbye...')
        break