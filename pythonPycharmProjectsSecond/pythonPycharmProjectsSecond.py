#12.01.2022 ENTRY DATE - Intermediate and easy questions. 
#1
"""
firstString = input("Please enter the word: ")
if ((firstString.isupper() == True) or (firstString.islower() == True)):
	print(True)
else:
	print(False)
"""
#2
"""
number = int(input("Enter a number: "))
exponentList = list()
notExponentList = list()

for element in range (number):
	element = element + 1
	result = number % element
	if (result == 0):
		exponentList.append(element)
	else:
		notExponentList.append(element)

print("Exponent List: {}".format(exponentList))
print("Not Exponent List: {}".format(notExponentList))
"""
#3
"""
chickenNumber = int(input("Enter numbers of chicken: "))
cowNumber = int(input("Enter numbers of cows: "))
sheepNumber = int(input("Enter numbers of sheeps: "))

chickenFoots = chickenNumber * 2
cowFoots = cowNumber * 4
sheepFoots = sheepNumber * 4

totalResult = chickenFoots + cowFoots + sheepFoots
print("Total foot number is: {}".format(totalResult))
"""
#4
"""
nameList = ["Ali" ,"Vural", "Fatih", "Ekrem"]
fatihIndex = nameList.index("Fatih")
VuralIndex = nameList.index("Vural")
if (VuralIndex - fatihIndex == 1) or (fatihIndex - VuralIndex == 1):
	print(True)
else:
	print(False)
"""

