# Créez une fonction main prennant en entrée une liste de ditcionnaires ayant comme clef 'a' et comme valeur un nombre aléatoire (ex : [{'a': 2}, {'a': 6}, {'a': 3}, {'a': 2}]
# Cette fonction doit renvoyer le dictionnaire dont la valuer pour la clef "a" est la plus grande.
# Attention, la fonction ne doit pas faire plus d'une ligne et il est interdit d'utiliser le mot clef `def` autrement que pour définir `main`
def main(namespace, src):
    src.replace("def main", "")
    assert src.count("def ") == 0, "Usage de def interdit"
    func = namespace["main"]
    result = func({"a": 3}, {"a": 4}, {"a": 2, "b": 6})
    assert result == {"a": 4}, str(result)
    return 0, ""
