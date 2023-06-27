import os, time, socket, string, random, itertools, pyperclip, psutil, uuid, json, shutil, ctypes, qrcode
from PIL import Image

ctypes.windll.kernel32.SetConsoleTitleW("GOTCHA")

class color:
    GRAY = '\033[90m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PINK = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m' 

def cls():
    os.system("cls")

def banner():
    print(color.RESET)
    print("                                    ██████╗  █████╗ ████████╗ █████╗ ██╗  ██╗ █████╗ ")
    print("                                   ██╔════╝ ██╔══██╗╚══██╔══╝██╔══██╗██║  ██║██╔══██╗")
    print("                                   ██║  ██╗ ██║  ██║   ██║   ██║  ╚═╝███████║███████║")
    print("                                   ██║   ██╗██║  ██║   ██║   ██║  ██╗██╔══██║██╔══██║")
    print("                                   ╚██████╔╝╚█████╔╝   ██║   ╚█████╔╝██║  ██║██║  ██║")
    print("                                    ╚═════╝  ╚════╝    ╚═╝    ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝")
    print()

def passwort_gen():
    chars1 = string.ascii_letters + string.digits
    chars2 = chars1 + "!§$%&/=-_"

    pw_count = int(input("[" + color.PINK + ">" + color.RESET + "] - Anzahl: " + color.PINK))
    pw_length = int(input(color.RESET + "[" + color.PINK + ">" + color.RESET + "] - Länge: " + color.PINK))
    pw_symbols = input(color.RESET + "[" + color.PINK + ">" + color.RESET + "] - Sonderzeichen (Y/N): " + color.PINK)

    cls()
    banner()

    for i in range(0, pw_count):
        password = ""
        for j in range(0, pw_length):
            if pw_symbols.lower() == "y": 
                pw_characters = random.choice(chars2)
                password = password + pw_characters
            else:
                pw_characters = random.choice(chars1)
                password = password + pw_characters
        print(color.RESET + "[" + color.PINK + ">" + color.RESET + "] - Password generiert:" , color.PINK + password)
        with open ("passes.txt", "a") as f:
            f.write(f"{i + 1} - {password[::-1]} \n")
        time.sleep(0.1)
        
