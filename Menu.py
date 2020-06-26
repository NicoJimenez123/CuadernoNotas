from Cuaderno import Cuaderno
import os


class Menu:

    def __init__(self):
        self.opciones = {1: 'anadir_nota', 2: 'ver_notas'}
        self.cuaderno = Cuaderno()
        while True:
            self.mostrar_menu()

    def mostrar_menu(self):
        print('Opcion 1) Añadir Notas')
        print('Opcion 2) Ver Notas')
        print('Opcion 3) Editar el Título de una Nota')
        print('Opcion 4) Editar el Contenido de una Nota')
        try:
            opcion = int(input('Ingrese una Opción: '))
        except ValueError:
            opcion = 0
        if opcion == 1:
            self.anadir_nota()
        if opcion == 2:
            self.ver_notas()
        if opcion == 3:
            self.editar_titulo()
        if opcion == 4:
            self.editar_contenido()
        os.system('pause')
        os.system('cls')

    def anadir_nota(self):
        titulo = input('Ingrese el Título: ')
        contenido = input('Ingrese el Contenido: ')
        self.cuaderno.anadir_nota(titulo, contenido)

    def ver_notas(self):
        for nota in self.cuaderno.notas:
            print(nota)

    def listar_notas(self):
        if len(self.cuaderno.notas) == 0:
            print("No hay Notas en el Cuaderno")
            return None
        while True:
            i = 0
            for nota in self.cuaderno.notas:
                print(i, ") "+nota.titulo)
                i += 1
            try:
                opcion = int(input("Ingrese una Opción: "))
            except ValueError:
                opcion = -1
            if 0 <= opcion <= len(self.cuaderno.notas):
                return self.cuaderno.notas[opcion]

    def obtener_nota(self):
        nota = self.listar_notas()
        return nota

    def editar_titulo(self):
        nota = self.obtener_nota()
        if nota:
            titulo = input('Ingrese el Nuevo Título: ')
            self.cuaderno.editar_titulo_nota(nota, titulo)

    def editar_contenido(self):
        nota = self.obtener_nota()
        if nota:
            titulo = input("Ingrese el Nuevo Contenido: ")
            self.cuaderno.editar_contenido_nota(nota, titulo)


if __name__ == '__main__':
    Menu()
