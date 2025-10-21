from passeggero import Passeggero


class Cabina:

    def __init__(self, codice, num_letti, ponte, prezzo_base, tipo):
        self._codice_cabina =codice
        self._num_letti = int(num_letti)
        self._ponte = int(ponte)
        self._prezzo_base = float(prezzo_base)
        self._passeggero = None
        self._tipo = None #proprietà privata
        self.tipo = tipo  #usa il setter per inizializzare

    @property
    def codice_cabina(self):
            return self._codice_cabina
    @property
    def tipo(self):
        return self._tipo
    @tipo.setter
    def tipo(self, tipo):
        if tipo == "Standard":
            self._tipo = tipo
        elif tipo in("Moderna", "Classica", "Lussuosa"):
            self._tipo = tipo
            self._prezzo_base = self._prezzo_base *1.20
        else:
            try:
                max_animali = int(tipo)
                self._tipo = "Animale"
                self._prezzo_base = self._prezzo_base *(1+0.1*max_animali)
            except ValueError:
                self._tipo = "Standard"

    @property
    def num_letti(self):
        return self._num_letti
    @property
    def ponte(self):
        return self._ponte
    @property
    def prezzo_base(self):
        return self._prezzo_base
    @property
    def passeggero(self):
        return self._passeggero
    @passeggero.setter
    def passeggero(self, passeggero):
        if passeggero is None:
            self._passeggero = None
            return
        if passeggero.cabina is not None:
            raise Exception(f"il passeggero {passeggero.nome} è già"
                            f" assegnato alla cabina {passeggero.cabina.codice_cabina}")
        self._passeggero = passeggero
        passeggero.cabina = self

    def __str__(self):

        return(f"Cabina {self._codice_cabina} ({self._num_letti} letti, "
              f"ponte {self._ponte}) - Prezzo: {self._prezzo_base} € - Tipo: {self._tipo}")

    def __repr__(self):
            return str(self)


