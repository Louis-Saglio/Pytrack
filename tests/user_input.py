def rewrite(src):
    src = "def modified_input(__prompt=None):return next(input_generator)\n" + src
    return src.replace("input(", "modified_input(")


input_generator = (word for word in ("zcb", "qdf", "sqd"))


def main(namespace, src):
    func = namespace["main"]
    exit_code, message = 0, ""
    try:
        func()
    except StopIteration:
        exit_code, message = 1, ""
    try:
        next(input_generator)
    except StopIteration:
        pass
    else:
        exit_code, message = 1, ""
    return exit_code, message
