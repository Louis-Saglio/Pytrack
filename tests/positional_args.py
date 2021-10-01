# Créez une fonction main acceptant 3 paramètres positionels ou nommés a, b et c (aka pouvant être appallé par : main(1, 2, 3) ou main(1, 2, c=3) ou main(a=1, b=2, c=3) ...)
# Le corps de la fonction doit être : `pass`
def main(namespace, src):
    src = src.split("\n")
    assert len(src) == 3 and src[1].strip() == "pass", "Le corps de la fonction n'est pas `pass`"
    func = namespace["main"]
    try:
        func(1, 2, 3)
        func(a=1, b=2, c=3)
        func(1, b=5, c=2)
    except:
        error_code, message = 1, ""
    else:
        error_code, message = 0, ""
    return error_code, message
