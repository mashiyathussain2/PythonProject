from translate import Translator  
translator = Translator(to_lang=input("Enter language into which you have to translate: "))
translation = translator.translate(input("Enter text: "))
print(translation)
