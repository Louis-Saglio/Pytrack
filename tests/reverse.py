def main(namespace, src):
    func = namespace["main"]
    if func([]) != []:
        error_code, message = 1, "Did not work with an empty list"
    elif func(["abc", True, 1, False, None, []]) != [[], None, False, 1, True, "abc"]:
        error_code, message = 1, ""
    else:
        error_code, message = 0, ""
    return error_code, message