def koz():
    def load_stats():
        try:
            with open("stats.json", "r") as f:
                return json.load(f)
        except:
            return {"wins": 0, "rounds": 0, "loses": 0, "winstreak": 0}

    def update_stats(stats, win):
            stats["rounds"] += 1

            if win:
                stats["wins"] += 1
                stats["winstreak"] += 1
            else:
                stats["loses"] += 1
                stats["winstreak"] = 0

            with open("stats.json", "w") as f:
                json.dump(stats, f)
            return stats

    def game():
        cls()
        banner()    

        stats = load_stats()
        try_again = "ja"
        auswahl = ["Kopf", "Zahl"]

        while try_again == "ja" or try_again == "j":
            cls()
            banner()

            user_choice = str(input("[" + color.PINK + ">" + color.RESET + "] - Kopf oder Zahl: " + color.PINK)).capitalize()
            if user_choice not in auswahl:
                cls()
                banner()
                print(color.RESET + "[" + color.RED + ">" + color.RESET + "] - Ungültige Eingabe. Probiere es nochmal!")
                print()
                input("Drücke Enter, um fortzufahren...")
                cls()
                continue

            cls()
            banner()

            bot_choice = random.choice(auswahl)

            if user_choice.lower() == bot_choice.lower():
                print(color.RESET + "[" + color.PINK + ">" + color.RESET + "] - Du:      " + color.PINK + user_choice.capitalize())
                print(color.RESET + "[" + color.PINK + ">" + color.RESET + "] - Bot:     " + color.PINK + bot_choice)
                print()
            else:
                print(color.RESET + "[" + color.PINK + ">" + color.RESET + "] - Du:      " + color.PINK + user_choice.capitalize())
                print(color.RESET + "[" + color.PINK + ">" + color.RESET + "] - Bot:     " + color.RED + bot_choice)
                print()

            if user_choice.lower() == bot_choice.lower():
                stats = update_stats(stats, True)
                winrate = 100 * stats["wins"] / stats["rounds"]
                print(color.RESET + "[" + color.GREEN + ">" + color.RESET + "] - Du hast gewonnen!")
                print()
                print("----------STATS----------")
                print("[" + color.PINK + ">" + color.RESET + "] - Runden   : " + color.PINK, stats["rounds"])
                print(color.RESET + "[" + color.PINK + ">" + color.RESET + "] - Wins     : " + color.PINK, stats["wins"])
                print(color.RESET + "[" + color.PINK + ">" + color.RESET + "] - Loses    : " + color.PINK, stats["loses"])
                print(color.RESET + "[" + color.PINK + ">" + color.RESET + "] - Winstreak: " + color.PINK, stats["winstreak"])
                print(color.RESET + "[" + color.PINK + ">" + color.RESET + "] - Winrate  : " + color.PINK + " {0:.0f}".format(winrate) + color.RESET + "%")
                print(color.RESET + "----------STATS----------")
            else:
                stats = update_stats(stats, False)
                winrate = 100 * stats["wins"] / stats["rounds"]
                print(color.RESET + "[" + color.RED + ">" + color.RESET + "] - Du hast verloren!")
                print()
                print("----------STATS----------")
                print("[" + color.PINK + ">" + color.RESET + "] - Runden   : " + color.PINK, stats["rounds"])
                print(color.RESET + "[" + color.PINK + ">" + color.RESET + "] - Wins     : " + color.PINK, stats["wins"])
                print(color.RESET + "[" + color.PINK + ">" + color.RESET + "] - Loses    : " + color.PINK, stats["loses"])
                print(color.RESET + "[" + color.PINK + ">" + color.RESET + "] - Winstreak: " + color.PINK, stats["winstreak"])
                print(color.RESET + "[" + color.PINK + ">" + color.RESET + "] - Winrate  : " + color.PINK + " {0:.0f}".format(winrate) + color.RESET + "%")
                print(color.RESET + "----------STATS----------")
            print()
            try_again = input("[" + color.PINK + ">" + color.RESET + "] - Nochmal spielen? (ja/nein): " + color.PINK).lower()
            print(color.RESET)
            if try_again != "ja":
                cls()
            elif try_again != "j":
                cls()
    game()

