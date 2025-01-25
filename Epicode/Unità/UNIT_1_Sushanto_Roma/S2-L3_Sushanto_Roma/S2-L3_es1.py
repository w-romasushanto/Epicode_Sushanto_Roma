numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 4 
medie_mobili = []

for i in range(len(numeri)):
    if i < n - 1:
        segmento = numeri[:i + 1]  #numeri disponibili finché non raggiungi n
    else:
        segmento = numeri[i - n + 1 :i + 1]  #ultimi n elementi

    media = sum(segmento) / len(segmento)
    medie_mobili.append(media)

print(medie_mobili)
