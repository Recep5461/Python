sorular = [
    {
    "soru":"Türkiye'nin başkenti neresidir?",
    "şıklar":{
        "A": "Ankara",
        "B": "İstanbul",
        "C": "Bursa",
        "D": "İzmir",
        },
     "doğru":"A"}, 
    {
    "soru":"TC. ne zaman kurulmuştur?",
    "şıklar":{
        "A": "1920",
        "B": "1924",
        "C": "1923",
        "D": "1919",
        },
     "doğru":"C"},
    {
    "soru":"Elon Musk'ın ilk oyunu hangisidir?",
    "şıklar":{
        "A": "Clash Royale",
        "B": "Subway Surfers",
        "C": "Roblox",
        "D": "Blastar",
        },
     "doğru":"D"}, 
    {
    "soru":"Teknofest ilk hangi yılda düzenlendi?",
    "şıklar":{
        "A": "2010",
        "B": "2018",
        "C": "2020",
        "D": "2015",
        },
     "doğru":"B"},
    {
    "soru":"Django hangi dil ile yazılır?",
    "şıklar":{
        "A": "Java",
        "B": "C#",
        "C": "Python",
        "D": "C++",
        },
     "doğru":"C"}, 
]

yanlislar = 0
dogrular = 0

def sorucu(): 
  global dogrular, yanlislar
  for soru in sorular: 
    print("\n")
    print(soru["soru"])
    for şık, cevap in soru["şıklar"].items():
        print(şık," : ",cevap)
    cevap = input("şıkkınız : ")
    if cevap.upper() == soru["doğru"]:
      print(cevap, "şıkkı bildiniz!")
      dogrular += 1
    else:
      print(cevap, "şıkkı yanlış\ndoğru = ", soru["doğru"])
      yanlislar += 1 

sorucu()
print("\n","doğru sayısı : ",dogrular,"\n","yanlış sayısı : ",yanlislar)

