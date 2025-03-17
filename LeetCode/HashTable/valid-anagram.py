dict_a = {}
dict_b = {}
s = 'anagram'
t = 'nagaram'

for char in s:
    dict_a[char] = dict_a.get(char, 0) + 1  
    
for char in t:
    dict_b[char] = dict_b.get(char, 0) + 1
    
print(dict_a == dict_b)


