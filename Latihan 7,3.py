def hapus_spasi_berlebih(kalimat):
    kata_kalimat = kalimat.split()
    
    kalimat_baru = " ".join(kata_kalimat)
    
    return kalimat_baru

kalimat = "saya tidak suka memancing ikan "
kalimat_tanpa_spasi_berlebih = hapus_spasi_berlebih(kalimat)
print(kalimat_tanpa_spasi_berlebih)