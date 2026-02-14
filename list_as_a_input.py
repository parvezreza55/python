n=input("Enter the text of numbers:")
lists=n.split()
print(lists)
# do sum of the number
sums=0

for i in lists:
    print(type(i))
    sums=sums+int(i)
    sums=sums + int(i)
print(sums)

numberOfWords=0
numberOfLetter=0
numberOfDigit=0

text = input("Enter the text of numbers:")
for x in text:
    x=x.lower()
    if x >= 'a' and x <= 'z':
        numberOfLetter = numberOfLetter + 1
    elif x >= '0' and x <= '9':
        numberOfDigit=numberOfDigit+1
    elif x == " " :
        numberOfWords = numberOfWords + 1

print("Number of Digit:",numberOfDigit)
print("Number of Letter: ",numberOfLetter)
print("Number of Words: ",numberOfWords+1)
