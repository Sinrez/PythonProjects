import os

curr_dir = os.getcwd()
for c in os.listdir(curr_dir):
    if os.path.isfile(c):
        print(c)