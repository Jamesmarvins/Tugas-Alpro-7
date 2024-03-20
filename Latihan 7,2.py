def hitung_kemunculan_kata(kalimat, kata):
    kata_kalimat = kalimat.split()
    count = kata_kalimat.count(kata)
    return count

kalimat = "Saya mau makan. Makan itu wajib. Mau siang atau malam saya wajib makan"
kata_dicari = "makan"

jumlah_kemunculan = hitung_kemunculan_kata(kalimat, kata_dicari)
print(f"{kata_dicari} ada {jumlah_kemunculan} buah")
