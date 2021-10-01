from utils import test_line_count


def main(namespace, src):
    if test_line_count(src, 3):
        code, message = 1, "Too many lines"
    elif namespace["main"]() != [i for i in range(0, 1000, 3)]:
        code, message = 1, ""
    else:
        code, message = 0, ""
    return code, message
