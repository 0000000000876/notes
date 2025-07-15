import colorama as c
import os
import enc
def main():
    print("Programm Start...") #start
    c.init()
    global load
    global text
    global t_enc
    load = ""
    text = ""
    t_enc = 0
    print("Dieses Programm ist Konsolen basiert und benutzt eine prompt um deine entscheidungen auszuführen.")
    print("Benutze den Befehl 'help' um Hilfe zu erhalten")
    user = input("Benutzer?   " + c.Fore.GREEN)
    while True:
        print(c.Fore.LIGHTRED_EX,end='')
        print("~[" + c.Fore.GREEN + user + c.Fore.LIGHTRED_EX + "]$ " + c.Fore.YELLOW,end='')
        command = input()
        cmd = command.split(' ')
        op = cmd[0].lower()
        print(c.Fore.CYAN)
        if op == "help":

            print("Liste der Befehle:")
            print("-- new NAME")
            print("-- load MASTERNAME")
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
            if len(cmd) < 1:print("Fehler: Kein NAME gegeben")
            else:
                name = cmd[1]
                with open(f'{name}.tgb','w') as new:  #i did
                    new.write('0')
        if op == "load":
            if len(cmd) < 1:print("Fehler: Kein DATEINAME gegeben")
            else:
                fname = cmd[1]
                if load != "":
                    print("Fehler: Es ist bereits ein Tagebuch geladen, benutzen sie 'drop' um es zu entladen")
                else:
                    if not os.path.exists(fname):
                        print(f"Fehler: Datei '{fname}' existiert nicht")
                        print("# hinweis :: Bitte enden sie den Dateiname mit der '.tgb' Dateiendung.")
                    else:
                        load = fname # this line seems to destroy it
                        with open(load,'r') as tload:
                            lines = tload.readlines()
                            rtxt = "\n".join(lines)
                        if lines[0] == "0":
                            text = rtxt
                        else:
                            print("Passwort Notwendig!")
                            print(c.Fore.YELLOW)
                            pw = input(">> ")
                            print(c.Fore.CYAN )
                            etext = "\n".join(lines[1:])
                            text = enc.dec(etext,pw)
                        print("Datei erfolgreich geladen!")
        if op == "save":
            print("Bist du dir sicher du willst Speichern?")
            print(" JA -> Fortsetzen \n Irgendwas anderes -> Abbrechen")
            print(c.Fore.YELLOW)
            choice = input(">> ")
            print(c.Fore.CYAN)
            if choice.upper() == "JA":
                
                print("Wird geschpeichert...")
                if load == "":
                    print("Fehler: Keine Datei geladen. Benutzen sie 'load' um sie zu laden")
                else:
                    with open(load,"w") as temp_load:
                        temp_load.write(str(t_enc) + "\n" + text)
                        print("Fertig gespeichert!")
            else:
                print("OK. Prozess abgebrochen")
        if op == "drop":
            print("Bist du sicher das du die aktuelle Datenbank schließen willst?")
            print(" JA -> Fortsetzen \n Irgendwas anderes -> Abbrechen")
            print(c.Fore.YELLOW)
            choice = input(">> ")
            print(c.Fore.CYAN)
            if choice.upper() == "JA":
                print("Datenbank gelöscht")
                load = ""
            else:
                print("OK. Prozess abgebrochen")
        #i will test this app now
    input("Drücke enter um das programm zu Schließen...")
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(c.Style.RESET_ALL)
        print(c.Fore.LIGHTRED_EX)
        print("Fataler Fehler: Sie haben das programm durch Strg+C in den erzwungenen Auschaltezustand gebracht")
        try: input("Drücke enter um das Programm zu schließen...")
        except: pass
        exit()