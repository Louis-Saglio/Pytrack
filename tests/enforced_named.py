# Créez une fonction main acceptant 2 paramètres dont un positionel et l'autre obligatoirement nommé "key"
# La fonction doit être appellable par main(5, key=7) mais pas par main(5, 7)
# Le corps de la fonction doit être : `pass`
def main(namespace, src):
    src = src.split("\n")
    assert len(src) == 3 and src[1].strip() == "pass", "Le corps de la fonction n'est pas `pass`"
    func = namespace["main"]
    error_code, message = 0, ""
    try:
        func(5, key=7)
    except:
        error_code, message = 1, ""
    try:
        func(5, 7)
    except:
        pass
    else:
        error_code, message = 1, ""
    return error_code, message
