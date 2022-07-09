


#Ejemplo de métodos PÚBLICOS/PRIVADOS:


class PublicPrivateExample:
    def __init__ (self):
        self.public = "safe"
        self._unsafe = "unsafe"

    def public_method(self):
        #EL CLIENTE PUEDE USARLO

    def _unsafe_method(self):
        #EL CLIENTE NO DEBERÍA USARLO (EMPIEZA CON UNDERSCORE)


