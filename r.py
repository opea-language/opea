import sys, os, subprocess
from data.projects import io

IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"

def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")

def user_choice():
    return input("\n>>> ").lower().strip()

def main():
    clear_screen()
    print("Opea Run File\n"
          "\n"
          "What file would you like to run?\n")
    subprocess.call(("dir", "data/projects"))
    choice = user_choice()
    if choice == "io.py":
        input("why are you here?")
        sys.exit()
    else:
        if ".op" in choice:
            l = 0
            clear_screen()
            try:
                file = open("data/projects/{}".format(choice), "r")
            except:
                input("Can't find the file {}".format(choice))
                subprocess.call((sys.executable, "opea.py"))
            for line in file:
                try:
                    l += 1
                    eval(line)
                except:
                    io.echo("\nERR Line: {}\n".format(l))
            file.close()
            input("Code Concluded")
            subprocess.call((sys.executable, "opea.py"))
        if ".oe" in choice:
            l = 0
            clear_screen()
            try:
                file = open("data/projects/{}".format(choice), "r")
            except:
                input("Can't find the file {}".format(choice))
                subprocess.call((sys.executable, "opea.py"))
            for line in file:
                try:
                    l += 1
                    eval(line)
                except:
                    io.echo("\nERR Line: {}\n".format(l))
            file.close()
            input("Code Concluded")
            subprocess.call((sys.executable, "opea.py"))
        else:
            input("Unknown File type")
            subprocess.call((sys.executable, "opea.py"))

main()
