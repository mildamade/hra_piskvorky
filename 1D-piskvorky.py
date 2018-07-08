
#definice herního pole a značek
radku = 6
sloupcu = 10
velikost_piskvorky = 3

def vytvor_slovnik(radku, sloupcu):
    slovnik = [ [ '-' for x in range(0, sloupcu) ] for y in range(0, radku) ]
    return slovnik

def testuj_smer(slovnik, velikost_piskvorky, r, s, barva, smer):
    for sl in range(0, velikost_piskvorky):
        radek = r + sl * smer[0]
        sloupec = s + sl * smer[1]
        if otestuj_rozsah(radek, sloupec, radku, sloupcu):
            if slovnik[radek][sloupec] != barva:
                return False
        else:
            return False
    return True


def testuj_piskvorku(slovnik, velikost_piskvorky, r, s, barva):
    smery = [(0, 1), (1, 0), (1, 1), (1, -1)]
    nalezeno = False
    for smer in smery:
        test_smeru = testuj_smer(slovnik, velikost_piskvorky, r, s, barva, smer)
        if test_smeru:
            return True
    return False

def najdi_piskvorku(slovnik, velikost_piskvorky, radek, sloupec, barva):
    print('Hledam piskvorku, posledni pozice: %d,%d barvy %s' % (radek, sloupec, barva))

    for r in range(0, len(slovnik)):
        for s in range(0, len(slovnik[0])):
            if testuj_piskvorku(slovnik, velikost_piskvorky, r, s, barva):
                return 'Vitezstvi! %s' % barva
    
    return False

    

slovnik = vytvor_slovnik(radku, sloupcu)
znacka = ['-', 'x', 'o']
pocettahu = 0
delkaslovniku=len(slovnik) * len(slovnik[0])

#střídání hráčů
def hracfn(pocettahu):
    if pocettahu%2 == 0:
        return 2
    else: return 1

def print_slovnik():
    for sl in slovnik:
        print (''.join(sl))

uvod = "Toto je pokus o 1D piškvorky"
print (uvod)

class OccupiedTileException(Exception):
    pass

def otestuj_rozsah(index_radku, hodnota, radku, sloupcu):
    return index_radku >= 0 and index_radku < radku and hodnota >= 0 and hodnota < sloupcu

is_finished = False
i = 0
while i < delkaslovniku and not is_finished:
    pocettahu= (pocettahu +1)
    hrac=hracfn(pocettahu)
    radek= str(pocettahu)+ ' kolo:'
    print ('Hraje hráč č: ',hrac, 'značka',znacka[hrac] )

    # kontrola zda je policko prazdne
    while True:
        vstup = input('Zadejte pozici; Q pro ukoncen: ').upper()
        if vstup.upper() == 'Q':
            is_finished = True
            break
        try:
            if len(vstup) < 2:
                raise ValueError('Vstup musi byt dlouhy aspon 2 znaky')

            pismeno = vstup[0]
            index_radku = ord(pismeno) - ord('A')
            hodnota=int (vstup[1:])-1

            print (index_radku, hodnota)

            if not otestuj_rozsah(index_radku, hodnota, radku, sloupcu):
                raise ValueError('Suuradnice jsou mimo rozsah!')
            
            if slovnik[index_radku][hodnota] == '-':
                slovnik[index_radku][hodnota] = znacka[hrac]
                print_slovnik()

                piskvorka = najdi_piskvorku(slovnik, velikost_piskvorky, index_radku, hodnota, znacka[hrac])
                if piskvorka:
                    print(piskvorka)
                    is_finished = True
                break
            else:
                raise OccupiedTileException()

        except ValueError as e:
            print('Spatny vstup pro tah %d : %s' % (i, vstup))
            print_slovnik()
        except OccupiedTileException as e:
            print('Obsazené pole, zvol jiné číslo !')
            print_slovnik()

    
    # while slovnik[hodnota]==znacka[0] is True:
    #     slovnik[hodnota]=znacka[hrac]
    #      print (slovnik)
    # else: 
    #    print ('Obsazené pole, zvol jiné číslo !')
        
        





#AI