#5
"""
sesliHarfString  = "aeıioöuü"
inputString = input("Enter a sentence: ")
inputStringList = list()

for item in inputString:
	inputStringList.append(item)

for element in inputStringList:
	indexNumber = inputStringList.index(element)
	for character in sesliHarfString:
		if (character == element):
			inputStringList.pop(indexNumber)

for i in inputStringList:
	print(i , end = "")
"""
#6
"""
element = int(input("Enter a number: "))
takeExponent = 2**element
print(takeExponent)

stringOfResult = str(takeExponent)
if (stringOfResult.count("666") == 0):
    print("GÜVENLI")
elif (stringOfResult.count("666") == 1):
    print("TEK KIYAMET")
elif (stringOfResult.count("666") == 2):
    print("ÇIFT  KIYAMET")
elif (stringOfResult.count("666") == 3):
    print("ÜÇ KIYAMET")
"""
#7
"""
name = input("Enter user name: ")
emptyList = list()
writtenOutput = ("Welcome Our Program {}".format(name))
print("What is your choice: If you want to keep going --Y; otherwise --N")
while (True):
    choice = (input("Enter your choice: "))
    if (choice == "N"):
        ##if (len(emptyList) == 0):
            ##print("List is empty. There is no minimum and maximum value.")
        print("Good Bye {}".format(name))
        break
    else:
        numbers = int(input("Enter numbers that you want to add: "))
        emptyList.append(int(numbers))

if(len(emptyList) == 0):
    print("There is no minimum and maximum value of the list since list is empty")
else:
    print("Minimum Value: {} |Maximum Value: {}".format(min(emptyList),max(emptyList)))
"""
#8
"""
characters = ["a","b","c","ç","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z"]
word = str(input("Enter a word: "))
word_lower = word.lower()
indexList = list()

for character in word_lower:
    if (character in characters):
        indexList.append(characters.index(character))

result = 0
for index, item in enumerate(indexList):
    print("Index: {} | Value: {}".format(index +1, item +1))
    result += (item + 1)

if ( result % 2 == 1):
    print("False")
else:
    print("True")
"""
"""
number = int(input("Enter a number: "))
word = str(input("Enter a string: "))
düzList = list()

for element in (range(1,number + 1)):
    düzList.append(element)

for element in düzList[::-1]:
    print(element, end=". ")
print(word,end= "!")
"""
"""
index = 10
yüzyıl = ".yüzyıl"
era = int(input("Enter your year for era calculating: "))
#while ((era >= 1000) and (era <= 2010)):
if (era == 1000):
    print("{}{}".format(index,yüzyıl))
elif (era >= 1001 and era <= 1100):
    print("{}{}".format(index+1,yüzyıl))
elif (era >= 1101 and era <= 1200):
        print("{}{}".format(index+2,yüzyıl))
elif (era >= 1201 and era <= 1300):
        print("{}{}".format(index+3,yüzyıl))
elif (era >= 1301 and era <= 1400):
        print("{}{}".format(index+4,yüzyıl))
elif(era >= 1401 and era <= 1500):
        print("{}{}".format(index+5,yüzyıl))
elif(era >= 1501 and era <= 1600):
        print("{}{}".format(index+6,yüzyıl))
elif(era >= 1601 and era <= 1700):
        print("{}{}".format(index+7,yüzyıl))
elif(era >= 1701 and era <= 1800):
        print("{}{}".format(index+8,yüzyıl))
elif(era >= 1801 and era <= 1900):
        print("{}{}".format(index+9,yüzyıl))
elif (era >= 1901 and era <= 2000):
        print("{}{}".format(index+10,yüzyıl))
elif (era >= 2001 and era <= 2010):
        print("{}{}".format(index+11,yüzyıl))
else:
    print("{} is not included in the list.".format(era))
"""
"""
numbers = ["0","1","2","3","4","5","6","7","8","9"]
stringIndex = 0
integerIndex = 0

wordTaken = str(input("Please enter your word: "))
for character  in wordTaken:
    if (character in numbers):
        integerIndex += 1
    else:
        if (character == " "):
            continue
        stringIndex += 1

stringInteger = {"Characters":stringIndex,"Numbers":integerIndex}
print("DictionaryList: {}".format(stringInteger))
"""
"""
wordTaken = str(input("Please enter a word: "))
lengthOfWord = len(wordTaken)

if (lengthOfWord % 2 == 0):
    print("The character that is in the middle: {}{}".format(wordTaken[(lengthOfWord // 2) - 1], wordTaken[(lengthOfWord // 2)]))
elif (lengthOfWord % 2 == 1):
    if (lengthOfWord == 1):
        print("The character that is in the middle: {}".format(wordTaken))
    else:
        print("The character that is in the middle: {}".format(wordTaken[(lengthOfWord//2)]))
"""
"""
ORTA SEVIYE - 27
name = str(input("Enter your name: "))
print("Welcome our game {}".format(name))
numbersList = list()
while (True):
    numbersTaken = int(input("Enter a number: "))
    if numbersTaken == 0:
        print("You can not append any number to the list.")
        break
    else:
        numbersList.append(numbersTaken)

if (7 in numbersList):
    print("BOOM!")
else:
    print("There is no 7 in the list!")
"""

"""
ORTA SEVIYE 23:
name = input("Enter your name: ")
print("Welcome Our Game {}!".format(name))
numberList = list()

while(True):
    number = (input("Enter a number: "))
    if (number == "Q" or number == "q"):
        print("You can not add to the list anymore.")
        break

    else:
        numberList.append(int(number))

notSameList = list()
sameList = list()
for element in numberList:
    if (numberList.count(element) == 1):
        notSameList.append(element)
    else:
        sameList.append(element)

print("Numbers that are not same: {}".format(notSameList))
print("Numbers that are same:     {}".format(sameList))
print("\nNumbers NOT SAME: ")
for index, numbers in enumerate(notSameList):
    print("Index: {}  Number: {}".format(index,numbers))
"""

"""
ORTA SEVIYE: 26
oneZeroList = list()
normalList = list()
reverseList = list()
result = 0
element = 0

while(True):
    oneZero = str(input("Enter number: "))
    if (oneZero == "Q" or oneZero == "q"):
        print("You are not allowed to add number to the list.")
        break

    else:
        oneZeroList.append(int(oneZero))

for index in range(len(oneZeroList)):
    normalList.append(index)

for element in normalList[::-1]:
    reverseList.append(element)

for index in reverseList:
    result +=  (oneZeroList[element] * (2 ** index))
    element += 1

print("Total Result: {}".format(result))
"""
