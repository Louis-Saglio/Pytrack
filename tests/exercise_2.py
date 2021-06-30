def rewrite(src):
    return src.replace("lol", "worked")


def main(namespace, src):
    namespace['main']()
    return 1, "worked"
