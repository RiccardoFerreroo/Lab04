class Cabina:
    def __init__(self, codice, num_letti, ponte, prezzo_base):
        self._codice_cabina =codice
        self._num_letti = int(num_letti)
        self._ponte = int(ponte)
        self._prezzo_base = float(prezzo_base)
        self._passeggero = None

    @property
    def codice_cabina(self):
            return self._codice_cabina

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
        self._passeggero = passeggero

    def __str__(self):
        return (f"Cabina {self._codice_cabina} ({self._num_letti} letti,"
                f" ponte {self._ponte}) - Prezzo: {self._prezzo_base}")




