from test_file_reader import file_search
import sys

nuwt = ()

def asking():
    while True:
        nuwt = input("\nWhat are you looking for?\n\n").lower()
        if nuwt == "no":
            end()
        try:
            return file_search(nuwt)
        except FileNotFoundError:
            print(f"\n{nuwt} isn't in our files.\nPlease try again.\n")
           

def ask_again():
    while True:
            nuwt = input("\nAnything else?\n\n").lower()
            if nuwt == "no":
                end()
            try:
                return file_search(nuwt)
            except FileNotFoundError:
                print(f"\n{nuwt} isn't in our files.\nPlease try again.\n")
                

#def not_found():
    while True:
        nuwt == input(f"{nuwt} isn't in our files.\nPlease try again.\n\n")
        
        try:
            print(f"\n{file_search(nuwt)}\n\n")
            ask_again()
        except FileNotFoundError:
            not_found()
        if nuwt == ("no"):
            end()


def end():
    sys.exit()