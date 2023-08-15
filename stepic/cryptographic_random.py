import os
import secrets

results = os.urandom(10)
# print([hex(b) for b in results])

traffic_lights = ["Red", "Yellow", "Green"]
# print(secrets.choice(traffic_lights))

byte_results = secrets.token_bytes(8)
print(byte_results)

hex_results = secrets.token_hex(8)
print(hex_results)

url_results = secrets.token_urlsafe()
print(url_results)