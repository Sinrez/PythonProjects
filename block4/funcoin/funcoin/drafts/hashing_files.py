from hashlib import sha256

with open("cape-town-original.jpg", "rb") as file1:
    hash1 = sha256(file1.read()).hexdigest()

with open("cape-town-modified.jpg", "rb") as file1:
    hash2 = sha256(file1.read()).hexdigest()

print()
print(f"Hash исходного оригинального файла: {hash1}")
print()
print(f"Hash измененного файла: {hash2}")