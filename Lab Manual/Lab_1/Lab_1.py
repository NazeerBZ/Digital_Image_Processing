#Write a program that takes the month (1…12) as input. 
#Print whether the season is summer, winter, spring or autumn depending upon the input month.

#month = int(input());
#
#if(month >= 3 and month <= 5 ):
#    print('spring');
#elif(month >=6 and month <= 8):
#    print('Summer');
#elif(month >= 9 and month <= 11):
#    print('Autumn');
#elif(month == 12 or month == 1 or month == 2):
#    print('Winter');
#else:
#    print('Incorrect input')

#############################################################

#To determine whether a year is a leap year, follow these steps:
#1.	If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
#2.	If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
#3.	If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
#4.	The year is a leap year (it has 366 days).
#5.	The year is not a leap year (it has 365 days).


#year = int(input());
#
#if (year % 4 == 0 and year % 100 == 0 and year % 400 == 0):
#       print(str(year) + ' is a leap year');
#elif(year % 4 == 0 and year % 100 != 0):
#       print(str(year) + ' is a leap year');
#else:
#    print(str(year) + ' is not a leap year');

###################################################################

#Write a program that takes a line as input and finds the number of letters and digits in the input

#sentance = input();
#digitCount = 0;
#letterCount = 0;
#
#for x in range(len(sentance)):
#    if(sentance[x].isdigit()):
#        digitCount = digitCount + 1;
#    else:
#        letterCount = letterCount + 1
#print('No. of Digits: ' + str(digitCount) + '\nNo. of letter: '+ str(letterCount));

#################################################################

#Write a program that takes a sentence as input. Compute the frequency of each words and prints them.

#sentance = input().split(' ');
#dic = {};
#for x in sentance:
#    if x in dic:
#        dic[x] = dic[x] + 1
#    else:
#        dic[x] = 1
#
#print(dic);