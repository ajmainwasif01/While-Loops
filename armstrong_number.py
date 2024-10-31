num = int(input("Enter a number:"))
digit = len(str(num))

sum = 0

temp = sum
while temp > 0:
    d = temp % 10
    sum += d**digit
    temp//= 10
if sum == num:
    print("The number is an armstrong number")
else:
    print("The number is not an armstrong number")
