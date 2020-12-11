#sözlükler pek çok veriyi barindirabilir
sozluk = {"araba":"car","kirmizi":"red"}
print(sozluk)
print(sozluk["araba"])
print(sozluk["kirmizi"])
for kelime in sozluk:
    print(kelime,":",sozluk[kelime])
