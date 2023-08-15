def valid_rgb(rgb):
    #check if rgb input tuple is within 0-255 
    for val in rgb:
        if not 0 <= val <= 255:
            return False
    return True


# print(valid_rgb((255, 100, 255)))
# print(valid_rgb((255, 100, 256)))

def valid_rgb(rgb):
    #check if rgb input tuple is within 0-255 
    valid = [
             0 <= val <= 255
             for val in rgb
    ]
    return all(valid)

# print(valid_rgb((255, 100, 255)))
# print(valid_rgb((255, 100, 256)))


def valid_rgb(rgb):
    #check if rgb input tuple is within 0-255 
    return all(
            0 <= val <= 255
            for val in rgb
    )

# print(valid_rgb((255, 100, 255)))
# print(valid_rgb((255, 100, 256)))


def contains_numbers(input):
    for char in input:
        if char.isdigit():
            return True
    return False

print(contains_numbers('one is done'))
print(contains_numbers('1 is done'))

def contains_numbers(input):
    return any(char.isdigit()
        for char in input
        )

print(contains_numbers('one is done'))
print(contains_numbers('1 is done'))  