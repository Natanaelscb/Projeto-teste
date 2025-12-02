from moto import Moto

class MotosCB:
    def __init__(self):
        self.motos = [
            Moto("CB 300R", "Honda", "Naked", 2024, "Vermelha", "001"),
            Moto("MT-03", "Yamaha", "Naked", 2023, "Preta", "002"),
            Moto("Z400", "Kawasaki", "Naked", 2024, "Verde", "003"),
            Moto("G 310 R", "BMW", "Naked", 2023, "Branca", "004"),
            Moto("Duke 390", "KTM", "Naked", 2024, "Laranja", "005"),
            Moto("Monster 821", "Ducati", "Sport", 2022, "Vermelha", "006"),
            Moto("Street Triple", "Triumph", "Naked", 2023, "Cinza", "007"),
            Moto("Ninja 400", "Kawasaki", "Sport", 2024, "Verde", "008"),
            Moto("YZF-R3", "Yamaha", "Sport", 2023, "Azul", "009"),
            Moto("CBR 500R", "Honda", "Sport", 2023, "Vermelha", "010"),
            Moto("Versys 650", "Kawasaki", "Touring", 2024, "Preta", "011"),
            Moto("V-Strom 650", "Suzuki", "Touring", 2023, "Amarela", "012"),
            Moto("Tracer 900", "Yamaha", "Touring", 2022, "Azul", "013"),
            Moto("Tiger 900", "Triumph", "Adventure", 2024, "Cinza", "014"),
            Moto("Africa Twin", "Honda", "Adventure", 2023, "Branca", "015"),
            Moto("GSX-S750", "Suzuki", "Naked", 2022, "Azul", "016"),
            Moto("XSR 700", "Yamaha", "Retro", 2024, "Cinza", "017"),
            ]
        

    def adicionarMoto(self):
        nome = input("Qual o nome da Motocicleta?: ")
        marca = input("Qual a marca?: ")
        modelo = input("Qual o modelo?: ")
        ano = int(input("Qual ano?: "))
        cor = input("Qual a cor?: ")
        registro = input("Qual o Registro?: ")

        moto = Moto(nome, marca, modelo, ano,cor,registro)
        self.motos.append(moto)
        print(f"A motocicleta {moto.nome} foi cadastrada")

    def deleteMoto(self):
        if not self.motos:
            print("Nenhuma moto cadastrada")
            return

        registro = input("Digite o registro da moto que deseja deletar: ")
        for moto in self.motos:
            if moto.registro == registro:
                self.motos.remove(moto)
                print(f"A motocicleta {moto.nome} foi removida")
                break
        else:
            print("Registro não encontrado")
    
    def atualizarMoto(self):
        if not self.motos:
            print("Nenhuma moto encontrada")
            return
        registro = input("Digite o registro da moto que deseja deletar: ")
        for moto in self.motos:
            if moto.registro == registro:
                novacor = input("Digite a nova cor!: ")
                moto.cor = novacor
                print(f"A cor do veiculo {moto.cor} foi alterada com sucesso")
                return f"Registro invalido"
    def todasasMotos(self):
        if not self.motos:
            print("Nenhuma moto encontrada")
            return
        print("\n# ---Motos ---#")
        for moto in self.motos:
            print(f"Nome: {moto.nome} | Marca: {moto.marca} | Modelo: {moto.modelo} | Ano: {moto.ano} | Cor: {moto.cor} | Registro: {moto.registro}")
        
    def listarNome(self):
        if not self.motos:
            print("Nenhuma moto encontrada")
            return
        print("\n# ---Motos ---#")
        name2 = input("Digite a marca da moto: ").strip().lower()

        encontrou = False
        for moto in self.motos:
            if moto.nome.strip().lower() == name2:
                print(f"Nome: {moto.nome} | Marca: {moto.marca} | Modelo: {moto.modelo} | Ano: {moto.ano} | Cor: {moto.cor} | Registro: {moto.registro}")
                print("------------------------------")
                encontrou = True

        if not encontrou:
            print("Nenhuma moto encontrada com esse nome.")
    def listarMarca(self):
        if not self.motos:
            print("Nenhuma moto encontrada")
            return
        print("\n# ---Motos ---#")
        name2 = input("Digite o nome da moto: ").strip().lower()

        encontrou = False
        for moto in self.motos:
            if moto.marca.strip().lower() == name2:
                print(f"Nome: {moto.nome} | Marca: {moto.marca} | Modelo: {moto.modelo} | Ano: {moto.ano} | Cor: {moto.cor} | Registro: {moto.registro}")
                print("------------------------------")
                encontrou = True

        if not encontrou:
            print("Nenhuma moto encontrada com esse modelo.")
    def listarModelo(self):
        if not self.motos:
            print("Nenhuma moto encontrada")
            return
        print("\n# ---Motos ---#")
        name2 = input("Digite o nome do modelo: ").strip().lower()

        encontrou = False
        for moto in self.motos:
            if moto.modelo.strip().lower() == name2:
                print(f"Nome: {moto.nome} | Marca: {moto.marca} | Modelo: {moto.modelo} | Ano: {moto.ano} | Cor: {moto.cor} | Registro: {moto.registro}")
                print("------------------------------")
                encontrou = True

        if not encontrou:
            print("Nenhuma moto encontrada com esse ano.")
    def listarAno(self):
        if not self.motos:
            print("Nenhuma moto encontrada")
            return
        print("\n# ---Motos ---#")
        name2 = int(input("Digite o ano da moto: "))

        encontrou = False
        for moto in self.motos:
            if moto.ano == name2:
                print(f"Nome: {moto.nome} | Marca: {moto.marca} | Modelo: {moto.modelo} | Ano: {moto.ano} | Cor: {moto.cor} | Registro: {moto.registro}")
                print("------------------------------")
                encontrou = True

        if not encontrou:
            print("Nenhuma moto encontrada com esse ano.")


        
    def listarMotos(self):
        while(True):
            print(''' Qual a sua pesquisa?
                  1 Nome
                  2 Marca
                  3 Modelo
                  4 Ano 
                  5 Ver todas as motos
                  6 Menu''')

            opcao = int(input(" "))
            match opcao:
                case 1:
                    self.listarNome()
                case 2:
                    self.listarMarca()
                case 3:
                    self.listarModelo()
                case 4:
                    self.listarAno()
                case 5:
                    self.todasasMotos()
                case 6:
                    print("Vc está voltando para o menu!")
                    self.menu()
                case _:
                    break
    def  menu(self):
        while(True):
            print('''                  1 Adicionar moto
                  2 Deletar moto
                  3 Atualizar dados
                  4 Listar modelo ''')
            opcao = int(input("="))
            match opcao:
                case 1:
                    self.adicionarMoto()
                case 2:
                    self.deleteMoto()
                case 3:
                    self.atualizarMoto()
                case 4: 
                    self.listarMotos()
                case _:
                    break

if __name__ =="__main__":
    bancodados = MotosCB()
    bancodados.menu()