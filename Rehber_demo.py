# KULLANILACAK MODÜLLERİ TANITMA
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

# VERİ TABANI OLUŞTURMA

vt = sqlite3.connect('REHBER3.db')
im = vt.cursor()
im.execute("create table if not exists adres(adivesoyadi TEXT, telefonu TEXT, resim TEXT, aciklama TEXT)")
vt.commit()



# PENCERE OLUŞTURMA
pencere = Tk()
pencere.title("ADRES DEFTERI")
pencere.geometry("1000x500")
pencere.resizable(False, False)



# ETİKETLER

Label(text="ADRES DEFTERİ", font="Verdana 20 bold").place(x=10, y=30)
Label(text="ADI SOYADI.............:", font="Verdana 12 ").place(x=10, y=110)
Label(text="TELEFON NUMARASI..:", font="Verdana 12 ").place(x=10, y=140)
Label(text="FOTOĞRAF...............:", font="Verdana 12 ").place(x=10, y=170)
Label(text="NOT........................:", font="Verdana 12 ").place(x=10, y=200)
global gir1
global gir2
global gir3
global gir4


# ARAMA BÖLÜMÜ

Label(text="İSME GÖRE ARAMA", font="Verdana 12 ").place(x=350, y=20)
ara_isim = Entry(width=30)
ara_isim.place(x=560, y=20)

Label(text="TELEFONA GÖRE ARAMA", font="Verdana 12 ").place(x=350, y=60)
ara_telefon = Entry(width=30)
ara_telefon.place(x=560, y=60)


# MESAJLAR

def mesaj1(text):
    msg = messagebox.showinfo(text, "Kayıt Başarılı !")

def mesaj2(text):
    msg = messagebox.showerror(text, "Aynı Kişi veya Numara Kayıtlı!")

def mesaj3(text):
    msg = messagebox.showerror(text, "Bu İsimde Kayıt Bulunamadı!")

def mesaj4(text):
    msg = messagebox.showerror(text, "Bu Numaralı Kayıt Bulunamadı!")

def mesaj5(text):
    msg = messagebox.showinfo(text, "Kayıt Silindi!")


#YENİ KAYIT EKLE (EKRANI TEMİZLEME)

def yeni_kayit():
    gir1 = Entry(width=90)
    gir1.place(x=200, y=110)
    gir2 = Entry(width=90)
    gir2.place(x=200, y=140)
    gir3 = Entry(width=90)
    gir3.place(x=200, y=170)
    gir4 = Entry(width=90)
    gir4.place(x=200, y=200)
    gir1.focus()


#KAYIT YAPMA FONKSİYONU

def kayit_yap():
    a = gir1.get()
    b = gir2.get()
    c = gir3.get()
    d = gir4.get()

    def degerle():
        im.execute("insert into adres values(?,?,?,?)", [a, b, c, d])
        vt.commit()

    kod=0
    im.execute("""SELECT adivesoyadi,telefonu FROM adres""")
    kontrol=im.fetchall()
    for i in kontrol:
        ad_kontrol=i[0]
        tel_kontrol=i[1]
        if ad_kontrol == a or tel_kontrol == b:
            mesaj2("KAYIT VAR")
            kod=1

    if kod==0:
        degerle()
        mesaj1("KAYIT")



#KAYIT ARAMA

def ara_isim1():
    kod=0
    z = ara_isim.get()
    im.execute("""SELECT adivesoyadi,telefonu, resim, aciklama  FROM adres""")
    kontrol_ara=im.fetchall()
    for i in kontrol_ara:
        ad_kontrol = i[0]
        if ad_kontrol == z:
            l1 = Label(text=i[0], font="Verdana 12 bold ")
            l1.place(x=200, y=110)
            l2 = Label(text=i[1], font="Verdana 12 bold ")
            l2.place(x=200, y=140)
            l3 = Label(text=i[2], font="Verdana 12 bold ")
            l3.place(x=200, y=170)
            l4 = Label(text=i[3], font="Verdana 12 bold ")
            l4.place(x=200, y=200)
            kod=1
    if kod==0:
       mesaj3("KAYIT BULUNAMADI")

def ara_telefon1():

    kod=0
    z = ara_telefon.get()
    im.execute("""SELECT adivesoyadi,telefonu, resim, aciklama  FROM adres""")
    kontrol_ara=im.fetchall()
    for i in kontrol_ara:
        tel_kontrol = i[1]
        if tel_kontrol == z:
            gir1.insert(0,i[0])
            gir2.insert(0,i[1])
            gir3.insert(0,i[2])
            gir4.insert(0,i[3])
            kod=1
    if kod==0:
       mesaj4("KAYIT BULUNAMADI")

#KAYIT SİLME

def kayit_silme():
    s=gir1.get()
    msg = messagebox.askyesno("SİLME İŞLEMİ", "EMİN MİSİN?")
    if msg == True:
        im.execute ("delete from adres where adivesoyadi= ? ", [s])
        vt.commit()
        gir1.delete(0, "end")
        gir2.delete(0, "end")
        gir3.delete(0, "end")
        gir4.delete(0, "end")
        ara_isim.delete(0,"end")
        mesaj5("SİLME")





# BUTONLAR

bul1 = Button(text="BUL", command=ara_isim1).place(x=750, y=20, height=20)

bul2 = Button(text="BUL", command=ara_telefon1).place(x=750, y=60, height=20)

kaydet_butonu = Button(text="KAYDET", command=kayit_yap).place(x=690, y=230)

yeni_kayit_ekle = Button(text="YENİ KAYIT EKLE", command=yeni_kayit).place(x=10, y=270, width=150, height=30)

kayit_sil = Button(text="KAYIT SİL", command=kayit_silme).place(x=10, y=310, width=150, height=30)

kayit_duzenle = Button(text="KAYIT DÜZENLE").place(x=10, y=350, width=150, height=30)

sirala = Button(text="İSME GÖRE SIRALA").place(x=10, y=390, width=150, height=30)

cikis = Button(text="ÇIKIŞ").place(x=10, y=430, width=150, height=30)









pencere.mainloop()
