from Marcacao import *

m1=Marcacao(90)

p1=Paciente('Haniel Costa', 30,'joelho')
p2=Paciente('Pablo Estrela', 30,'tornozelo')
p3=Paciente('Gabriel Félix', 30,'joelho')


print(m1.addPaciente(p1))
print(m1.addPaciente(p2))
print(m1.addPaciente(p3))

print(m1)
m1.cancelarAgendamento('joelho')

print(m1)
