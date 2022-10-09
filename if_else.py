
# if
celsius = 25
if celsius > 20:
  print('Weather is Good 🟩')
  
  
# if-else  
  
celsius = 18
if celsius > 20:
  print('Weather is Good 🟩')
else:
  print('Weather is Cold ❄️')  
  
  
  
# if--if-else    
celsius = 32
if celsius > 30:
  print('Weather is Hot 🔥')
if celsius > 20:
  print('Weather is Good 🟩')
else: 
  print('Weather is Cold ❄️')
  
  
# if--elif-elif-else     
celsius = 32
 
if celsius > 30:
  print('Hot 🔥')
elif 30 >= celsius > 20:
  print('Good 🟩')
elif -273 < celsius <= 20:
  print('Cold ❄️')
else:
  print('Something went wrong!')
  
  

# Nested conditions  
drivers_licence = False
age = 18
 
if age > 17:
    if drivers_licence:
        print('You can drive car')
    else:
        print('You need to go to a drivers licence course')
else:
    print('You need to get older')