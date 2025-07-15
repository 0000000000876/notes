import colorama as c
import os
def main():
    print("Programm Start...") #start
    c.init()
    global load
    load = 0
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
            print("-- save")
            print("-- drop")
            print("-- exit")
        if op == "exit":
            print("Auf wiedersehen!")
            break
        if op == "new":
            name = cmd[1]
            with open(f'{name}.tgb','w') as new:  #i did
                new.write('0')
        if op == "load":
            fname = cmd[1]
            if load != 0:
                print("Fehler: Es ist bereits ein Tagebuch geladen, benutzen sie 'drop' um es zu entladen")
            else:
                if not os.path.exists(fname):
                    print(f"Fehler: Datei '{fname}' existiert nicht")
                else:
                    load = open(fname,'a+')
                    if load.readlines[0] == "0":
                        print("Datei erfolgreich geladen!")
                    else:
                        print("Passwort Notwendig!")
                        print(c.Fore.YELLOW)
                        pw = input()
                        #decrypt here ig
    input("Drücke enter um das programm zu Schließen...")
if __name__ == "__main__":
    main()