import random
import string

charValue=string.ascii_letters+string.punctuation+string.digits
pass_len = 20
password = "".join([random.choice(charValue) for i in range(pass_len)])
print("Your random password is "+password)
