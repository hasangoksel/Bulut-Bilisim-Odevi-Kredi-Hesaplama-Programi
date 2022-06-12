def Listele():
    krediTurleri = {
    "İhtiyaç Kredisi" : 1,
    "Taşıt Kredisi" : 2,
    "Konut Kredisi" : 3,
    "Düğün Kredisi" : 4,
    "Esnaf Kredisi" : 5,
    "Öğrenci Kredisi" : 6
}
    j=1
    for i in krediTurleri:            
        print(f"{j}- {i}")
        j+=1
    