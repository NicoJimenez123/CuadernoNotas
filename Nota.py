from datetime import date


class Nota:

    def __init__(self, titulo: str, texto: str):
        self.titulo = titulo
        self.texto = texto
        self.fecha_creacion = date.today()
        self.ultima_modificacion = date.today()

    def __str__(self):
        attr = (self.titulo, self.texto, self.fecha_creacion.strftime('%A, %d %b %Y'),
                self.ultima_modificacion.strftime('%A, %d %b %Y'))
        tit = 'Titulo: '+attr[0]
        cont = 'Contenido: '+attr[1]
        creacion = 'Fecha de Creación: '+attr[2]
        ultmod = 'Ultima Modificación: '+attr[3]
        string = tit + '\n' + cont + '\n' + creacion +  '\n' + ultmod + '\n'
        return string

    def editar_titulo(self, titulo: str):
        self.titulo = titulo
        self.ultima_modificacion = date.today()

    def editar_contenido(self, contenido: str):
        self.texto = contenido
        self.ultima_modificacion = date.today()