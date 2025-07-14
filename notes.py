import colorama as c
def main():
    print("Programm Start...")
    c.init()
    print("Dieses Programm ist Konsolen basiert und benutzt eine prompt um deine entscheidungen auszuführen.")
    print("Benutze den Befehl 'help' um Hilfe zu erhalten")
    user = input("Benutzer?   ")
    while True:
        print(c.Style.RESET_ALL,end='')
        print("~[" + user + "]$ ",end=c.Fore.YELLOW)
        command = input() #add logic later
if __name__ == "__main__":
    main()