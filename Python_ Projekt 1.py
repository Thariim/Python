"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Viktor Krchňavý
email: krchnavy.viktor@gmail.com
discord: thariim
"""
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

separator="-"*40
user_name=input('username:')
user_password=input('password:')
users={'bob':'123','ann':'pass132','mike':'password123','liz':'pass123'}

#Přihlášení
if users.get(user_name)==user_password:
    print(separator,
          f'Welcome to the app, {user_name} \nWe have 3 texts to be analyzed.',
          separator, sep='\n'
          )
else:
    print('unregistered user, terminating the program..')
    exit()

#Výběr textu  
roster={}
while len(roster)<len(TEXTS):
    roster[len(roster)+1]=TEXTS[len(roster)]
array=len(TEXTS) 
selection=(input(f'Enter a number btw. 1 and {array} to select: '))

#Zarućení že se jedná jenom o číslo
while not selection.isnumeric():
    selection=input("Input has to be number. Please try again: ")

#Zaručení že číslo je v rozsahu
while int(selection)>array:
    selection=input('No text was selected. Please pick number in defined range: ')   
else:
    print(separator)
    picked_text=roster[int(selection)]
    text_list=(picked_text.split())
    capital=0
    upper=0
    lower=0
    numbers=0
    sum_num=0
    
    for word in text_list:
        if word.isupper() and word.isalpha():
            print(word)
            upper+=1
        elif word[0].isupper() and word.isalpha():
            capital+=1
        elif word.islower() and word.isalpha():
            lower+=1
        elif word.isdecimal():
            numbers+=1
            sum_num+=int(word)

    print(f'There are {len(text_list)} words in the selected text.\n'
        f'There are {capital} titlecase words.\n'
        f'There are {upper} uppercase words.\n'
        f'There are {lower} lowercase words.\n'
        f'There are {numbers} numeric strings.\n'
        f'The sum of all the numbers {sum_num}',
        separator,'LEN|  OCCURENCES  |NR.',separator,
        sep="\n"
        )
 
    
    nums={}
    for word in text_list:
        if len(word.strip(',')) not in nums:
            nums[len(word.strip(','))]=1
        else:
            nums[len(word.strip(','))]+=1
   
    for index in sorted(nums.items()):
         spacer="  "
         print(
            f"{spacer[:-len(str(index[0]))]}{index[0]}|{"*"*index[1]:15}|{(index[1])}",
            sep="\n"
            )   
        
            
            

    





    
    