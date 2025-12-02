from classs import Aluno
class AlunoDB:
        def __init__(self):
            self.alunos=[]
    
        def adicionarAL(self):
            nome = input("Qual seu nome? ")
            matricula = input("Qual a sua matricula? ")
            nota = float(input("Qual a sua nota? "))
        
            aluno = Aluno(nome,matricula,nota)
        
            self.alunos.append(aluno)
            print(f"O Aluno {aluno.nome} foi cadastrado!")
            
        def deleteAL(self):
            if not self.alunos:
                print("Nenhum aluno cadastrado")
                return
            matricula= input("Digite a Matricula do elemento para deletar ")
            for aluno in self.alunos:
                if aluno.matricula == matricula:
                    self.alunos.remove(aluno)
                    print(f" Aluno {aluno.nome} foi deletado")
                    return
                else:
                    print(f"Aluno não existe")
        def atualizarAL(self):
            if not self.alunos:
                print("Nenhum aluno cadastrado")
                return
            matricula= input("Digite a Matricula do elemento para deletar ")
            for aluno in self.alunos:
                if aluno.matricula == matricula:
                    novanota = float(input("Digite a nova nota: "))
                    aluno.nota = novanota
                    print(f" Aluno {aluno.nome} teve sua nova  nota")
                    return
                else:
                    print(f"Aluno não existe")
                
        def menu(self):
            while(True):
                print('''                      1 ADD
                      2 Lista
                      3 Delet
                      4 Atualizar  ''')
                opcao= int(input())
                match opcao:
                    case 1:
                        self.adicionarAL()
                    case 2:
                        self.listarAL()
                    case 3:
                        self.deleteAL()
                    case 4:
                        self.atualizarAL()
                    case _:
                        break
if __name__ =="__main__":
    bancodados = AlunoDB()
    bancodados.menu()