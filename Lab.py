import sys

Child = 6.0
Adult = 10.0
Older = 7.0

print()
print('                 - WELCOME TO TUWIAQ CINEMA - ')
print('-'*65)

print()
Age = int(input('ENTER YOUR AGE: '))
# Condition for invalid age entered from the user .
if Age < 0:
  print('INVALID NUMBER!')
  sys.exit()

print()
Day = input('WHICH DAY DO YOU PREFER TO WATCH YOUR FAVORITTE MOVIE ?: ')
# Condition for invalid day enterd from the user .
Valid_Days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
if Day not in Valid_Days:
  print('INVALID DAY!')
  sys.exit()

# Age Conditions
if Age < 5 :
  TicketPrice = 0.0 # It revert to (Free ticket) condition
elif 5 <= Age <= 12 : 
  TicketPrice = Child
elif 13 <= Age <= 59 :
  TicketPrice = Adult
else :
  TicketPrice = Older

# if the user age are less than 5 years old, the ticket are free.
if TicketPrice == 0.0 :
  print('WELCOME, YOUR TICKET IS FREE')
  print()


# Condition for an extre $2 charge for everyone select Friday to visit the cinema .
if Day == 'Friday':
  TicketPrice += 2.0
  print('AN EXTRA $2 HAS BEEN ADDED TO YOUR TICKET')
  print()


Discount = input('ARE YOU STUDENT? (Yes/No): ')
# Condition for insure that the user are student or not, if yes he will get 20% discount .
if Discount == 'Yes':
  DiscountAmount = TicketPrice * 0.20
  TicketPrice -= DiscountAmount
  print(f'NICE!, YOU GOT A 20% DISCOUNT (-${DiscountAmount:.2f})' )
  print()

print(f'YOUR FINAL TICKET PRICE FOR {Day}: ${TicketPrice:.2f}')