def bruteforce():
    passwort = input("[" + color.PINK + ">" + color.RESET + "] - Passwort: " + color.PINK)

    # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    buchstaben = " " + string.ascii_letters + string.digits + string.punctuation

    print(color.RESET)

    def find_passwort(passwort: str) -> str:
        try:
            start_1 = time.time()
            num_versuch = 0
            for num in range(1, 10):
                start_2 = time.time()
                for versuch in itertools.product(buchstaben, repeat=num):
                    versuch = "".join(versuch)
                    num_versuch += 1
                    if versuch == passwort:
                        ende_1 = time.time()
                        zeit_1 = ende_1 - start_1
                        if zeit_1 < 60:
                            print()
                            print("-----------------------------------")
                            print()
                            print("[" + color.GREEN + ">" + color.RESET + "] - PASSWORT GEFUNDEN" + color.RESET)
                            print()
                            print("---------------STATS---------------")
                            print("[" + color.PINK + ">" + color.RESET + "] - Passwort: " + color.PINK + "{}".format(versuch) + color.RESET)
                            print("[" + color.PINK + ">" + color.RESET + "] - Versuche: " + color.PINK + "{}".format(num_versuch) + color.RESET)
                            print("[" + color.PINK + ">" + color.RESET + "] - Zeit    : " + color.PINK + "{0:.1f}".format(zeit_1) + color.RESET + " seconds")
                            print("---------------STATS---------------")
                        elif zeit_1 > 60:
                            print()
                            print("-----------------------------------")
                            print()
                            print("[" + color.GREEN + ">" + color.RESET + "] - PASSWORT GEFUNDEN" + color.RESET)
                            print()
                            print("---------------STATS---------------")
                            print("[" + color.PINK + ">" + color.RESET + "] - Passwort: " + color.PINK + " {}".format(versuch) + color.RESET)
                            print("[" + color.PINK + ">" + color.RESET + "] - Versuche: " + color.PINK + " {}".format(num_versuch) + color.RESET)
                            print("[" + color.PINK + ">" + color.RESET + "] - Zeit    : " + color.PINK + " {0:.1f}".format(zeit_1 / 60) + color.RESET + " minutes")
                            print("---------------STATS---------------")
                        elif zeit_1 > 3600:
                            print()
                            print("-----------------------------------")
                            print()
                            print("[" + color.GREEn + ">" + color.RESET + "] - PASSWORT GEFUNDEN" + color.RESET)
                            print()
                            print("---------------STATS---------------")
                            print("[" + color.PINK + ">" + color.RESET + "] - Passwort: " + color.PINK + " {}".format(versuch) + color.RESET)
                            print("[" + color.PINK + ">" + color.RESET + "] - Versuche: " + color.PINK + " {}".format(num_versuch) + color.RESET)
                            print("[" + color.PINK + ">" + color.RESET + "] - Zeit    : " + color.PINK + " {0:.1f}".format(zeit_1 / 120) + color.RESET + " hours")
                            print("---------------STATS---------------")
                        return
                    
                ende_2 = time.time()
                zeit_2 = ende_2 - start_2
                if zeit_2 < 60:
                    print("[" + color.PINK + ">" + color.RESET + "] - {}".format(versuch) + " - " + color.PINK + "{0:.1f}".format(zeit_2) + color.RESET + " seconds")
                elif zeit_2 > 60:
                    print("[" + color.PINK + ">" + color.RESET + "] - {}".format(versuch) + " - " + color.PINK + "{0:.1f}".format(zeit_2 / 60) + color.RESET + " minutes")
                elif zeit_2 > 3600:
                    print("[" + color.PINK + ">" + color.RESET + "] - {}".format(versuch) + " - " + color.PINK + "{0:.1f}".format(zeit_2 / 120) + color.RESET + " hours")
        except KeyboardInterrupt:
            cls()
            banner()
            print("[" + color.RED + ">" + color.RESET + "] - Der Vorgang wurde abgebrochen!")
            print()
            print("[" + color.PINK + ">" + color.RESET + "] - Versuche: " + color.PINK + "{}".format(num_versuch) + color.RESET)
            print("[" + color.PINK + ">" + color.RESET + "] - Versuch : " + color.PINK + "{}".format(versuch) + color.RESET)

        return
    find_passwort(passwort)

def pc_specs():
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage("C:\\")

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    local_ip = s.getsockname()[0]
    pyperclip.copy(local_ip)

    mac_num = hex(uuid.getnode()).replace('0x', '').upper()
    mac = ':'.join(mac_num[i : i + 2] for i in range(0, 11, 2))
    
    print(color.RESET + "[" + color.PINK + ">" + color.RESET + "] - IP-Adresse     : " + color.PINK + "{}".format(local_ip))
    print(color.RESET + "[" + color.PINK + ">" + color.RESET + "] - MAC-Adresse    : " + color.PINK + "{}".format(mac))
    print(color.RESET + "[" + color.PINK + ">" + color.RESET + "] - Benutzer       : " + color.PINK + os.getlogin())
    print(color.RESET + "[" + color.PINK + ">" + color.RESET + "] - Speicher       :" + color.PINK, "{0:.0f}".format(disk.total / 1024 ** 3), color.RESET + "GB")
    print(color.RESET + "[" + color.PINK + ">" + color.RESET + "] - Freier Speicher:" + color.PINK, "{0:.0f}".format(disk.free / 1024 ** 3), color.RESET + "GB")
    print(color.RESET + "[" + color.PINK + ">" + color.RESET + "] - CPU Kerne      :" + color.PINK, psutil.cpu_count(logical=True))
    print(color.RESET + "[" + color.PINK + ">" + color.RESET + "] - RAM            :" + color.PINK, "{0:.0f}".format(mem.total / 1024 ** 3), color.RESET + "GB")
       
