department="computer"
txt = "My name is vijay, and I am {}" #The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} 
print(txt.format(department))


matrial = "icecream"
pdid=1
price = 78
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(matrial,pdid, price))