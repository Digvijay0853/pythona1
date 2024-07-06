# # # # # # # mark=int(input('Enter the marks :'))
# # # # # # # if mark >= 35:
# # # # # # #    print('pass')
# # # # # # # else:
# # # # # # #    print('fail')
# # # # # #
# # # # # # # char=input('Enter the character')
# # # # # # # if len(char) == 1:
# # # # # # #    if char in 'AIEOUaioue':
# # # # # # #       print('Entered character is vowel')
# # # # # # #    else:
# # # # # # #       print('Entered character is not vowel')
# # # # # # # else:
# # # # # # #    print('Please entered single character')
# # # # # #
# # # # # # string=input('Enter the String')
# # # # # # if string[0] in 'AIEOUaieou':
# # # # # #    print(f'{string} startswith vowel')
# # # # # # else:
# # # # # #    print(f'{string} not startwith vowel')
# # # # #
# # # # # # mark=int(input('Enter the marks'))
# # # # # # if mark > 80:
# # # # # #    print('Bike')
# # # # # # elif mark > 70:
# # # # # #    print('Mobile')
# # # # # # elif mark>35:
# # # # # #    print('belt')
# # # # # # else:
# # # # # #    print('you are not my son')
# # # # #
# # # # # #write a program to check string is palindrome or not
# # # # # s1=input('Enter the string : ')
# # # # # s2=s1[::-1]
# # # # # if s1 == s2:
# # # # #    print(f'{s1} is a palindrome string')
# # # # # else:
# # # # #    print(f'{s1} is not a palindrome string')
# # # #
# char=input('Enter the value : ')
# if len(char) == 1:
#    if char.isupper():
#       print(f'Entered value is in uppercase')
#    elif char.islower():
#       print('Entered value is in lowercase')
#    elif char.isdigit():
#       print('Entered value is a number')
#    else:
#       print('Entered value is a special character')
# else:
#    print('Entered only single value')
# # # # #
# # # s=int(input('Enter the value :'))
# # # s1=str(s)
# # # if s1 == s1[::-1]:
# # #    print(f'{s} is a palindrome int')
# # # else:
# # #    print(f'{s} is not a palindrome int')
# # # print(chr(97))
#

char=input('Enter the value : ')
if len(char) == 1:
    if char.isalpha():
      if char.isupper():
        print(f'The entered character was {char} and updated character is {char.lower()}')
      elif char.islower():
        print(f'The entered character was {char} and updated character is {char.upper()}')
    else:
        print('Entered character is not alphabet')
else:
    print('Please enter single character')
