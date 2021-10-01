# Créez une fonction `main` sans paramètre qui lève une RuntimeError avec 'hello world' comme message d'erreur
def main(namespace, src):
    func = namespace["main"]
    try:
        func()
    except RuntimeError as e:
        assert str(e) == "hello world", "Mauvais message d'erreur"
        code, message = 0, ""
    else:
        code, message = 1, ""
    return code, message
