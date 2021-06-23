import exercise_1

assert {"my_dict", "my_list", "my_tuple"}.issubset(dir(exercise_1)), "Missing mandatory variable"


assert exercise_1.my_tuple == (42, "abc", True), "my_tuple is not correct"

my_list = [(42, "abc", True), "lorem ipsum"]
my_list.append(my_list)
assert exercise_1.my_list[:-1] == [(42, "abc", True), "lorem ipsum"], "my_list is not correct"
assert my_list[-1] == my_list, "my_list is not correct"

assert exercise_1.my_dict == {"hello": "world", 42: None, True: False}, "my_dict is not correct"


with open("exercise_1.py") as f:
    content = f.read()

assert "my_tuple = (" in content, "my_tuple was not directly created with the literal syntax"
assert "my_list = [" in content, "my_list was not directly created with the literal syntax"
assert "my_dict = {" in content, "my_dict was not directly created with the literal syntax"
