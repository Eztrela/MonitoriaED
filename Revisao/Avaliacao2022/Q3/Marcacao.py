from filasequencialcircular import *
from Paciente import *


class Marcacao:
    
    
    def __init__(self, tempo_max_todos_atendimentos:int):
        self.fila = FilaSequencial()
        self.tempo_max = tempo_max_todos_atendimentos
        self.tempo_Acumulado=0


    def addPaciente(self, paciente:Paciente)->bool:
        '''Adiciona o paciente na fila de espera SE a fila de espera não tiver estourado o tempo limite das consultas
        '''
        if self.tempo_Acumulado < self.tempo_max:
            self.fila.enfileira(paciente)
            self.tempo_Acumulado += paciente.tempo_atendimento_minutos
            return True

        return False         

    def cancelarAgendamento(self, especialidade:str):
        
        if self.fila.estaVazia():
            raise Exception('A fila já está vazia')
                  
        for pacienteCheck in range(len(self.fila)):  # Percorre a fila de espera
            
            paciente= self.fila.desenfileira()
                 
            if paciente.especialidade == especialidade:  # Verifica se a especialidade do paciente é igual à especialidade informada
                self.tempo_Acumulado-=paciente.tempo_atendimento_minutos
            
            else:
                self.fila.enfileira(paciente) 
    
    
    def __str__(self) -> str:
        return str(self.fila)
        