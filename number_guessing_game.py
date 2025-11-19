import random
#generate random number 0-9
rand_num=random.randrange(0,10)

while True:
 user=input('enter guess:  ')
    
 try:
    if user.lower()=='q':
        break
    elif int(user) < rand_num:
        print('too low')
    elif int(user) > rand_num:
         print('too high')     
    else:
         print(f'Congratulations the number is {user}')
         break
 except:
     print('invalid input try again')