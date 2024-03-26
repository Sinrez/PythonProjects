import sys

def longest_unique_substring(s):
    if not s:
        return 0
    
    max_length = 0
    start = 0
    char_index_map = {}
    
    for i, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1
        else:
            max_length = max(max_length, i - start + 1)
        
        char_index_map[char] = i

    return max_length

if __name__ == '__main__':
    arr = sys.stdin.readline().rstrip()
    print(longest_unique_substring(arr))