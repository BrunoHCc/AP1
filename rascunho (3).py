
def listarTodosMed(matrizMedicos,matrizPacientes):
    continuar=True
    while continuar:
        for i in range(len(matrizMedicos)):
            for j in range(len(matrizMedicos[i])):
                print([matrizMedicos[i][j]], end= " ")
            
            print('\n')
        retorno=input('Retornar ao menu anterior? (S/N) \n')
        if retorno == 'S' or retorno == 's':
            continuar=False
            submenu_medicos(matrizMedicos,matrizPacientes)
        else:
            continuar
            print('\n Listar usuários \n')
       
def listarTodosPac(matrizMedicos,matrizPacientes):
    continuar=True
    while continuar:
        for i in range(len(matrizPacientes)):
            for j in range(len(matrizPacientes[i])):
                print([matrizPacientes[i][j]], end= " ")
            
            print('\n')
        retorno=input('Retornar ao menu anterior? (S/N) \n')
        if retorno == 'S' or retorno == 's':
            continuar=False
            submenu_pacientes(matrizMedicos,matrizPacientes)
        else:
            continuar
            print('\n Listar usuários \n')


def listarElementoMed(matrizMedicos,matrizPacientes):
    continuar=True
    while continuar:    
        print("Menus disponíveis",'\n')
        print("0. CRM")
        print("1. Nome")
        print("2. Data de nascimento")
        print("3. Sexo")
        print("4. Especialidade")
        print("5. Universidade")
        print("6. E-mail")
        print("7. Telefone")

        position = int(input("Qual gostaria de ver? \n"))

        for i in range(len(matrizMedicos)):
            print(matrizMedicos[i][position])
            print('\n')
        
        retorno=input('Retornar ao menu anterior? (S/N) \n')
        if retorno == 'S' or retorno == 's':
            continuar=False
            submenu_medicos(matrizMedicos,matrizPacientes)
        else:
            continuar
            print('\n Listar novo elemento \n')

def listarElementoPac(matrizMedicos,matrizPacientes):
    continuar=True
    while continuar:
        print("Menus disponíveis",'\n')
        print("0. CPF")
        print("1. Nome")
        print("2. Data de nascimento")
        print("3. Sexo")
        print("4. Plano de saúde")
        print("5. E-mail")
        print("6. Telefone")

        position = int(input("Qual gostaria de ver? \n"))

        for i in range(len(matrizPacientes)):
            print(matrizPacientes[i][position])
            print('\n')
        
        retorno=input('Retornar ao menu anterior? (S/N) ')
        if retorno == 'S' or retorno == 's':
            continuar=False
            submenu_pacientes(matrizMedicos,matrizPacientes)
        else:
            continuar
            print('\n Listar novo elemento \n')

def incluirMed(matrizMedicos,matrizPacientes):
    continuar=True
    while continuar:
        novo_med=[]
        novo_med.append(int(input('Digite o CRM: ')))
        for i in range(len(matrizMedicos)):
            if matrizMedicos[i][0] == novo_med[0]:
                print('Este usuário já está cadastrado')
                while matrizMedicos[i][0] == novo_med[0]:
                    novoCRM=(int(input('Digite um CRM válido: ')))
                    novo_med[0]= novoCRM
        nomeletra=True
        while nomeletra:
            nomepac=(input('Digite o nome: '))
            sem_espaco=nomepac.replace(" ","")
            if sem_espaco.isalpha() is True:
                novo_med.append(nomepac)
                nomeletra=False
            else:
                print('Digite caracteres válidos ')
        novo_med.append(input('Digite a data de nascimento: '))
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
                novo_med.append(str(input('Digite outro email: ')))
            else:
                print('digite novamente (S/N) ')
        novo_med.append(int(input('Digite outro telefone: ')))
        var2=True
        while var2:    
            tele=input("adicionar novo telefone? (S/N)")
            if tele== 'N' or tele=='n':
                var2=False
            elif email== 'S' or email=='s':    
                novo_med.append(int(input('Digite outro telefone: ')))
            else:
                print('digite novamente (S/N) ')

        matrizMedicos.append(novo_med)

        retorno=input('Retornar ao menu anterior? (S/N) ')
        if retorno == 'S' or retorno == 's':
            continuar=False
            submenu_medicos(matrizMedicos,matrizPacientes)
        else:
            continuar
            print('\n Incluir novo usuário \n')


