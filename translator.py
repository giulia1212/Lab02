import dictionary as d
class Translator:

    def __init__(self):
        pass

    def printMenu(self):
        # 1. Aggiungi nuova parola
        # 2. Cerca una traduzione
        # 3. Cerca con wildcard
        # 4. Exit
        print("---------------------------------------------------")
        print("Translator Alien-Italian")
        print("---------------------------------------------------")
        print("1. Aggiungi una parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcard")
        print("4. Stampa tutto il dizionario")
        print("5. Exit")


    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        # dovrei caricare il dizionario dal file dictionary
        pass

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        campi = entry.strip().split()
        lunghezza = len(campi)
        for i in range(1, lunghezza):
            dizionario[campi[0]] = campi[i]     # devo mettere loadDisctionary in modo da poterlo vedere
        pass

    # dovrai prima svilppare il metodo qui sopra e il metodo addWord() in dictionary.py
    # poi in base alla lunghezza della stringa che l'utente ha inserito decidi se fare uno o l'altro,
    # però se l'utente riscrive una parola aliena già esistente devi solamente aggiungere la traduzione alla lista che si trova nel valore del dizionario
    # in realtà questo dovresti già averlo implemetato nella funzione addWord(), controlla però se lo hai fatto correttamente
    def handleTranslate(self, query):           # questo dovrebbe darti le varie traduzioni
        # query is a string <parola_aliena>
        pass

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>            # penso che puoi mettere qui il contatore di '?' e segnalare problemi se cnt>1
        pass