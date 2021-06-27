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

global_test_script = [
    # By default cython expect Python2 code
    "#cython: language_level=3",
    # We need to add this dir to the path because it will contain the student submissions that we will want to import
    "import sys",
    "sys.path.append('/jail/student')",
]

# Concatenate all the test files into one big file that we will transpile to C using cython and then compile to a binary
# There is probably a cleaner way to achieve this by compiling python modules to C library (.so)
tests_directory = 'tests'
for file_name in os.listdir(tests_directory):
    with open(os.path.join(tests_directory, file_name)) as f:
        script = f.read()
    module_name = os.path.splitext(file_name)[0]
    # Rename the main function into the name of the exercise it tests, we will use this name to run the appropriate
    # test function later
    script = script.replace("def main(submitted_module):", f"def {module_name}(submitted_module):")
    global_test_script.append(script)

global_test_script.extend(
    [
        # Load the student submission and give it as an argument to the test function
        "import os",
        "code, message = globals()[os.environ['EXERCISE']](__import__(os.environ['EXERCISE']))",
        # Display any error message it returned
        "if message:sys.stdout.write(message)",
        # And exit with the appropriate response
        "exit(code)",
    ]
)

# Write the generated global test script
with open('test/test.py', 'w') as f:
    f.write('\n'.join(global_test_script))

# Transpile it to C
os.system("cython test/test.py --embed -o test/test.c")
# Compile the generated C code
os.system(
    "gcc -Os -I /usr/include/python3.9 -o test/test test/test.c -lpython3.9 -lpthread -lm -lutil -ldl"
)
# Build the docker image
os.system("docker build -t pytrack .")

