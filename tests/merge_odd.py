def main(namespace, src):
    func = namespace["main"]
    if func([1, 8, 9, 6, 3, 5], [2, 0, 4]) == [1, 0, 9, 3]:
        error_code, message = 0, ""
    else:
        error_code, message = 1, ""
    return error_code, message
