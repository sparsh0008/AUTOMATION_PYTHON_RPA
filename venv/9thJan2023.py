import re

s1 = "one two three four five 6 7 8 9 10"
res = re.findall(r'[\d]+', s1)
print("Only Digits  \t", res)

s2 = "cat bat mat rat mon m"
result3 = re.findall(r'\bm[\w]', s2)
print("starts with M  ", result3)

s3 = "Rahul 20 08-02-2002 Arun 22 28-11-2000 Vicky 24 27-10-1998"
result1 = re.findall(r'\b\d{2}-\d{2}-\d{4}\b', s3)
print("BOD  \t\t\t", result1)

s4 = "Arun 8360325166 Arun@gmail.com sk 8360328285 sk@gmail.com"
name = re.findall(r'\b\w\w\w\w\b', s4)
number = re.findall(r'\b[\w]*\b\d{10}\b', s4)
email = re.findall(r'[\w]*@[\w]*.[\w]*', s4)
print("Name    \t\t", name)
print("Phone number  \t", number)
print("Email  \t\t", email)
