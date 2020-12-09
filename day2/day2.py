import re

f = open("inputDay2.txt","r")

# Read data from file
lines=[]
for x in f:
    lines.append(x)


# Convert lines to data
# [min, max, char, password]
data = []
for line in lines:
    d = re.split(r'\W',line)
    lineData = list(filter(None, d))
    data.append(lineData)


# Verify passwords
passwordCount = 0
for password in data:
    nbr = password[3].count(password[2])
    if nbr>=int(password[0]) and nbr<=int(password[1]):
        passwordCount+=1

print("Number of valid passwords :",passwordCount)
