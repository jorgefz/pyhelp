
import sys
import argparse
import importlib

def pyhelp():
    parser = argparse.ArgumentParser(
        prog = 'pyhelp',
        description = "Quick access to Python documentation from the command line",
        epilog = "Author: Jorge Fernandez. Check out the source code at github.com/jorgefz/pyhelp"
    )
    parser.add_argument('module')
    args = parser.parse_args()
    
    # try:
    #     importlib.import_module()
    
    help(args.module)


if __name__ == "__main__":
    pyhelp()