def incluirPac(matrizMedicos,matrizPacientes):
    continuar=True
    while continuar:    
        novo_pac=[]
        novo_pac.append(int(input('Digite o CPF: ')))
        for i in range(len(matrizPacientes)):
            if matrizPacientes[i][0] == novo_pac[0]:
                print('Este usuário já está cadastrado')
                while matrizPacientes[i][0] == novo_pac[0]:
                    novoCPF=(int(input('Digite um CPF válido: ')))
                    novo_pac[0]= novoCPF
        nomeletra=True
        while nomeletra:
            nomepac=(input('Digite o nome: '))
            sem_espaco=nomepac.replace(" ","")
            if sem_espaco.isalpha() is True:
                novo_pac.append(nomepac)
                nomeletra=False
            else:
                print('Digite caracteres válidos ')
        novo_pac.append(str(input('Digite a data de nascimento: ')))
        novo_pac.append(str(input('Digite o sexo: ')))
        novo_pac.append(str(input('Digite plano de saúde: ')))
        novo_pac.append(str(input('Digite o email: ')))
        var1=True
        while var1:    
            email=input("adicionar novo email? (S/N)")
            if email== 'N' or email=='n':
                var1=False
            elif email== 'S' or email=='s':    
                novo_pac.append(str(input('Digite outro email: ')))
            else:
                print('digite novamente (S/N) ')
        novo_pac.append(int(input('Digite outro telefone: ')))
        var2=True
        while var2:    
            tele=input("adicionar novo telefone? (S/N)")
            if tele== 'N' or tele=='n':
                var2=False
            elif email== 'S' or email=='s':    
                novo_pac.append(int(input('Digite outro telefone: ')))
            else:
                print('digite novamente (S/N) ')

        matrizPacientes.append(novo_pac)

        retorno=input('Retornar ao menu anterior? (S/N) ')
        if retorno == 'S' or retorno == 's':
            continuar=False
            submenu_pacientes(matrizMedicos,matrizPacientes)
        else:
            continuar
            print('\n Incluir novo usuário \n')

def alterarMed(matrizMedicos,matrizPacientes):
    continuar=True
    while continuar:
        for i in range(len(matrizMedicos)):
            for j in range(len(matrizMedicos[i])):
                print(matrizMedicos[i][j], end= " ")
            print('\n')

        print("1. Alterar todos os dados de um usuário")
        print("2. Alterar um dado específico de um usuário")
        escolha=int(input())
        usuario=int(input("Qual usuário gostaria de alterar? \n"))

        if escolha==1:#alterar completamente um usuário

            for i in range(len(matrizMedicos[usuario])):
                atualizacao=input('digite o novo dado: ')
                matrizMedicos[usuario][i]=atualizacao

        elif escolha==2:#alterar info especifica
            print("0. CRM")
            print("1. Nome")
            print("2. Data de nascimento")
            print("3. Sexo")
            print("4. Especialidade")
            print("5. Universidade")
            print("6. E-mail")
            print("7. Telefone")
            dado=int(input('Qual informação gostaria de alterar? '))
            atualizacao=input('digite o novo dado: ')
            for i in range(len(matrizMedicos[usuario])):
                matrizMedicos[usuario][dado]=atualizacao

        print("Alteração realizada com sucesso \n")
        retorno=input('Retornar ao menu anterior? (S/N) ')
        if retorno == 'S' or retorno == 's':
            continuar=False
            submenu_medicos(matrizMedicos,matrizPacientes)
        else:
            continuar
            print('\n Alterar novo usuário \n')

def alterarPac(matrizMedicos,matrizPacientes):
    continuar=True
    while continuar:
        for i in range(len(matrizPacientes)):
            for j in range(len(matrizPacientes[i])):
                print(matrizPacientes[i][j], end= " ")
            print('\n')

        print("1. Alterar todos os dados de um usuário")
        print("2. Alterar um dado específico de um usuário")
        escolha=int(input())
        usuario=int(input("Qual usuário gostaria de alterar? \n"))

        if escolha==1:#alterar completamente um usuário

            for i in range(len(matrizPacientes[usuario])):
                atualizacao=input('digite o novo dado: ')
                matrizPacientes[usuario][i]=atualizacao

        elif escolha==2:#alterar info especifica
            print("0. CPF")
            print("1. Nome")
            print("2. Data de nascimento")
            print("3. Sexo")
            print("4. Plano de saúde")
            print("5. E-mail")
            print("6. Telefone")
            dado=int(input('Qual informação gostaria de alterar? '))
            atualizacao=input('digite o novo dado: ')
            for i in range(len(matrizPacientes[usuario])):
                matrizPacientes[usuario][dado]=atualizacao

        print("Alteração realizada com sucesso \n")
        retorno=input('Retornar ao menu anterior? (S/N) ')
        if retorno == 'S' or retorno == 's':
            continuar=False
            submenu_pacientes(matrizMedicos,matrizPacientes)
        else:
            continuar
            print('\n Alterar novo usuário \n')
    

