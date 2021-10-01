# Créez une fonction main prennant en paramètre la path vers un fichier et retournant le contenu de ce fichier
def main(namespace, src):
    assert (
        "= open(" not in src
    ), "Attention, utiliser open naïvement peut avoir des effets de bords indésirables, utilisez `with open(path) as f:` plutôt"
    func = namespace["main"]
    with open("/jail/file", "w") as f:
        f.write("worked")
    assert func("/jail/file") == "worked"
    return 0, ""
