print('welcome to opolo: ')
print('signin/login: ')
x=input()
if x=='signin' :
    print('firstname: ')
    fn=input()
    print('lastname: ')
    ln=input()
    print('phone number: ')
    pn=input()
    print('state: ')
    st=input()
    print('school: ')
    sc=input()
    print('local government: ')
    lg=input()
    print('email: ')
    em=input()
    print('sex: ')
    sex=input()
    print('age: ')
    age=input()
    print('password: ')
    pw=input()
    print('confirm password: ')
    cp=input()
    if cp=='pw':
elif sex=='m':
    print('welcome mr, +fn')
    print('your username is: +un')
    print('your password is: +cp')
elif sex=='f':
    print('welcome miss, +un')
    print('your username is: +un')
    print('your password is: +cp')
    else:
        print('re-enter password')
        rp=input()
        print('your password is: +rp')
elif x=='login' :
    print('enter username: ')
    eun=input()
    print('enter passworrd: ')
    ep=input()
    print('welcome mr/miss, +un')
else:
    print('confirm paswworrd: ')
    cp=input()
    print('your paswword is: +cpp')
else:
    print('you have to create account')
    print('thank you mr/miss: +sn').


                  number 2
num 1=int(input('enter first number: '))
num 2=int(input('enter second number: '))
op=input('enter operator: ')
if op=='+':
    print('the addition is',num1 + num2)
if op=='-':
    print('the substraction is',num1 - num2)
if op=='*':
    print('the multiplication is',num1 * num2)
if op=='/':
    print('the division is',num1 / num2)
else:
    print('enter valid operator: ')
    evo=input()


              number 3
def Happybirthday(person):
    print('Happy birthday to you! ')
    print('Happy birthday yo you!! ')
    print('Happy birthday, dear'+person)
    print('happy birthday to you!!!')
def main():
    username=input('enter celebrant name: ')
    Happybirthday(username)
main()
        
    
    
