import sys, os, subprocess

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
    print("Opea Language\n"
          "\n"
          "1. Run Project")
    choice = user_choice()
    if choice == "1":
        subprocess.call((sys.executable, "r.py"))
    else:
        main()

main()
