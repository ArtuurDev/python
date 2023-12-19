class Estudante:
    nome = "paulo"
    matricula = 353637




class EstudanteGraduacao(Estudante):
    curso = "ads"



class EstudantePos(Estudante):
    nivel = 1
    orientador = "roberto"



aluno = EstudanteGraduacao()


print(f' olá {aluno.nome} seu curso de graduaçao é {aluno.curso} e sua matricula de acesso é {aluno.matricula}')


aluno2 = EstudantePos()
print(f'olá {aluno2.nome}, seu nivel é {aluno2.nivel} e seu orientador será o {aluno2.orientador}')

