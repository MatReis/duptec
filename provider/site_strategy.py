
class Site:
    def __init__(self, filtro, documento) -> None:
        self.filtro = filtro
        self.documento = documento

    def consultar(self, site):
        self.dados = site.realiza_consulta(self.filtro, self.documento)
    
    def dados(self):
        return self.dados