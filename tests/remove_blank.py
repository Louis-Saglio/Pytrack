def main(namespace, src):
    func = namespace["main"]
    if func([]) != []:
        error_code, message = 1, "Did not work with an empty list"
    elif func(["abc", "def"]) != ["abc", "def"]:
        error_code, message = 1, ""
    elif func(["", "lol", "lorem", "ipsum", "", "", "dolor", ""]) != ["lol", "lorem", "ipsum", "dolor"]:
        error_code, message = 1, ""
    else:
        error_code, message = 0, ''
    return error_code, message
