from argostranslate import package, translate

sentence = "At eight o'clock on Thursday morning Arthur didn't feel very good."

excerpt = [
'''Donde se prosiguen los innumerables trabajos que el bravo don Quijote y su buen escudero Sancho Panza pasaron en la venta que, por su mal, pensó que era castillo''',

'''Donde se cuentan las razones que pasó Sancho Panza con su señor Don Quijote, con otras aventuras dignas de ser contadas''',

'''De las discretas razones que Sancho pasaba con su amo, y de la aventura que le sucedió con un cuerpo muerto, con otros acontecimientos famosos''',

'''De la jamás vista ni oída aventura que con más poco peligro fue acabada de famoso caballero en el mundo, como la que acabó el valeroso don Quijote de la Mancha'''
]

installed_languages = translate.load_installed_languages()
print(installed_languages)
_t1 = None
_t2 = None
for lang in installed_languages:
    if lang.name == "Spanish":
        _t1 = lang
    if lang.name == "English":
        _t2 = lang

print("hmmmmm???")
t = _t1.get_translation(_t2)
for paragraph in excerpt:
    translated = t.translate(paragraph)

    print("---")
    print(paragraph)
    print()
    print(translated)
    print("---")

print(t.translate("Hola Mundo"))

#import ebooklib
#from ebooklib import epub

book = "res/foreign/novels/Don_Quixote.txt"