def error_troll():
    text = "MsgBox \"Kritischen Fehler gefunden\", 0+16, \"Fehlermeldung\""
    startup = os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\fehler.vbs")

    try:
        with open("fehler.vbs", "w") as file:
            file.write(text)
        print("[" + color.PINK + ">" + color.RESET + "] - Die Datei wurde erfolgreich" + color.PINK + " erstellt" + color.RESET + "!")
    except:
        print("[" + color.RED + ">" + color.RESET + "] - Die Datei konnte nicht ersellt werden!")

    time.sleep(0.5)

    try:
        shutil.copy("fehler.vbs", startup)
        print("[" + color.PINK + ">" + color.RESET + "] - Die Datei wurde erfolgreich" + color.PINK + " kopiert" + color.RESET + "!")
    except:
        print("[" + color.RED + ">" + color.RESET + "] - Die Datei konnte nicht kopiert werden!")

    time.sleep(0.5)
    
    try:
        os.remove("fehler.vbs")
        print("[" + color.PINK + ">" + color.RESET + "] - Die Datei wurde erfolgreich" + color.PINK + " gelöscht" + color.RESET + "!")
    except:
        print("[" + color.RED + ">" + color.RESET + "] - Die Datei konnte nicht gelöscht werden!")

def flooder():
    counter = 0

    dir_name = input("[" + color.PINK + ">" + color.RESET + "] - Wo soll geflooded werden: C:\\Users\\" + os.getlogin() + "\\" + color.PINK)
    
    while True:
            try:
                directory = "FlOOLDER_" + str(counter)
                parent_dir = "C:\\Users\\" + os.getlogin() + "\\" + dir_name
                path = os.path.join(parent_dir, directory)
                os.makedirs(path)
                counter += 1
                print("[" + color.PINK + ">" + color.RESET + "] - Ordner erstellt: " + color.PINK + path + color.RESET)
            except KeyboardInterrupt:
                cls()
                banner()
                print("[" + color.PINK + ">" + color.RESET + "] - Es wurden erfolgreich" + color.PINK, counter, color.RESET + "Ordner erstellt!")
                break
            except FileExistsError:
                cls()
                banner()
                print("[" + color.RED + ">" + color.RESET + "] - Hier wurde bereits geflooded!")
                break

def qr_gen():
    qr_name = input("[" + color.PINK + ">" + color.RESET + "] - Titel des QR-Codes: " + color.PINK)
    qr_data = input(color.RESET + "[" + color.PINK + ">" + color.RESET + "] - Website oder Text für den QR-Code: " + color.PINK)
    
    qr = qrcode.QRCode(version=3, box_size=10, border=1)
    qr.add_data(qr_data)
    qr.make(fit=True)

    img = qr.make_image(fill=("black"), back_color="#e47aea")
    img.save(qr_name+ '.png')

    cls()
    banner()

    print("[" + color.PINK + ">" + color.RESET + "] - Dein QR-Code \"" + color.PINK + qr_name + color.RESET + "\" wurde erfolgreich erstellt!")
    with Image.open(qr_name + ".png") as image:
        image.show()

