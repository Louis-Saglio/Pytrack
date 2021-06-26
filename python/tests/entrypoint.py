import os
import sys


# Add the student submissions directory to the python path so we can import them later during the test process
sys.path.append('/jail/student')
sys.path.append('/app')

os.system('black -q -l 1000 /jail/student')

test_module = __import__(f"{os.environ['EXERCISE']}_test")
submitted_module = __import__(os.environ['EXERCISE'])


# todo : test that submission runs without exception (if not give traceback)
#   then run with tester and give only error message
#   don't show to the student the actual testing code to make cheating more difficult
test_module.main(submitted_module)
