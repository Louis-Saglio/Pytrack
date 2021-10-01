def main(namespace, src):
    func = namespace["main"]
    if func(["abc", "def", "ijk", "wxc"], ["qsd", "fgh", "jkl"]) != ["abcqsd", "deffgh", "ijkjkl"]:
        error_code, message = 1, ""
    elif func([]) != []:
        error_code, message = 0, "Did not work with an empty list"
    elif func(["M", "na", "i", "Jo"], ["y", "me", "s", "sh"]) != ['My', 'name', 'is', 'Josh']:
        error_code, message = 0, ""
    else:
        error_code, message = 0, ""
    return error_code, message
