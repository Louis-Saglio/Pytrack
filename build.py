"""
This build script creates a binary which is able to test any student submission,
and include it into docker image tailored for Ytrack.
We want to build a binary instead of a Python script to avoid cheating made possible be student code being able to read
the test code.
If you want to run a Python script it *must* have the r right, you cannot just give it the x right.
To work around this limitation we use Cython and GCC to compile the Python script into a binary which can be executed
without the r right.
There is probably an other way of preventing student submitted code from reading the test code by using the user system.
However this will probably be difficult to achieve because Ytrack messes with the uid:gid used to run the container.
"""


import os
import string
from random import choices

os.system("black -l 120 .")

prefix = "".join(choices(string.ascii_lowercase, k=10))

global_test_script = f"""
#cython: language_level=3
import sys, os, black
"""

with open("utils.py") as f:
    global_test_script += f.read()

# Concatenate all the test files into one big file that we will transpile to C using cython and then compile to a binary
# There is probably a cleaner way to achieve this by compiling python modules to C library (.so)
tests_directory = "tests"
for file_name in os.listdir(tests_directory):
    with open(os.path.join(tests_directory, file_name)) as f:
        script = f.read().replace("from utils", "#")
    module_name = os.path.splitext(file_name)[0]
    # Rename the main function into the name of the exercise it tests, we will use this name to run the appropriate
    # test function later
    script = script.replace("def main(namespace, src):", f"def {prefix}_{module_name}(namespace, src):")
    script = script.replace("def rewrite(src):", f"def {prefix}_{module_name}_rewrite(src):")
    global_test_script += script

global_test_script += f"""
''
with open(f"/jail/student/{{os.environ['EXERCISE']}}.py") as f:
    src = f.read()
try:
    src = black.format_str(src, mode=black.FileMode())
except black.parsing.InvalidInput:
    code, message = 1, 'Erreur de syntaxe'
else:
    rewrite_func = globals().get(f"{prefix}_{{os.environ['EXERCISE']}}_rewrite")
    if rewrite_func:
        src = rewrite_func(src)
    submitted_module_namespace = {{}}
    eval(compile(src, '<submitted_module>', 'exec'), {{}}, submitted_module_namespace)
    try:
        code, message = globals()[f"{prefix}_{{os.environ['EXERCISE']}}"](submitted_module_namespace, src)
    except AssertionError as e:
        code, message = 1, str(e)
if message:sys.stdout.write(message)
exit(code)
"""

# Write the generated global test script
if not os.path.isdir("test"):
    os.mkdir("test")
with open("test/test.py", "w") as f:
    f.write(global_test_script)

# Transpile it to C
os.system("cython test/test.py --embed -o test/test.c")
# Compile the generated C code
os.system("gcc -Os -I /usr/include/python3.10 -o test/test test/test.c -lpython3.10 -lpthread -lm -lutil -ldl")
# Build the docker image
os.system("docker build -t pytrack .")
