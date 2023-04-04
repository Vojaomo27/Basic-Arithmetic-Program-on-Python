#creating a runtime application for two inputs in an arithmethic operations

num1 = int(input('ENTER THE FIRST NUMBER'))
print ("your first input:" ,num1)
num2 = int(input('ENTER THE SECOND NUMBER'))
print ("your second input:" ,num2)

#inputing arithmethic operators

add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2
power = num1 ** num2

#output

print('The Sum of ',num1,' and ',num2 ,' is : ',add)
print('The Difference of ',num1,' and ' ,num2,' is :' ,sub)
print('The Product of ',num1, ' and ' ,num2,' is :',mul)
print('The Division of ',num1,' and ' ,num2,' is :',div)
print('Exponent of ',num1,' and ',num2,' is :',power)