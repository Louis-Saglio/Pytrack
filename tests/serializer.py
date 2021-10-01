# Créez une fonction main ayant un paramètre de type quelquonque et enregistrant l'argument passé en paramètre dans le fichier '/jail/data'
import pickle
from os.path import exists


def main(namespace, src):
    func = namespace["main"]
    func({True, 45, "abcd"})
    assert exists("/jail/data")
    with open("/jail/data", "rb") as f:
        assert pickle.load(f) == {True, 45, "abcd"}
    return 0, ""
