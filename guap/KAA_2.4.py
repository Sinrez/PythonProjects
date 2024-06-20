#вывести сочетания каждого числа из списка [1, 2, 3] с каждым числом из [10, 20, 30]
print(([(i,j) for i in [1, 2, 3] for j in [10, 20, 30]]))
print()

lst = "«радар», «мадам», «утро», «казак», «топот», «стул»".strip() .replace('«', "").replace('»', "").split(', ')
print({word: word == word[::-1] for word in lst})
print()

#второй способ
def is_palindrome(text):
    return text == text[::-1]
print({word: is_palindrome(word) for word in lst})

words = "‘apple’,‘banana’,‘orange’,‘avocado’,‘lime’,‘artichoke’".replace('‘', "").replace('’', "").split(',')
print(*('\n' + word  for word in words if word[0].lower() in 'aeiou'))
print()

print(sorted(set(''.join(['hello', 'world', 'python', 'programming']))))
print()

# второй способ
input_strings = ['hello', 'world','python', 'programming']
print(sorted({char for string in input_strings for char in string}))