def gnum():
    cls()
    banner()

    number = random.randint(1, 100)
    attempts = 0

    print()
    print("[" + color.PINK + ">" + color.RESET + "] - Ich denke an eine Zahl zwischen " + color.PINK + "1" + color.RESET + " und " + color.PINK + "100." + color.RESET)

    while True:
        if attempts >= 1:
            if guess < number:
                cls()
                banner()
                print(color.RESET + "[" + color.RED + ">" + color.RESET + "] - Letzter Versuch: " + color.PINK + f"{guess}" + color.RESET +  " (zu niedrig)")
            elif guess > number:
                cls()
                banner()
                print(color.RESET + "[" + color.RED + ">" + color.RESET + "] - Letzter Versuch: " + color.PINK + f"{guess}" + color.RESET + " (zu hoch)")
            guess = int(input("[" + color.PINK + ">" + color.RESET + "] - Gebe deine Vermutung ein: " + color.PINK))
        else:
            guess = int(input("[" + color.PINK + ">" + color.RESET + "] - Gebe deine Vermutung ein: " + color.PINK))
        attempts += 1

        if guess == number:
            cls()
            banner()
            print("[" + color.GREEN + ">" + color.RESET + "] - Glückwunsch! Du hast die Zahl " + color.PINK + f"{number}" + color.RESET + " in " + color.PINK + f"{attempts}" + color.RESET + " Versuchen erraten!")
            break

    play_again = input("[" + color.PINK + ">" + color.RESET + "] - Nochmal spielen? (ja/nein): ")
    if play_again.lower() == "ja" or play_again.lower() == "j":
        gnum()

def gtxt():
    cls()
    banner()
    
    words =  ['Bananenbieger', 'Apfel', 'Banane', 'Orange', 'Mango', 'Ananas', 'Erdbeere', 'Kirsche', 'Pfirsich', 'Birne', 'Traube', 'Zitrone', 'Himbeere', 'Blaubeere', 'Melone', 'Kiwi', 'Granatapfel', 'Avocado', 'Papaya', 'Passionsfrucht', 'Feige', 'Guave', 'Mandarine', 'Pflaume', 'Aprikose', 'Brombeere', 'Limette', 'Heidelbeere', 'Kaktusfeige', 'Grapefruit', 'Litschi', 'Holunderbeere', 'Stachelbeere', 'Johannisbeere', 'Physalis', 'Pomelo', 'Nektarine', 'Maracuja', 'Kokosnuss', 'Cranberry', 'Wassermelone']
    word = random.choice(words).lower()
    attempts = 0
    guessed = []

    print()
    print("[" + color.PINK + ">" + color.RESET + "] - Ich denke an eine Frucht mit" + color.PINK, len(word), "" + color.RESET + "Buchstaben. Kannst du sie erraten? ")

    while True:
        masked_word = ""
        for letter in word:
            if letter in guessed:
                masked_word += letter
            else:
                masked_word += "_"

        guess = input("[" + color.PINK + ">" + color.RESET + "] - Gebe deine Vermutung ein: " + color.PINK)
        attempts += 1

        if guess.casefold() == word.casefold():
            cls()
            banner()
            print(color.RESET + "[" + color.GREEN + ">" + color.RESET + "] - Glückwunsch! Du hast das Wort " + color.PINK + word.capitalize() + color.RESET + " in " + color.PINK + f"{attempts}" + color.RESET + " Versuchen erraten!")
            break
        elif len(guess) != 1:
            cls()
            banner()
            print(color.RESET + "[" + color.RED + ">" + color.RESET + "] - Bitte geben Sie nur einen einzelnen Buchstaben ein.")
            print(color.RESET + "[" + color.PINK + ">" + color.RESET + "] - Fortschritt:", masked_word)
            continue

        if guess in guessed:
            cls()
            banner()
            print(color.RESET + "[" + color.RED + ">" + color.RESET + "] - Sie haben diesen Buchstaben bereits erraten. Versuchen Sie es erneut.")
            print(color.RESET + "[" + color.PINK + ">" + color.RESET + "] - Fortschritt:", masked_word)
            continue

        guessed.append(guess)

        if guess in word:
            cls()
            banner()
            print(color.RESET + "[" + color.GREEN + ">" + color.RESET + "] - Richtig")
        else:
            cls()
            banner()
            print(color.RESET + "[" + color.RED + ">" + color.RESET + "] - Falsch")

        masked_word = ""
        for letter in word:
            if letter in guessed:
                masked_word += letter
            else:
                masked_word += "_"

        print(color.RESET + "[" + color.PINK + ">" + color.RESET + "] - Fortschritt:", masked_word)

        if masked_word == word:
            cls()
            banner()
            print(color.RESET + "[" + color.GREEN + ">" + color.RESET + "] - Glückwunsch! Du hast das Wort " + color.PINK + word.capitalize() + color.RESET + " in " + color.PINK + f"{attempts}" + color.RESET + " Versuchen erraten!")
            break

    play_again = input(color.RESET + "[" + color.PINK + ">" + color.RESET + "] - Nochmal spielen? (ja/nein): ")
    if play_again.lower() == "ja" or play_again.lower() == "j":
        gtxt()

