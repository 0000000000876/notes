import colorama as c
import os
def main():
    print("Programm Start...")
    c.init()
    print("Dieses Programm ist Konsolen basiert und benutzt eine prompt um deine entscheidungen auszuführen.")
    print("Benutze den Befehl 'help' um Hilfe zu erhalten")
    user = input("Benutzer?   ")
    while True:
        print(c.Fore.LIGHTRED_EX,end='')
        print("~[" + c.Fore.GREEN + user + c.Fore.LIGHTMAGENTA_EX + "]$ " + c.Fore.YELLOW,end='')
        command = input()
        cmd = command.split(' ')
        op = cmd[0].lower()
        print(c.Fore.CYAN)
        if op == "help":

            print("Liste der Befehle:")
            print("-- new NAME")
            print("-- link MASTERNAME")
            print("-- add FILENAME")
            print("-- addraw TEXT")
            print("-- enc PASSWORD")  #TODO: Maybe change the password system so it is censored while the user is typing(like just enc and then later then password using idk password.input or smth
            print("-- drop")
            print("-- exit")
        if op == "exit":
            print("Auf wiedersehen!")
            break
        if op == "new":
            name = cmd[1]
            with open(f'{name}.dbk','w') as new:  #maybe we will be changing extension idk
                new.write('0')
    input("Drücke enter um das programm zu Schließen...")
if __name__ == "__main__":
    main()