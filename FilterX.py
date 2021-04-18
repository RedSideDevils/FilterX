import os 
import shutil
from settings import types
from colorama import Fore
from banner import banner

os.system("clear")

print(Fore.GREEN + banner)

def main():
    files = os.listdir()

    for file in files:
        for key, value in types.items():
            for i in range(len(value)):
                if file.endswith(value[i]):
                    if file == "FilterX.py" or file == "settings.py" or file == "banner.py":
                        continue

                    if value[i] in types[key]:
                        if not os.path.isdir(key):
                            q = input(Fore.RED + "Do you want to create new?(Y/N): ")
                            if q == "Y":
                                os.mkdir(key)
                                curdir = os.path.join(os.getcwd(), file)
                                new_dir = os.path.join(os.getcwd(), key, file)
                                shutil.move(curdir, new_dir)
                                print("\n" + Fore.YELLOW + "[~]File | " + Fore.GREEN + file + Fore.YELLOW + " | has been moved from | " + Fore.GREEN + curdir + Fore.YELLOW + " | to | " + Fore.GREEN + new_dir)
                            else:
                                print("[~]Then byee!")
                                exit()
                        else:
                            curdir = os.path.join(os.getcwd(), file)
                            new_dir = os.path.join(os.getcwd(), key, file)
                            shutil.move(curdir, new_dir)
                            print("\n" + Fore.YELLOW + "[~]File | " + Fore.GREEN + file + Fore.YELLOW + " | has been moved from | " + Fore.GREEN + curdir + Fore.YELLOW + " | to | " + Fore.GREEN + new_dir)

if __name__ == "__main__":
    main()
