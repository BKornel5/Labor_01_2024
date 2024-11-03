import Labor_04_modul
from Labor_04_modul import adatok_bekerese, muveletek_vegrehajtasa, eredmenyek_megjelenitese
adatok = adatok_bekerese()
print(adatok)

eredmeny = muveletek_vegrehajtasa(adatok[0], adatok[1], adatok[2])
print(eredmeny)

eredmenyek_megjelenitese(adatok[0], adatok[1], adatok[2], eredmeny)






