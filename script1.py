name = raw_input('Podaj imie i nazwisko: \n')
age = input('Podaj swoj wiek: \n')

if(age<18):
    print ('Czesc {}, jestes {}'.format(name,'NIEPELNOLETNI'))
else:
    print ('Czesc {}, jestes {}'.format(name,'PELNOLETNI'))