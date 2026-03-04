class Dictionary:
    def __init__(self):
        pass

    dati = {}
    with open('dictionary.txt', 'r') as file:
        for riga in file:
            chiave, valore = riga.strip().split(" ")
            # dizionario è fatto da parola-aliena, traduzione(in teoria ho creato una lista che contiene tutte le traduzioni)
            dati[chiave] = valore
    print(dati)

    def addWord(self, dizionario, aliena, traduzione):
        if aliena in dizionario:
            dizionario[aliena].append(traduzione)
        else:
            dizionario[aliena] = traduzione         # così in teoria sovrascrive se la chiave esiste già
                                                    # a me serve che la scriva di nuovo? O mi basta fare una lista di tutte le traduzioni come valore

    # dovrai anche scrivere sul file le parole che stai aggiungendo?
    def translate(self, dizionario, parola_aliena_da_tradurre):     # questi ti da la traduzione nel caso normale
        tradotta = dizionario[parola_aliena_da_tradurre]
        print("La traduzione di ", parola_aliena_da_tradurre, " è ", tradotta)

    def translateWordWildCard(self):
        pass

    def printDictionary(self, dizionario):
        print(dizionario)