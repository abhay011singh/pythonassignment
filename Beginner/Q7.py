str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if sorted(str1.lower()) == sorted(str2.lower()):
    print("True (Anagram)")
else:
    print("False (Not an Anagram)")
