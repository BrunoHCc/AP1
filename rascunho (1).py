matrizMedicos = [[1245, 'João Pedro', 457812, 'M', 'Acrobata', 'Unip', 'joaop@google.com', 124578964], 
[8962, 'Juliana Pereira', 756348, 'F', 'Dermatologista', 'UFScar', 'julianap@google.com', 951423687]]

matrizPacientes = []

def listarTodos(opcaoSubmenu):

    if opcaoSubmenu == 1:
        
        for i in range(len(matrizMedicos)):
            for j in range(len(matrizMedicos[i])):
                print(matrizMedicos[i][j], end= " ")
            
            print('\n')
            main()

    elif opcaoSubmenu == 2:
        for i in range(len(matrizPacientes)):
            for j in range(len(matrizPacientes)):
                print(matrizPacientes[i][j], end= " ")


def listarElemento(opcaoSubmenu):

    if opcaoSubmenu == 1:

        print("Menus disponíveis",'\n')
        print("0. crm")
        print("1. nome")
        print("2. Data de nascimento")
        print("3. Sexo")
        print("4. Especialidade")
        print("5. Universidade")
        print("6. E-mail")
        print("7. Telefone")

        position = int(input("Qual gostaria de ver? "))


        for i in range(len(matrizMedicos)):
            print(matrizMedicos[i][position])
            print('\n')
        
        main()




def incluir(opcaoSubmenu):

    if opcaoSubmenu == 1:

        novo_med=[]
        novo_med.append(int(input('Digite o CRM: ')))
        for i in range(len(matrizMedicos)):
            if matrizMedicos[i][0] == novo_med[0]:
                print('Este usuário já está cadastrado')
                while matrizMedicos[i][0] == novo_med[0]:
                    novoCRM=(int(input('Digite um CRM válido: ')))
                    novo_med[0]= novoCRM
        novo_med.append(str(input('Digite o nome: ')))
        novo_med.append(input('Digite a data: '))
        novo_med.append(str(input('Digite o sexo: ')))
        novo_med.append(str(input('Digite a especialidade: ')))
        novo_med.append(str(input('Digite a universidade: ')))
        novo_med.append(input('Digite o email: '))

        matrizMedicos.append(novo_med)

        main()

def alterar(opcaoSubmenu):

    if opcaoSubmenu == 1:
        listarTodos(operacao)


def main():

    print('1. Médicos')
    print('2. Pacientes')
    print('5. Sair')

    opcaoSubmenu = int(input('Digite qual menu gostaria de acessar: '))

    if opcaoSubmenu == 1 or opcaoSubmenu == 2:
    
        print('1. Listar todos')
        print('2. Listar elemento específico')
        print('3. incluir')
        print('4. alterar')
        print('5. excluir')

        operacao = int(input('Digite qual menu gostaria de acessar: '))

    
    if operacao == 1:
        listarTodos(opcaoSubmenu)
    elif operacao == 2:
        listarElemento(opcaoSubmenu)
    elif operacao == 3:
        incluir(opcaoSubmenu)
    




main()