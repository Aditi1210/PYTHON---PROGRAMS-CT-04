n=int(input("Enter the range of number:"))

sum=0

p=3

for i in range(1,n+1):

    sum += p

    p=(p*10)+3

print("The sum of the series = ",sum)
