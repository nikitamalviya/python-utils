import textwrap
 
mystring = '123456789abcdefghijkl'

print(textwrap.wrap(mystring, 4))

n = 4
# using list comprehension 
sentences = [mystring[i * n:(i + 1) * n] for i in range((len(mystring) + n - 1) // n )] 
print("sentence 1 : ", sentences) 
