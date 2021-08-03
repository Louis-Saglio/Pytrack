def main(namespace, src):
    func = namespace['main']
    if func("") is not None:
        exit_code, message = 1, "Does not return None for empty string"
    elif func("\t") != (0, "Tabulation"):
        exit_code, message = 1, "Failed to find tab"
    elif func("abc\n\tabc") != (1, "Tabulation"):
        exit_code, message = 1, "Failed to find tab"
    elif func("abc ") != (0, "Trailing white space"):
        exit_code, message = 1, "Failed to find trailing white space"
    elif func("abc\t") != (0, "Trailing white space"):
        exit_code, message = 1, "Failed to find trailing white space"
    elif func("abc\nabc\t") != (1, "Trailing white space"):
        exit_code, message = 1, "Failed to find trailing white space"
    else:
        exit_code, message = 0, ""
    return exit_code, message
