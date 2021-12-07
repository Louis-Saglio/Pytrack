# Créez une fonction main prennant en paramètre nommé "test" une autre fonction sans paramètre
# main doit ensuite appeller `test` et renvoyer le message d'erreur de l'exception si test lève une exception de type RuntimeError ou AssertionError
# si test ne lève pas d'exception de ce  type ou pas d'exception du tout renvoyer "passed"
# Attention il est interdit d'utiliser le mot clef `if` et vous n'avez droit qu'à un seul `return`
def test_r():
    raise RuntimeError("rtime")


def test_a():
    raise AssertionError("assert")


def test_p():
    pass


def main(namespace, src):
    assert src.count("return") <= 1
    assert "if " not in src
    func = namespace["main"]
    assert func(test_r) == "rtime"
    assert func(test_a) == "assert"
    assert func(test_p) == "passed"
    return 0, ""
