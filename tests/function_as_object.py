# Créez une fonction main quelcquonque et une variable a telle que `a is main` renvoie `True`
def main(namespace, src):
    func = namespace["main"]
    a = namespace.get("a")
    assert a is func
    return 0, ""
