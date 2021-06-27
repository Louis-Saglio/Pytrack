import inspect


def main(submitted_module):
    try:
        assert {"my_dict", "my_list", "my_tuple"}.issubset(dir(submitted_module)), "Missing mandatory variable"

        assert submitted_module.my_tuple == (42, "abc", True), "my_tuple is not correct"

        my_list = [(42, "abc", True), "lorem ipsum"]
        my_list.append(my_list)
        assert submitted_module.my_list[:-1] == [(42, "abc", True), "lorem ipsum"], "my_list is not correct"
        assert my_list[-1] == my_list, "my_list is not correct"

        assert submitted_module.my_dict == {"hello": "world", 42: None, True: False}, "my_dict is not correct"

        content = inspect.getsource(submitted_module)

        assert "my_tuple = (" in content, "my_tuple was not directly created with the literal syntax"
        assert "my_list = [" in content, "my_list was not directly created with the literal syntax"
        assert "my_dict = {" in content, "my_dict was not directly created with the literal syntax"
    except AssertionError as e:
        code, message = 1, str(e)
    else:
        code, message = 0, None
    return code, message
