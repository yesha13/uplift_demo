# string formatting using named indexes



order = 'I want to purchase {amount} {item_name}. The item number is {item_no}. Its price is {cost} rupees.'

print (order.format(amount= "2", item_name= "pen", item_no="5", cost= "20"))






# string formatting using numbered indexes


dog_name= 'loki' #0

name = 'yesha' #1

age = 20 #2

hobbies = 'painting' #3

myself= " My name is {1}. I am {2} years old. I like {3}. I have a dog. Her name is {0}"

print (myself.format(dog_name, name, age, hobbies))

