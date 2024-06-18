import random
chars="qwertyuio123789654pasdfghklzxcvbnm,.;'/[]}{:;@#$%?1^&*()!~AQWERTYUIOLMNBVCXZDFGHJKL"
length = int (input("Enter length of the password: "))
password=""

for a in range(length):
    password+=random.choice(chars)
    
print(password)    
