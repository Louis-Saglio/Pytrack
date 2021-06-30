def main(namespace, src):
    try:
        assert {"my_dict", "my_list", "my_tuple"}.issubset(namespace.keys()), "Missing mandatory variable"

        assert namespace['my_tuple'] == (42, "abc", True), "my_tuple is not correct"

        my_list = [(42, "abc", True), "lorem ipsum"]
        my_list.append(my_list)
        assert namespace['my_list'][:-1] == [(42, "abc", True), "lorem ipsum"], "my_list is not correct"
        assert my_list[-1] == my_list, "my_list is not correct"

        assert namespace['my_dict'] == {"hello": "world", 42: None, True: False}, "my_dict is not correct"

        assert "my_tuple = (" in src, "my_tuple was not directly created with the literal syntax"
        assert "my_list = [" in src, "my_list was not directly created with the literal syntax"
        assert "my_dict = {" in src, "my_dict was not directly created with the literal syntax"
    except AssertionError as e:
        code, message = 1, str(e)
    else:
        code, message = 0, None
    return code, message
