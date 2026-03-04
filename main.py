import translator as tr
import dictionary as d        # mi serve?

t = tr.Translator()
dizionario = d.Dictionary()    # mi serve?

while(True):

    t.printMenu()
    print("Scegli cosa vuoi fare: ")
    t.loadDictionary("filename.txt")

    txtIn = input()
    numeroIntero = int(txtIn)

    # Add input control here!
    while numeroIntero < 1 or numeroIntero > 5:
        print("Hai inserito un valore che non corrisponde a nessuna scelta!")
        print("Inserisci nuovamente la tua scelta: ")
        numeroIntero = int(input())

    if int(txtIn) == 1:
        print()
        print("Scrivi <parola aliena> <traduzione>: ")
        da_inserire = input().strip()
        campi = da_inserire.split()
        for campo in campi:
            campo.lower()
            while not campo.isalpha():     # attenzione che forse isalpha non va bene perchè conumque può contenere un punto interrogativo
                                           # può contenere UN SOLO punto interrogativo, puoi usare un contatore contando i '?', se è >1 segnala un problema
                print("Hai inserito caratteri nella parola aliena che non sono lettere!")
                print("Scrivi <parola aliena> <traduzione>: ")
                da_inserire = input().strip()
                campi = da_inserire.split()
                break
        if(len(campi) != 2):
            print("Hai inserito il formato sbagliato!")
            break
        dizionario.addWord(dizionario,campi[0], campi[1])     # da correggere

    if int(txtIn) == 2:
        print("Inserisci la parola aliena che vuoi tradurre: ")
        aliena = input().strip()
        while(aliena.lower().isalpha() == False):
            print("Hai inserito una parola non valida, inseriscine una che contenga solo lettere: ")
            aliena = input().strip()
        dizionario.translate(dizionario, aliena)

    if int(txtIn) == 3:
        pass

    if int(txtIn) == 4:
        dizionario.printDictionary()  # dovrai usare la funzione loadDictionary
        break

    if int(txtIn) == 5:
        print("Hai deciso di uscire!")
        break