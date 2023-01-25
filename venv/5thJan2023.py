import re
s1 = " an apple a day keeps the doctor away"

result = re.findall(r'a\w', s1)
print("Start with a with 2 letters only - ", result)

result1 = re.findall(r'a[\w]+', s1)
print("Start with a - ", result1)

result2 = re.findall(r'a[\w]*', s1)
print("Start with a with with single a too - ", result2)
