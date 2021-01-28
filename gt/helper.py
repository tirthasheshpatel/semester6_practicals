import os
import sys
from beautify import bcolors

def main(flag):
    os.system("tput cols > tmp.pyhelper")
    with open("tmp.pyhelper", "r") as f:
        cols = f.read()
        cols = int(cols)
        chars = cols // 2 - 4
    os.system("rm tmp.pyhelper")
    if flag:
        print(bcolors.GREEN, end="")
        print(cols*"=")
        print(bcolors.ENDC, end="")
    else:
        str = chars*"="
        print("%s%s stdout %s%s" % (bcolors.GREEN, str, str, bcolors.ENDC))

if __name__ == "__main__":
    main(int(sys.argv[1]))
