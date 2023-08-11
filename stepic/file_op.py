
fp = open("test.txt", "w")
fp.write("test test test\n")
fp.close()

with open("test.txt", "r") as fp:
    data = fp.read()
    print(data)

with open("test.txt", "a+") as fp:
    fp.write("added more tests\n")
    fp.seek(0)
    data = fp.read()
    print(data)