#mathematical operations
#operations using numbers
print(23+56)
print(65-23)
print(56*89)
print(96/7)
print(34**2)
print(96//7)
print(type(96//7)) # class int

#using variables
num1=24
num2=36
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num2/num1)
print(num1**num2)
print(num2//num1)

#strings
print("good morning")
print('glad to see you')
hello="nice to meet you"
print(hello)
print(len(hello))
#index and slicing
hello= "Difficulties in life are intended to make us better, not bitter"
print(len(hello))
print(hello[5])
print(hello[16])
print(hello[5: 54])
print(hello[15: 25])
print(hello[23: 57])
#slicing(+)
text="If you can't find a way, create one!"
print(text)
print(len(text))
print(text[2: 6])
print(text[5])
print(text[ :12])
print(text[26: ])
print(text[1:1])
print(text[26: 2: -1])#-1 indicates reverse direction
print(text[-1:-36]) #empty string
print(text[-5: -15 : -2])
print(text[-34 : -32 : ])
print(text[ : : -3])
print("index 16 value is", text[16])
#text[16] = 'l'
#print(text[16]) #immutability but when reassign it will change
print(id(text))#to know the address value.
text1="If you can't find a way, create one!"
text2="If you can't find a way, create one!"
print(id(text2))
print(id(text1))
print(type(2))#int
print(type(10.63514))#float
print(type(5+8j))#complex
