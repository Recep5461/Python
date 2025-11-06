import pandas as pd
import matplotlib.pyplot as plt

veriler = {   
    "person_name":["Ahmet Ali","Taha","Yusuf Kerem","Ahmet Yasin","Muhammed Akif","Muhammed Eren"],
    "person_surname":["Kutluay","Karaöz","Karakaya","Tokyürek","Canyurt","Yiğit"],
    "person_id":[54,38,14,25,6,34]
}

def table_create():
    df = pd.DataFrame(veriler)
    fig, ax = plt.subplots()
    fig.canvas.manager.set_window_title("Tablo")
    ax.axis("off")
  
    table = ax.table(
        cellText = df.values,    
        colLabels = ["Ad","Soyad","Favori ID"],  
        cellLoc = "center",       
        loc = "center"            
    )
    for (row, col), cell in table.get_celld().items():
        if row == 0: 
            cell.set_text_props(weight='bold', color='white')  
            cell.set_facecolor("#4CAF50")  
        elif row %2 != 0: 
            cell.set_facecolor("#FFFFFFFC")  
        elif row %2 == 0: 
            cell.set_facecolor("#6C6A6EC8")  

    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1.2, 2) 
    plt.show()

def add_item():
    isim = input("İsim ekle: ")
    soyad = input("Soyad ekle: ")
    id = input("Favori ID ekle: ")
    veriler["person_name"].append(isim)
    veriler["person_surname"].append(soyad)  
    veriler["person_id"].append(id) 

while True:
 df = pd.DataFrame(veriler)
 print("Şuanki veriler\n",df,"\n\n<Veri Eklemek için 'a' tuşu \n<tablo oluşturmak için 't' tuşu\n<Çıkmak için 'q' tuşu")
 gir = input("bekleniyor: ").strip()
 if gir.lower() == "q": 
    break
 elif gir.lower() == "t":
    print("\n<<<Tablo oluşturuldu!...Görev Çubuğunda>>>\n@Sonraki işlem için Tablo penceresini kapat!\n")
    table_create()
 elif gir.lower() == "a":   
    add_item() 

print("Program kapatıldı!")