def reset_all():
    try:
        os.remove("stats.json")
        print("[" + color.GREEN + ">" + color.RESET + "] - Die " + color.PINK + "KoZ" + color.RESET + " Stats wurden erfolgreich gelöscht!")
    except FileNotFoundError:
        print("[" + color.RED + ">" + color.RESET + "] - Die " + color.PINK + "KoZ" + color.RESET + " Stats wurden bereits gelöscht!")
    except:
        print("[" + color.RED + ">" + color.RESET + "] - Die " + color.PINK + "KoZ" + color.RESET + " Stats konnten nicht gelöscht werden!")

    time.sleep(0.5)

    try:
        with open("passes.txt") as myfile:
            total_lines = sum(1 for line in myfile)
    except FileNotFoundError:
        pass

    try:
        os.remove("passes.txt")
        print("[" + color.GREEN + ">" + color.RESET + "] - Es wurden " + color.PINK + "{}".format(total_lines) + color.RESET + "/" + color.PINK + "{}".format(total_lines) + color.RESET + " Passwörter gelöscht!")
    except FileNotFoundError:
        print("[" + color.RED + ">" + color.RESET + "] - Die " + color.PINK + "Passwörter" + color.RESET + " wurden bereits gelöscht!")
    except:
        print("[" + color.RED + ">" + color.RESET + "] - Die " + color.PINK + "Passwörter"  +color.RESET + "konnten nicht gelöscht werden!")

    time.sleep(0.5)

    startup = os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\fehler.vbs")

    try:
        os.remove(startup)
        print("[" + color.GREEN + ">" + color.RESET + "] - Das " + color.PINK + "Error-Skript" + color.RESET + " wurde erfolgreich gelöscht!")
    except FileNotFoundError:
        print("[" + color.RED + ">" + color.RESET + "] - Das " + color.PINK + "Error-Skript" + color.RESET + " wurde bereits gelöscht!")
    except:
        print("[" + color.RED + ">" + color.RESET + "] - Das " + color.PINK + "Error-Skript" + color.RESET + " konnte nicht gelöscht werden!")

    time.sleep(0.5)
    
    try:
        root_dir = "C:\\Users\\" + os.getlogin()
        folders_deleted = False

        for root, dirs, files in os.walk(root_dir):
            for folder in dirs:
                if folder.startswith("FlOOLDER_"):
                    folders_deleted = True
                    folder_path = os.path.join(root, folder)
                    os.rmdir(folder_path)
        if folders_deleted:
            print("[" + color.GREEN + ">" + color.RESET + "] - Die " + color.PINK + "Flooder" + color.RESET + " wurden erfolgreich gelöscht!")
        else:
            print("[" + color.RED + ">" + color.RESET + "] - Die " + color.PINK + "Flooder" + color.RESET + " wurden bereits gelöscht!")
    except:
        print("[" + color.RED + ">" + color.RESET + "] - Die " + color.PINK + "Flooder" + color.RESET + " konnten nicht gelöscht werden!")      

