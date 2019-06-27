# password basic

password = '12345'
userinput = ''

while userinput != password:
    userinput = input('Inser your password : ')
    if userinput != password:
        print('Wrong password! Please enter the right password')
    else:
        print('Login success!')


