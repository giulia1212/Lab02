import dictionary as d
class Translator:

    def __init__(self):
        self.dizionario = d.Dictionary()

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
        try:
            with open(dict, "r") as file:
                for riga in file:
                    campi = riga.strip().split()
                    if len(campi) >= 2:
                        aliena = campi[0]
                    for traduzione in campi[1:]:
                        self.dizionario.addWord(aliena, traduzione)
        except FileNotFoundError:
            print("File non trovato!")


    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        campi = entry.strip().split()
        lunghezza = len(campi)
        aliena = campi[0]
        for i in range(1, lunghezza):
            self.dizionario.addWord(aliena, campi[i])


    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        self.dizionario.translate(query)


    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        self.dizionario.translateWordWildCard(query)