def excluirMed(matrizMedicos,matrizPacientes):
    continuar=True
    while continuar:

        print('\n Excluir um usuário')
        for i in range(len(matrizMedicos)):
            for j in range(len(matrizMedicos[i])):
                print([matrizMedicos[i][j]], end= " ")
            print('\n')
        usuario=int(input('Qual usuário gostaria de excluir? '))
        del matrizMedicos[usuario]
        print('\n Dados excluídos com sucesso. \n')
        retorno=input('Retornar ao menu anterior? (S/N) ')
        if retorno == 'S' or retorno == 's':
            continuar=False
            submenu_medicos(matrizMedicos,matrizPacientes)
        else:
            continuar

def excluirPac(matrizMedicos,matrizPacientes):
    continuar=True
    while continuar:

        print('\n Excluir um usuário')
        for i in range(len(matrizPacientes)):
            for j in range(len(matrizPacientes[i])):
                print([matrizPacientes[i][j]], end= " ")
            print('\n')
        usuario=int(input('Qual usuário gostaria de excluir? '))
        del matrizPacientes[usuario]
        print('\n Dados excluídos com sucesso. \n')
        retorno=input('Retornar ao menu anterior? (S/N) ')
        if retorno == 'S' or retorno == 's':
            continuar=False
            submenu_pacientes(matrizMedicos,matrizPacientes)
        else:
            continuar


def submenu_medicos(matrizMedicos,matrizPacientes):
    print('\n')
    print('1. Listar todos')
    print('2. Listar elemento específico')
    print('3. incluir')
    print('4. alterar')
    print('5. excluir')
    print('6. Voltar ao Menu principal')
    
    operacao = int(input('Digite qual menu gostaria de acessar: \n'))

    if operacao == 1:
        listarTodosMed(matrizMedicos,matrizPacientes)
    elif operacao == 2:
        listarElementoMed(matrizMedicos,matrizPacientes)
    elif operacao == 3:
        incluirMed(matrizMedicos,matrizPacientes)
    elif operacao == 4:
        alterarMed(matrizMedicos,matrizPacientes)
    elif operacao == 5:
        excluirMed(matrizMedicos,matrizPacientes)
    elif operacao == 6:
        menu_principal(matrizMedicos,matrizPacientes)
    

def submenu_pacientes(matrizMedicos,matrizPacientes):
    print('\n')
    print('1. Listar todos')
    print('2. Listar elemento específico')
    print('3. incluir')
    print('4. alterar')
    print('5. excluir')
    print('6. Voltar ao Menu principal')

    operacao = int(input('Digite qual menu gostaria de acessar: \n'))

    if operacao == 1:
        listarTodosPac(matrizMedicos,matrizPacientes)
    elif operacao == 2:
        listarElementoPac(matrizMedicos,matrizPacientes)
    elif operacao == 3:
        incluirPac(matrizMedicos,matrizPacientes)
    elif operacao == 4:
        alterarPac(matrizMedicos,matrizPacientes)
    elif operacao == 5:
        excluirPac(matrizMedicos,matrizPacientes)
    elif operacao == 6:
        menu_principal(matrizMedicos,matrizPacientes)


def menu_principal(matrizMedicos, matrizPacientes):
    print('1. Médicos')
    print('2. Pacientes')
    print('5. Sair')

    opcaoSubmenu = int(input('Digite qual menu gostaria de acessar: \n'))

    if opcaoSubmenu == 1:
        submenu_medicos(matrizMedicos,matrizPacientes)

    elif opcaoSubmenu == 2:
        submenu_pacientes(matrizMedicos,matrizPacientes)


def main():
    matrizMedicos = [[1245, 'João Pedro', '14/01/1990', 'M', 'Geriatra', 'Unip', 'joaop@google.com', 124578964], [8962, 'Juliana Pereira', '29/07/1982', 'F', 'Dermatologista', 'UFScar', 'julianap@google.com', 951423687]]
    matrizPacientes = [[12345678920, 'Pedro Coelho', '06/11/2002', 'M', 'Plano Especial 1', 'pedro.coelho@google.com', 114578451],[75314710162, 'Gabriela Santos', '10/05/2000', 'F', 'Plano especial 2', 'gabielaS@google.com', 1154712359 ]]
    menu_principal(matrizMedicos, matrizPacientes)


main()