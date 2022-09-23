import translator
import detector

#looping
i=True
while i :

    #tampilan Menu
    print("---------Raw Translator Program by albert---------")
    print("Menu")
    print("1.penerjemah bahasa")
    print("2.pendeteksi bahasa")
    print("3.keluar")

    #input pilihan
    choice = input("Masukkan pilihan menu(nomor) :")

    #pemanggilan
    if choice == "1":
        a=open("codeBahasa.txt","r").read()
        print(a)
        txt = input("masukkan teks : ")
        language = input("convert ke bahasa lain (masukkan kode) :")
        print("")
        if language == "en":
            translator.transen(txt)
        else:
            translator.trans(txt,language)

    elif choice == "2":
        txt = input("masukkan text : ")
        detector.pendeteksi(txt)

    elif choice == "3":
        print("good bye. it's happy to serve you")
        i=False
        
    else:
        print("pilihan salah")
        print("")
