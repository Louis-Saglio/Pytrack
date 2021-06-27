import os

global_test_script = [
    "#cython: language_level=3",
    "import sys",
    "sys.path.append('/jail/student')",
]

tests_directory = '/home/louis/PycharmProjects/Pytrack/python/tests'
for file_name in os.listdir(tests_directory):
    with open(os.path.join(tests_directory, file_name)) as f:
        script = f.read()
        module_name = os.path.splitext(file_name)[0]
        script = script.replace("def main(submitted_module):", f"def {module_name}(submitted_module):")
        global_test_script.append(script)

global_test_script.extend(
    [
        "import os",
        "code, message = globals()[os.environ['EXERCISE']](__import__(os.environ['EXERCISE']))",
        "if message:sys.stdout.write(message)",
        "exit(code)",
    ]
)

with open('test/test.py', 'w') as f:
    f.write('\n'.join(global_test_script))

os.system("cython test/test.py --embed -o test/test.c")
os.system(
    "gcc -Os -I /usr/include/python3.9 -o test/test test/test.c -lpython3.9 -lpthread -lm -lutil -ldl"
)
os.system("docker build -t pytrack .")

