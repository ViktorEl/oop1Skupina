
text = 'Kuzelnik zautocil silou 20 s manou 50'

cisla = [int(slovo) for slovo in text.split(' ') if slovo.isdigit()] # generatorova notacia
print(cisla)



