# Créez une class User ayant comme attribut name et age pouvant être initialisé à l'instentiation comme celà : `User(name='Name', age=42)
def main(namespace, src):
    if "User" not in namespace and not callable(namespace["User"]):
        return 1, "No class named User found"
    user = namespace["User"](name="Louis", age=23)
    assert (getattr(user, "name", None), getattr(user, "age", None)) == ("Louis", 23)
    return 0, ""
