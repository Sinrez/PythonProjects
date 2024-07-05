import hashlib
# Представим строку в виде байтов
input_bytes = b"backpack"
output = hashlib.sha256(input_bytes)
# Используем hexdigest() для преобразования байтов
print(output. hexdigest())