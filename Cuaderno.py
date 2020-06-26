from Nota import Nota


class Cuaderno:

    def __init__(self):
        self.opciones = {1: self.anadir_nota}
        self.notas = []

    def anadir_nota(self, titulo: str, cont: str):
        nota = Nota(titulo, cont)
        self.notas.append(nota)

    def editar_titulo_nota(self, nota: Nota, titulo: str):
        if nota in self.notas:
            nota.editar_titulo(titulo)

    def editar_contenido_nota(self, nota: Nota, titulo: str):
        if nota in self.notas:
            nota.editar_contenido(titulo)
