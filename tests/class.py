# Créez une classe User ayant méthode hello qui ne prend pas d'argument (à part self) et qui retorune 'hello'
def main(namespace, src):
    User = namespace["User"]
    assert User().hello() == "hello"
    return 0, ""
