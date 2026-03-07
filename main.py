import translator as tr

t = tr.Translator()
t.loadDictionary("dictionary.txt")

while(True):

    t.printMenu()
    print("Scegli cosa vuoi fare: ")

    txtIn = input()

    # Add input control here!
    while not txtIn.isdigit() or int(txtIn) < 1 or int(txtIn) > 5 :
        print("Hai inserito un valore che non corrisponde a nessuna scelta!")
        print("Inserisci nuovamente la tua scelta: ")
        txtIn = input()

    if int(txtIn) == 1:
        print()
        print("Scrivi <parola aliena> <traduzione1 traduzione2 ...>: ")
        campi = input().strip()
        while len(campi.split()) < 2:
            campi = input("Hai inserito un formato sbagliato. Devi inserire almeno una parola aliena con la sua traduzione: ").strip()
        t.handleAdd(campi)
        print("Parola aggiunta correttamente!")

    if int(txtIn) == 2:
        print("Inserisci la parola aliena che vuoi tradurre: ")
        aliena = input().strip()
        while not aliena.replace("?", "").isalpha():
            print("Hai inserito una parola non valida, inseriscine una che contenga solo lettere: ")
            aliena = input().strip()
        t.handleTranslate(aliena)

    if int(txtIn) == 3:
        print("Inserisci una parola aliena che contenga '?': ")
        aliena = input().strip()
        while aliena.count("?") > 1 or not aliena.replace("?", "").isalpha():
            print("Puoi inserire al max un '?' e solo lettere. Riprova: ")
            aliena = input().strip()
        t.handleWildCard(aliena)

    if int(txtIn) == 4:
        print("Dizionario completo: ")
        t.dizionario.printDictionary()

    if int(txtIn) == 5:
        print("Hai deciso di uscire!")
        break