import uuid

result_uuid4 = uuid.uuid4()
print("UUID4: ")
print(result_uuid4)
print(result_uuid4.hex)
print(result_uuid4.urn)

print("=============================")

result_uuid5 = uuid.uuid5(uuid.NAMESPACE_DNS, "avecoders.com")
print("UUID5: ")
print(result_uuid5)
print(result_uuid5.hex)
print(result_uuid5.urn)

print("=============================")