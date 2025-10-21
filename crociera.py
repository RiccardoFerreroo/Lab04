from cabina import Cabina
from passeggero import Passeggero

class Crociera:
    def __init__(self, nome):
        self._nome = nome
        self._cabine =[]
        self._passeggeri=[]
        #@property agisce subito prima di stampare\leggere
        # un attributo mentre il @nome.setter è un check aggiuntivo
        # che non sostituice il metodo per assegnare una variabile
        # ma semplicemente la controlla , noi volendo poremmo evitare
        # questo controllandola prima di arricare alla assegnazione
        # della variabile all oggetto però questo ci può preclude dal
        # farlo prima facendolo dopo

    @property
    def cabine(self):
        return self._cabine

    @property
    def passeggeri(self):
        return self._passeggeri
    def __repr__(self):
        return f"{self._cabine} {self._passeggeri}, nome : {self._nome}"

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        with open(file_path, 'r', encoding = "utf-8") as f:
            for riga in f:
                riga = riga.strip()
                if not riga:
                    continue

                elementi = [e.strip() for e in riga.split(",")]

                if elementi[0].startswith("P"):
                    try:
                        passeggero = Passeggero(elementi[0], elementi[1], elementi[2])
                        self._passeggeri.append(passeggero)
                    except Exception as e:
                        print(e)

                elif elementi[0].startswith("CAB"):
                    try:

                        num_letti = int(elementi[1])
                        ponte = int(elementi[2])
                        prezzo = float(elementi[3])

                        c = Cabina(elementi[0], num_letti, ponte, prezzo)
                        self._cabine.append(c)
                    except Exception as e:
                        print(e)
                else:
                    continue



    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        #trova cabina
        cabina = None
        for c in self._cabine:
            if c.codice_cabina == codice_cabina:
                cabina = c
                break
        if cabina is None:
            raise ValueError(f"Cabina {codice_cabina} non trovata.")

        #trova passeggero
        passeggero = None
        for p in self._passeggeri:
            if p.codice_passeggero == codice_passeggero:
                passeggero = p
                break
        if passeggero is None:
            raise ValueError(f"Passeggero {codice_passeggero} non trovato.")

        # Controlla se cabina è libera
        if cabina.passeggero is not None:
            raise ValueError(f"Cabina {codice_cabina} già occupata da {cabina.passeggero.nome}.")

        # Assegna
        cabina.passeggero = passeggero

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""

        return sorted(self._cabine, key=lambda c: c.prezzo_base)

    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        for p in self._passeggeri:
            cabina_info = "Non assegnata"
            for c in self._cabine:
                if c.passeggero == p:
                    cabina_info = c.codice_cabina
                    break
            print(f"{p.nome} {p.cognome} ({p.codice_passeggero}) - Cabina: {cabina_info}")
        # TODOo

