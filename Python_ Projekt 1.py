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
oddelovac="-"*40
user_name=input('username:')
user_password=input('password:')
users={'bob':'123','ann':'pass132','mike':'password123','liz':'pass123'}

if users.get(user_name)==user_password:
    print(oddelovac,
          f'Welcome to the app, {user_name} \nWe have 3 texts to be analyzed.',
          oddelovac, sep='\n'
          )
else:
    print('unregistered user, terminating the program..')
    exit()
selection=int(input('Enter a number btw. 1 and 3 to select: '))
seznam={1:TEXTS[0] , 2:TEXTS[1] , 3:TEXTS[2]}
rozsah=1,2,3
if selection not in rozsah:
    print('unregistered user, terminating the program..')
    exit()
else:
    print(oddelovac)
    i=seznam[selection]
    s=(i.split())
    capital=0
    upper=0
    lower=0
    numbers=0
    sum_num=0
    
    for slovo in s:
        if slovo[0].isupper():
            capital+=1
        elif slovo.isupper():
            upper+=1
        elif slovo.islower():
            lower+=1
        elif slovo.isdecimal():
            numbers+=1
            sum_num+=int(slovo)

    print(f'There are {len(s)} words in the selected text.\n'
        f'There are {capital} titlecase words.\n'
        f'There are {upper} uppercase words.\n'
        f'There are {lower} lowercase words.\n'
        f'There are {numbers} numeric strings.\n'
        f'The sum of all the numbers {sum_num}',
        oddelovac,'LEN|  OCCURENCES  |NR.',oddelovac,
        sep="\n"
        )
 
    
    pocty={}
    for word in s:
        if len(word.strip(',')) not in pocty:
            pocty[len(word.strip(','))]=1
        else:
            pocty[len(word.strip(','))]+=1
   
    for index,tupl in sorted(pocty.items()):
         print(
            f"{index}|{"*"*tupl:15}|{(tupl)}",
            sep="\n"
            )   
        