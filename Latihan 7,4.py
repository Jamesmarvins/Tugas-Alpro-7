def kata_terpendek_terpanjang(kalimat):
    kata_kalimat = kalimat.split()
    
    kata_terpendek = min(kata_kalimat, key=len)
    kata_terpanjang = max(kata_kalimat, key=len)
    
    return kata_terpendek, kata_terpanjang

kalimat = "red snakes and a black frog in the pool"
terpendek, terpanjang = kata_terpendek_terpanjang(kalimat)
print(f"terpendek: {terpendek}, terpanjang: {terpanjang}")