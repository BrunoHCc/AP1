

def listarTodosMed(matrizMedicos,matrizPacientes):
    
    for i in range(len(matrizMedicos)):
        for j in range(len(matrizMedicos[i])):
            print(matrizMedicos[i][j], end= " ")
        
        print('\n')
    menu_principal(matrizMedicos,matrizPacientes)
       
def listarTodosPac(matrizMedicos,matrizPacientes):

    for i in range(len(matrizPacientes)):
        for j in range(len(matrizPacientes[i])):
            print(matrizPacientes[i][j], end= " ")
        
        print('\n')
    menu_principal(matrizMedicos,matrizPacientes)


def listarElementoMed(matrizMedicos,matrizPacientes):
        
    print("Menus disponíveis",'\n')
    print("0. CRM")
    print("1. Nome")
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
    
    menu_principal(matrizMedicos,matrizPacientes)

def listarElementoPac(matrizMedicos,matrizPacientes):

    print("Menus disponíveis",'\n')
    print("0. CPF")
    print("1. Nome")
    print("2. Data de nascimento")
    print("3. Sexo")
    print("4. Plano de saúde")
    print("5. E-mail")
    print("6. Telefone")

    position = int(input("Qual gostaria de ver? "))


    for i in range(len(matrizPacientes)):
        print(matrizPacientes[i][position])
        print('\n')
    
    menu_principal(matrizMedicos,matrizPacientes)

def incluirMed(matrizMedicos,matrizPacientes):

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
    var1=True
    while var1:    
        email=input("adicionar novo email? (S/N)")
        if email== 'N' or email=='n':
            var1=False
        elif email== 'S' or email=='s':    
            novo_med.append(input('Digite o email: '))
        else:
            print('digite novamente (S/N) ')
    novo_med.append(int(input('Digite o telefone: ')))
    var2=True
    while var2:    
        tele=input("adicionar novo email? (S/N)")
        if tele== 'N' or tele=='n':
            var2=False
        elif email== 'S' or email=='s':    
            novo_med.append(input('Digite o telefone: '))
        else:
            print('digite novamente (S/N) ')

    matrizMedicos.append(novo_med)

    menu_principal(matrizMedicos,matrizPacientes)


def incluirPac(matrizMedicos,matrizPacientes):
    novo_pac=[]
    novo_pac.append(int(input('Digite o CPF: ')))
    for i in range(len(matrizPacientes)):
        if matrizPacientes[i][0] == novo_pac[0]:
            print('Este usuário já está cadastrado')
            while matrizPacientes[i][0] == novo_pac[0]:
                novoCPF=(int(input('Digite um CPF válido: ')))
                novo_pac[0]= novoCPF
    novo_pac.append(str(input('Digite o nome: ')))
    novo_pac.append(input('Digite a data: '))
    novo_pac.append(str(input('Digite o sexo: ')))
    novo_pac.append(str(input('Digite plano de saúde: ')))
    novo_pac.append(input('Digite o email: '))
    var1=True
    while var1:    
        email=input("adicionar novo email? (S/N)")
        if email== 'N' or email=='n':
            var1=False
        elif email== 'S' or email=='s':    
            novo_pac.append(input('Digite o email: '))
        else:
            print('digite novamente (S/N) ')
    novo_pac.append(int(input('Digite o telefone: ')))
    var2=True
    while var2:    
        tele=input("adicionar novo email? (S/N)")
        if tele== 'N' or tele=='n':
            var2=False
        elif email== 'S' or email=='s':    
            novo_pac.append(input('Digite o telefone: '))
        else:
            print('digite novamente (S/N) ')

    matrizPacientes.append(novo_pac)

    menu_principal(matrizMedicos,matrizPacientes)

def alterarMed(matrizMedicos,matrizPacientes):


    for i in range(len(matrizMedicos)):
        for j in range(len(matrizMedicos[i])):
            print(matrizMedicos[i][j], end= " ")
        print('\n')

    usuario=int(input("Qual usuário gostaria de alterar? \n"))

    for usuario in range(len(matrizMedicos[usuario])):
        
        print("0. CRM")
        print("1. Nome")
        print("2. Data de nascimento")
        print("3. Sexo")
        print("4. Especialidade")
        print("5. Universidade")
        print("6. E-mail")
        print("7. Telefone")
        dado=int(input('Qual informação gostaria de alterar? '))
        for dado in matrizMedicos[usuario]:
            matrizMedicos[dado]=input('digite o novo dado: ')



def submenu_medicos(matrizMedicos):
    print('1. Listar todos')
    print('2. Listar elemento específico')
    print('3. incluir')
    print('4. alterar')
    print('5. excluir')

    operacao = int(input('Digite qual menu gostaria de acessar: '))

    if operacao == 1:
        listarTodosMed(matrizMedicos)
        
    elif operacao == 2:
        listarElementoMed(matrizMedicos)
        
    elif operacao == 3:
        incluirMed(matrizMedicos)
    
    elif operacao == 4:
        alterarMed(matrizMedicos)

    

def submenu_pacientes(matrizPacientes):
    print('1. Listar todos')
    print('2. Listar elemento específico')
    print('3. incluir')
    print('4. alterar')
    print('5. excluir')

    operacao = int(input('Digite qual menu gostaria de acessar: '))

    if operacao == 1:
        listarTodosPac(matrizPacientes)
    elif operacao == 2:
        listarElementoPac(matrizPacientes)
    elif operacao == 3:
        incluirPac(matrizPacientes)


def menu_principal(matrizMedicos, matrizPacientes):
    print('1. Médicos')
    print('2. Pacientes')
    print('5. Sair')

    opcaoSubmenu = int(input('Digite qual menu gostaria de acessar: '))

    if opcaoSubmenu == 1:
        submenu_medicos(matrizMedicos)

    elif opcaoSubmenu == 2:
        submenu_pacientes(matrizPacientes)


def main():
    matrizMedicos = [[1245, 'João Pedro', 123456, 'M', 'Acrobata', 'Unip', 'joaop@google.com', 124578964], [8962, 'Juliana Pereira', 456789, 'F', 'Dermatologista', 'UFScar', 'julianap@google.com', 951423687]]
    matrizPacientes = [[12345678920, 'Pedro Coelho', 123456, 'M', 'Plano Especial 1', 'pedro.coelho@google.com', 124578451]]
    menu_principal(matrizMedicos, matrizPacientes)


main()