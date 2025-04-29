import random
import string
caracters = string.ascii_letters + string.digits + '!@#%&*'
password = ''.join(random.choice(caracters) for _ in range(10))
print(f"A senha gerada é {password}")