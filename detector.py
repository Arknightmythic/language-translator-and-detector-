from langdetect import detect
import langbahasa
#pendeteksi
def pendeteksi(txt):
    lg = detect(txt)
    #convert kode bahasa
    print("")
    print("text ini berbahasa : " + langbahasa.bahasa(lg))
    print("")
    