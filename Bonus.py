Weight = float(input('Enter you weight please: '))
Height = float(input('Enter you height please: '))

BMI = Weight / (Height ** 2)

if BMI < 18.5 :
  print('Your BMI is below 18.5, which is classified as underweight. Every small step toward better health matters. Keep nourishing your body and building strength!')

elif 18.5 < BMI < 24.5 :
  print('Your BMI is between 18.5 and 24.9, which is considered a healthy weight range. Great job! Keep maintaining your healthy habits and taking care of yourself.')

elif 25.0 < BMI < 29.9 :
  print('Your BMI is between 25.0 and 29.9, which is classified as overweight. Every journey starts with one step. Stay consistent, make healthy choices, and believe in yourself!')

else :
  print('Your BMI is 30.0 or higher, which is classified as obesity. It is never too late to start! Focus on progress, not perfection, and celebrate every step toward a healthier you.')
