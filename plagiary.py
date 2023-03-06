from googletrans import Translator

trans = Translator() # translates text

# main cycle
while True:
    
    spanish = trans.translate(input("Input text: "), dest='es')
    result = trans.translate(spanish.text, src='es', dest=spanish.src)
    print(f"Changed text: {result.text}\n")