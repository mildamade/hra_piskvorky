while True:
    try:
        strana = float(input('Zadej stranu čtverce v centimetrech: '))
    except ValueError:
        print('To nebylo číslo!')
    else:
        if strana <= 0:
            print('To nedává smysl!')
        else:
            break

print('Obvod čtverce se stranou', strana, 'je', 4 * strana, 'cm')
print('Obsah čtverce se stranou', strana, 'je', strana * strana, 'cm2')