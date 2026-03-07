class Dictionary:
    def __init__(self):

        self.dizionario = {}

    def addWord(self, aliena, traduzione):
        aliena = aliena.lower()
        traduzione = traduzione.lower()
        if aliena in self.dizionario:
            self.dizionario[aliena].append(traduzione)      # se la parola aliena è già presente nel dizionario aggiungo la traduzione alla lista delle traduzioni
        else:
            self.dizionario[aliena] = [traduzione]            # se la parola aliena non è presente nel dizionario creo una nuova chiave con rispettivo valore


    def translate(self, parola_aliena_da_tradurre):
        parola_aliena_da_tradurre = parola_aliena_da_tradurre.lower()
        if parola_aliena_da_tradurre in self.dizionario:                    # se parola aliena è presente nel dizionario stampo tutte le sue traduzioni
            print(f"Le traduzioni di {parola_aliena_da_tradurre} sono: ")
            for traduzione in self.dizionario[parola_aliena_da_tradurre]:
                print( " - ", traduzione )
        else:
            print("La parola che vuoi tradurre non ha traduzione!")         # parola aliena non presente nel dizionario
    def translateWordWildCard(self, query):
        query = query.lower()

        # controllo che ci sia al max un solo ?
        if query.count("?") > 1:
            print("Può esserci al massimo un solo ? all'interno della parola.")
            return

        posizione = query.find("?")  # trovo la posizione di ?
        trovate = False

        for parola in self.dizionario:
            # ignoro le parole che hanno lunghezza diversa da quella della query
            if len(parola) != len(query):
                continue
            # se la parte prima ? della parola è uguale a quella della query
            # e se la parte dopo ? della parola è uguale a quella della query
            # stampo e trovate = True
            if parola[:posizione] == query[:posizione] and parola[posizione+1:] == query[posizione+1:]:
                print(f"La parola aliena trovata è: {parola}")
                print(f"Le traduzioni di {parola} sono: ", ", ".join(self.dizionario[parola]))
                trovate = True
        if not trovate:
            print(f"Non è stata trovata nessuna parola compatibile!")       # parola aliena non trovata

    def printDictionary(self):
        for aliena, traduzioni in self.dizionario.items():
            print(f"Parola aliena: {aliena} , traduzioni: {traduzioni}")