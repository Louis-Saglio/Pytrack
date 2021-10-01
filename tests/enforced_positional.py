# Créez une fonction main acceptant 2 paramètres a et b positionels seulement
# La fonction doit être appellable par main(5, 7) mais pas par main(a=5, b=7) ou main(1, b=2)
# Le corps de la fonction doit être : `pass`
import inspect


def main(namespace, src):
    src = src.split("\n")
    assert len(src) == 3 and src[1].strip() == "pass", "Le corps de la fonction n'est pas `pass`"
    func = namespace["main"]
    error_code, message = 0, ""
    try:
        func(5, 7)
    except:
        error_code, message = 1, ""
    try:
        func(a=5, b=7)
        func(4, b=8)
    except:
        pass
    else:
        error_code, message = 1, ""
    assert inspect.getfullargspec(func).args == ["a", "b"], "Les paramètres possibles ne sont pas a et b"
    return error_code, message
