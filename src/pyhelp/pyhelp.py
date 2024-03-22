
import sys
import argparse
import importlib
import pydoc

def pyhelp():
    parser = argparse.ArgumentParser(
        prog = 'pyhelp',
        description = "Quick access to Python documentation from the command line",
        epilog = "Author: Jorge Fernandez. Check out the source code at github.com/jorgefz/pyhelp"
    )
    parser.add_argument('module')
    parser.add_argument('-i', "--interactive", action="store_true", help="Open interactive session")
    args = parser.parse_args()
    
    # module_hierarchy = args.module.rsplit('.')
    # module_name = module_hierarchy[0]

    if args.interactive:    
        help(args.module)
    else:
        docs = pydoc.render_doc(args.module, renderer=pydoc.plaintext)
        print(docs)

if __name__ == "__main__":
    pyhelp()
