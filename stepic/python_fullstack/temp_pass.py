import secrets
import string

def generate_temp_password(number_of_characters=8):
    char_pool = string.ascii_letters + string.digits + "+=?/!@#$%*"
    result = ''.join(secrets.choice(char_pool) for i in range(number_of_characters))
    return result

print(generate_temp_password(10))

def generate_perm_password(number_of_characters=8):
    char_pool = string.ascii_letters + string.digits + "+=?/!@#$%*"
    while True:
       result = ''.join(secrets.choice(char_pool) for i in range(number_of_characters))

       if (any(c.isupper() for c in result) and any(c.isdigit() for c in result)):
           break
    return result

print(generate_perm_password(10)) 

result_url = "http://www.example.com?reset="
result_url += secrets.token_urlsafe(15)
print(result_url)


