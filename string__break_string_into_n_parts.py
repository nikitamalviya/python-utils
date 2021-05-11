import textwrap
 
mystring = '123456789abcdefghijkl'

print(textwrap.wrap(mystring, 4))

len_of_substring = 4

# using list comprehension 
sentences = [mystring[i * len_of_substring:(i + 1) * len_of_substring] for i in range((len(mystring) + len_of_substring - 1) // len_of_substring )] 
print("sentence 1 : ", sentences) 
