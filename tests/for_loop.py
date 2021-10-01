def main(namespace, src):
    return len(src.split("\n")) > 10 or namespace["main"]() != [i for i in range(1000)], ""
