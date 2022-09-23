from googletrans import Translator

#object
translate = Translator()

#translator
def trans(txt, language):
    result= translate.translate(txt,dest=language)
    print("hasil terjemahan:")
    print(result.text)
    print("")

#translator english
def transen(txt):
    result= translate.translate(txt)
    print("hasil terjemahan:")
    print(result.text)
    print("")

