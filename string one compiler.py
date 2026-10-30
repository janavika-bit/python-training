//(no:1)Length of a string
Max Score: 1 | Difficulty: Not Specified

Take a string from the input and print the length of that string

Input:

OneCompiler
Output:

11

//pgm
  s=input()
print(len(s))

//(no:2)Join the strings
Max Score: 2 | Difficulty: Not Specified

Take two strings from the input, join those two strings with a space and print the new string

Input:

Harry
Potter
Output:

Harry Potter

//pgm
s1 = input()
s2 = input()
print(s1+ s2)

//(no:3)Compare the Strings
Max Score: 3 | Difficulty: Not Specified

Take two strings from the input and print whether or not the strings are equal

Input(1):

Hello
Hi
Output(1):

false
Input(2):

Hello
Hello
Output(2):

true

//pgm
  1 = input()
s2 = input()
if s1==s2:
  print("true")
else:
  print("false")

//(no:4)First character of a string
Max Score: 3 | Difficulty: Not Specified

Take a string from the input and print the first character of that string

Input:

World
Output:

W

//pgm
  s=input()
print(s[0])

//(no:5)Last character of a string
Max Score: 3 | Difficulty: Not Specified

Take a string from the input and print the last character of that string

Input:

World
Output:

d
  
//pgm
  s=input()
print(s[-1])

//(no:6)Join first & last characters of a string
Max Score: 4 | Difficulty: Not Specified

Take a string from the input and print the first character and last characters of the string together

Input:

Hello World
Output:

Hd
//pgm
  s=input()
print(s[0]+s[-1])

//(no:7)Alphanumeric strings
Max Score: 5 | Difficulty: Not Specified

Take a string from the input and check whether or not it contains both letters and numerals

Input(1):

R2D2
Output(1):

true
Input(2):

OC
Output(2):

false

//pgm
  s=input()
numcount=alphacount=False
for i in s:
  if i.isalpha():
    alphacount=True
  elif i.isalnum():
    numcount=True
  if alphacount and numcount:
    break
if alphacount and numcount:
  print("true")
else:
  print("false")

//(no:8)Uppercase check
Max Score: 5 | Difficulty: Not Specified

Take a string from the input and check all the letters in the string are of upper case

Input(1):

OC
Output(1):

true
Input(2):

oc
Output(2):

false

//pgm
  s=input()
if s.isupper():
  print("true")
else:
  print("false")

//(no:9)Lowercase check
Max Score: 5 | Difficulty: Not Specified

Take a string from the input and check all the letters in the string are of lower case

Input:

OC
Output:

false
Input:

oc
Output:

true

//pgm
  s=input()
if s.islower():
  print("true")
else:
  print("false")

//(no:10)String lengths equal or not
Max Score: 5 | Difficulty: Not Specified

Take two strings from the input and check the lengths of those strings equal or not

Input:

Peter
Griffin
Output:

false

//pgm
  s1=input()
s2=input()
if len(s1)==len(s2):
  print("true")
else:
  print("false")

//(no:11)Reverse a string
Max Score: 5 | Difficulty: Not Specified

Take a string from the input and print it in reverse

Tom
Output:

moT
  
//pgm
  s=input()
print(s[::-1])

//(no:12)Split strings by comma
Max Score: 5 | Difficulty: Not Specified

Take a string from the input and split the strings with comma. Print the new strings one per line

Input:

a,b,c,d
Output:

a
b
c
d

//pgm
s=input()
for i in s.split("," ):
  print(i)

//(no:13)Remove vowels
Max Score: 6 | Difficulty: Not Specified

Take a string from the input and remove the vowels and print it

Input:

Harry
Output:

Hrry

//pgm
  string = input()
vow="aeiouAEIOU"
for char in string:
  if char in vow:
    string=string.replace(char,"")
print(string)

//(no:14)Reverse the character case
Max Score: 7 | Difficulty: Not Specified

Take a string from the input and change lowercase characters to uppercase and uppercase characters to lowercase

Input:

Harry
Output:

hARRY

//pgm
  s=input()
print(s.swapcase())

//(no:15)Print ascii value
Max Score: 8 | Difficulty: Not Specified

Take a string from the input and print ascii character

Input:

A
Output:

65

//pgm
  s=input()
print(ord(s))

//(no:16)Remove occurrences of a char
Max Score: 8 | Difficulty: Not Specified

Take a string from the input and remove all occurrences of given char from that string

Input:

abcdefghabcdefgh
b
Output:

acdefghacdefgh

//pgm
  s=input()
char=input()
print(s.replace(char,""))

//(no:17)Search for a word
Max Score: 9 | Difficulty: Not Specified

Search a word existence inside a given string

Input:

Wikipedia is a free online encyclopedia, created and edited by volunteers around the world
online
Output:

true

//pgm
  sen=input()
word=input()
print("true" if word in sen else"false")

//(no:18)Count vowels and consonants
Max Score: 10 | Difficulty: Not Specified

Count the total vowels and consonants in a given string and print them

Input:

Harry Potter
Output:

3
9

//pgm
s = input()
vowelcount = 0
con = 0
for i in s:
  if i in "aeiouAEIOU":
   vowelcount = vowelcount+1
  else:
   con = con+1
  
print(vowelcount)
print(con)

//(no:19)Anagram check
Max Score: 10 | Difficulty: Not Specified

Check the given 2 strings are anagrams.

Hint: anagram means the strings contains same characters but order of characters is not important

Note: Ignore considering the case or spaces.

Input(1):

Listen
Silent
Output(1):

true
Input(1):

School master
The classroom
Output(1):

true

//pgm
  s1=input().lower().replace(" ","") 
s2=input().lower().replace(" ","")
if (len(s1)!=len(s2)):
  print("false")
elif sorted (s1)==sorted(s2):
  print("true")
else:
  print("false")

//(no:20)Palindrome check
Max Score: 10 | Difficulty: Not Specified

Check whether or not the given string is a palindrome

Input:

civic
Output:

true

//pgm
  s=input()
if s==s[::-1]:
  print("true")
else:
  print("false")
  
  
