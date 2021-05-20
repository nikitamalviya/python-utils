import string

# replace any char
my_str = my_str.replace('/', '')

# slicing operation
str_ = "helloworld"
print(string1[:-3]) # str_='hellowor' # ignore last 3 chars
print(string1[-3:]) # str_='ld' # take last 3 chars only
print(string1[::-1]) # str='dlrowolleh # reverse sstring

# check only characters
isalpha_status = str_.isalpha()
# check only numbers 
isnumeric_status = str_.isnumeric()
# check combo of numbers and chars, false if any special char present 
isalnum_status = str_.isalnum()

# check special chars
invalidcharacters= set(string.punctuation) # special characters
if any(char in invalidcharacters for char in ocr_string):
    specialcharstatus = True
else:
  specialcharstatus = False
