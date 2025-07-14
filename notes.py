import colorama as c
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
        cmd = [i.lower().strip() for i in cmd]
        op = cmd[0]
        print(c.Fore.CYAN)
        if op == "help":

            print("Liste der Befehle:")
            print("-- new NAME")
            print("-- load MASTERNAME")
            print("-- add FILENAME")
if __name__ == "__main__":
    main()