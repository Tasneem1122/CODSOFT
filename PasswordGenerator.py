import random
import string
print('Password generator!')
length = int(input('\nEnter the length of password: '))
lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation
all = lower + upper + numbers + symbols
temp = random.sample(all,length)
password = "".join(temp)
all = string.ascii_letters + string.digits + string.punctuation
password = "" .join(random.sample(all,length))
print(password)
