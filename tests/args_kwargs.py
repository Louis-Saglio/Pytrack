# Créez une fonction qui peut prendre comme paramétres n'importe quelles paramètres positionels et nommés
# Le corps de la fonction doit être `pass`
def main(namespace, src):
    src = src.split("\n")
    assert len(src) == 3 and src[1].strip() == "pass", "Le corps de la fonction n'est pas `pass`"
    func = namespace["main"]
    try:
        func(1, 2, 2, None, a=5, qzerf=8, fswq=9)
        func(1, 2, 2, None, 8, 5)
        func(t=1, g=2, b=2, c=None, qwsdef=8, wsd=5)
    except:
        code, message = 1, ""
    else:
        code, message = 0, ""
    return code, message
