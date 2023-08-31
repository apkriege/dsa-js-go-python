import subprocess
import sys

sys.dont_write_bytecode = True


def run_tests():
    subprocess.call(["python", "./Queue/_test.py"])
    subprocess.call(["python", "./DynamicArray/_test.py"])


if __name__ == "__main__":
    run_tests()
