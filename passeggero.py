class Passeggero :
    def __init__(self, codice_passeggero, nome, cognome):
        self._cod_passeggero= codice_passeggero
        self._nome = nome
        self._cognome = cognome

    @property
    def codice_passeggero(self):
        return self._cod_passeggero

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def cognome(self):
        return self._cognome

    @cognome.setter
    def cognome(self, cognome):
        self._cognome = cognome

    def __str__(self):
        return f"{self._nome} {self._cognome} ({self._cod_passeggero})"