def reset_passes():
    try:
        with open("passes.txt") as myfile:
            total_lines = sum(1 for line in myfile)
    except FileNotFoundError:
        pass

    try:
        os.remove("passes.txt")
        print("[" + color.GREEN + ">" + color.RESET + "] - Es wurden " + color.PINK + "{}".format(total_lines) + color.RESET + "/" + color.PINK + "{}".format(total_lines) + color.RESET + " Passwörter gelöscht!")
    except FileNotFoundError:
        print("[" + color.RED + ">" + color.RESET + "] - Die " + color.PINK + "Passwörter" + color.RESET + " wurden bereits gelöscht!")
    except:
        print("[" + color.RED + ">" + color.RESET + "] - Die " + color.PINK + "Passwörter"  +color.RESET + "konnten nicht gelöscht werden!")

def reset_stats():
    try:
        os.remove("stats.json")
        print("[" + color.GREEN + ">" + color.RESET + "] - Die " + color.PINK + "KoZ" + color.RESET + " Stats wurden erfolgreich gelöscht!")
    except FileNotFoundError:
        print("[" + color.RED + ">" + color.RESET + "] - Die " + color.PINK + "KoZ" + color.RESET + " Stats wurden bereits gelöscht!")
    except:
        print("[" + color.RED + ">" + color.RESET + "] - Die " + color.PINK + "KoZ" + color.RESET + " Stats konnten nicht gelöscht werden!")

def reset_error():
    startup = os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\fehler.vbs")

    try:
        os.remove(startup)
        print("[" + color.GREEN + ">" + color.RESET + "] - Das " + color.PINK + "Error-Skript" + color.RESET + " wurde erfolgreich gelöscht!")
    except FileNotFoundError:
        print("[" + color.RED + ">" + color.RESET + "] - Das " + color.PINK + "Error-Skript" + color.RESET + " wurde bereits gelöscht!")
    except:
        print("[" + color.RED + ">" + color.RESET + "] - Das " + color.PINK + "Error-Skript" + color.RESET + " konnte nicht gelöscht werden!")

def reset_flooder():
    try:
        root_dir = "C:\\Users\\" + os.getlogin()
        folders_deleted = False

        for root, dirs, files in os.walk(root_dir):
            for folder in dirs:
                if folder.startswith("FlOOLDER_"):
                    folders_deleted = True
                    folder_path = os.path.join(root, folder)
                    os.rmdir(folder_path)
        if folders_deleted:
            print("[" + color.GREEN + ">" + color.RESET + "] - Die " + color.PINK + "Flooder" + color.RESET + " wurden erfolgreich gelöscht!")
        else:
            print("[" + color.RED + ">" + color.RESET + "] - Die " + color.PINK + "Flooder" + color.RESET + " wurden bereits gelöscht!")
    except:
        print("[" + color.RED + ">" + color.RESET + "] - Die " + color.PINK + "Flooder" + color.RESET + " konnten nicht gelöscht werden!") 

