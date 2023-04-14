class Paciente:
    def __init__(self, nome:str, tempo_atendimento_minutos:int, especialidade:str):
        self.__nome = nome
        self.tempo_atendimento_minutos = tempo_atendimento_minutos
        self.especialidade = especialidade # joelho / quadril / ombro / tornozelo
        
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self,nome):
        self.__nome=nome
        
    
    def __str__(self) -> str:
        return f'{self.__nome}, {self.especialidade}, {self.tempo_atendimento_minutos}'