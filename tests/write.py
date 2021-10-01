# Créez une fonction main prennant le path d'un file comme paramètre et écrivant 'lorem ipsum' dans ce fichier
def main(namespace, src):
    assert (
        "= open(" not in src
    ), "Attention, utiliser open naïvement peut avoir des effets de bords indésirables, utilisez `with open(path) as f:` plutôt"
    func = namespace["main"]
    func("/jail/file")
    with open("/jail/file") as f:
        assert f.read() == "lorem ipsum"
    return 0, ""
