
#definice herního pole a značek
slovnik = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
znacka = ['-', 'x', 'o']
pocettahu = 0
delkaslovniku=len(slovnik)

#střídání hráčů
def hracfn(pocettahu):
    if pocettahu%2 == 0:
        return 2
    else: return 1

uvod = "Toto je pokus o 1D piškvorky"
print (uvod)

class OccupiedTileException(Exception):
    pass

is_finished = False
i = 0
while i < delkaslovniku and not is_finished:
    pocettahu= (pocettahu +1)
    hrac=hracfn(pocettahu)
    radek= str(pocettahu)+ ' kolo:'
    print ('Hraje hráč č: ',hrac, 'značka',znacka[hrac] )

    # kontrola zda je policko prazdne
    while True:
        vstup = input('Zadejte číslo od 1 do 10; Q pro ukoncen: ')
        if vstup.upper() == 'Q':
            is_finished = True
            break
        try:
            hodnota=int (vstup)-1
            
            if slovnik[hodnota] == '-':
                slovnik[hodnota] = znacka[hrac]
                print(slovnik)
                break
            else:
                raise OccupiedTileException()

        except ValueError as e:
            print('Spatny vstup pro tah %d : %s' % (i, vstup))
            print(slovnik)
        except OccupiedTileException as e:
            print('Obsazené pole, zvol jiné číslo !')
            print(slovnik)

    
    # while slovnik[hodnota]==znacka[0] is True:
    #     slovnik[hodnota]=znacka[hrac]
    #      print (slovnik)
    # else: 
    #    print ('Obsazené pole, zvol jiné číslo !')
        
        





#AI

