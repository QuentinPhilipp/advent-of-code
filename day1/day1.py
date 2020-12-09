f = open("inputDay1.txt","r")

# Read data from file
data=[]
for x in f:
    data.append(int(x))

# Get answer
op = 0
for number1 in data:
    for number2 in data:
        op+=1
        if number1+number2==2020:
            print("Found answer")
            print("Number 1:",number1," | Number 2: ",number2)
            print("Sum=",number1+number2)
            print("Multiplication=",number1*number2)
            break

print("Number of opearations:",op)