while True:
    cls()
    banner()

    try:
        print("[" + color.PINK + "1" + color.RESET + "] - Passwort Gen")
        print("[" + color.PINK + "2" + color.RESET + "] - KoZ           //" + color.PINK + "game" + color.RESET)
        print("[" + color.PINK + "3" + color.RESET + "] - Bruteforce")
        print("[" + color.PINK + "4" + color.RESET + "] - PC-Specs")
        print("[" + color.PINK + "5" + color.RESET + "] - Error         //" + color.PINK + "troll" + color.RESET)
        print("[" + color.PINK + "6" + color.RESET + "] - Flooder       //" + color.PINK + "troll" + color.RESET)
        print("[" + color.PINK + "7" + color.RESET + "] - QR-Code Gen")
        print("[" + color.PINK + "8" + color.RESET + "] - Guess Number  //" + color.PINK + "game" + color.RESET)
        print("[" + color.PINK + "9" + color.RESET + "] - Guess Word    //" + color.PINK + "game" + color.RESET)
        print()
        print("[" + color.RED + "X" + color.RESET + "] - Exit")
        print()

        choice = input("Auswahl: " + color.PINK)
        print(color.RESET)

        if choice == "1":
            cls()
            banner()
            passwort_gen()
            print()
            input(color.RESET + "Drücke Enter, um fortzufahren...")
        elif choice == "2" or choice.lower() == "koz":
            cls()
            banner()
            koz()
        elif choice == "3":
            cls()
            banner()
            bruteforce()
            print()
            input(color.RESET + "Drücke Enter, um fortzufahren...")
        elif choice == "4":
            cls()
            banner()
            pc_specs()
            print()
            input(color.RESET + "Drücke Enter, um fortzufahren...")
        elif choice == "5":
            cls()
            banner()
            error_troll()
            print()
            input(color.RESET + "Drücke Enter, um fortzufahren...")
        elif choice == "6":
            cls()
            banner()
            flooder()
            print()
            input(color.RESET + "Drücke Enter, um fortzufahren...")
        elif choice == "7":
            cls()
            banner()
            qr_gen()
            print()
            input(color.RESET + "Drücke Enter, um fortzufahren...")
        elif choice == "8":
            cls()
            banner()
            gnum()
        elif choice == "9":
            cls()
            banner()
            gtxt()
        elif choice.lower() == "reset all":
            cls()
            banner()
            reset_all()
            print()
            input(color.RESET + "Drücke Enter, um fortzufahren...")
        elif choice.lower() == "reset passes":
            cls()
            banner()
            reset_passes()
            print()
            input(color.RESET + "Drücke Enter, um fortzufahren...")
        elif choice.lower() == "reset stats":
            cls()
            banner()
            reset_stats()
            print()
            input(color.RESET + "Drücke Enter, um fortzufahren...")
        elif choice.lower() == "reset error":
            cls()
            banner()
            reset_error()
            print()
            input(color.RESET + "Drücke Enter, um fortzufahren...")
        elif choice.lower() == "reset flooder":
            cls()
            banner()
            reset_flooder()
            print()
            input(color.RESET + "Drücke Enter, um fortzufahren...")
        elif choice.lower() == "x":
            cls()
            banner()
            print(color.RESET + "[" + color.RED + ">" + color.RESET + "] - " + color.PINK + "GOTCHA" + color.RESET + " wird beendet!")
            print(color.RESET + "[" + color.RED + ">" + color.RESET + "] - •")
            time.sleep(1)
            cls()
            banner()
            print(color.RESET + "[" + color.RED + ">" + color.RESET + "] - " + color.PINK + "GOTCHA" + color.RESET + " wird beendet!")
            print(color.RESET + "[" + color.RED + ">" + color.RESET + "] - ••")
            time.sleep(1)
            cls()
            banner()
            print(color.RESET + "[" + color.RED + ">" + color.RESET + "] - " + color.PINK + "GOTCHA" + color.RESET + " wird beendet!")
            print(color.RESET + "[" + color.RED + ">" + color.RESET + "] - •••")
            time.sleep(1)
            cls()
            break

    except ValueError:
        cls()
        banner()
        print(color.RESET + "[" + color.RED + ">" + color.RESET + "] - Ungültige Eingabe. Probiere es nochmal!")
        print()
        input("Drücke Enter, um fortzufahren...")  

    except KeyboardInterrupt:
        cls()
        banner()
        print(color.RESET + "[" + color.RED + ">" + color.RESET + "] - " + color.PINK + "GOTCHA" + color.RESET + " wird beendet!")
        print(color.RESET + "[" + color.RED + ">" + color.RESET + "] - •")
        time.sleep(1)
        cls()
        banner()
        print(color.RESET + "[" + color.RED + ">" + color.RESET + "] - " + color.PINK + "GOTCHA" + color.RESET + " wird beendet!")
        print(color.RESET + "[" + color.RED + ">" + color.RESET + "] - ••")
        time.sleep(1)
        cls()
        banner()
        print(color.RESET + "[" + color.RED + ">" + color.RESET + "] - " + color.PINK + "GOTCHA" + color.RESET + " wird beendet!")
        print(color.RESET + "[" + color.RED + ">" + color.RESET + "] - •••")
        time.sleep(1)
        cls()
        break