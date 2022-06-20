###########################################################
#        FUNÇOES PARA LISTAR TODOS USUARIOS/CONSULTA
###########################################################
def listarTodosMed(matrizMedicos):

    print('=-'*15, 'LISTAR TODOS USUÁRIOS', '=-'*15, '\n')
    for i in range(len(matrizMedicos)):
        for j in range(len(matrizMedicos[i])):
            print([matrizMedicos[i][j]], end=" ")
        print('\n')
    return matrizMedicos
                                                    
def listarTodosPac(matrizPacientes):
    
    print('=-'*15, 'LISTAR TODOS USUÁRIOS', '=-'*15, '\n')
    for i in range(len(matrizPacientes)):
        for j in range(len(matrizPacientes[i])):
            print([matrizPacientes[i][j]], end= " ")
        print('\n')
    return matrizPacientes

def listarTodosCons(matrizConsultas):
    print('=-' * 15, 'LISTAR TODAS AS CONSULTAS', '=-' * 15, '\n')
    for i in range(len(matrizConsultas)):
        for j in range(len(matrizConsultas[i])):
            print([matrizConsultas[i][j]], end=" ")
        print('\n')
    return matrizConsultas

###########################################################
#        FUNÇOES PARA LISTAR ELEMENTOS ESPECIFICOS DOS USUARIOS/CONSULTA
###########################################################
def listarElementoMed(matrizMedicos): ### Listar médico
    
    print('=-'*15, 'LISTAR ELEMENTO', '=-'*15, '\n')
    digito = True
    while digito:
        crm = input("Informe o CRM do médico que deseja listar: ")
        encontrou = localizarMed(matrizMedicos,crm)
        if encontrou:
            i=0
            for j in range(len(matrizMedicos[i])):
                print(matrizMedicos[i][j])

            digito = False
            
        else:
            print("CRM digitado incorretamente, tente novamente \n")
    return matrizMedicos

def listarElementoPac(matrizPacientes): ### Listar paciente
    
    print('=-'*15, 'LISTAR ELEMENTO', '=-'*15, '\n')
    digito = True
    while digito:
        cpf = input("Informe o CPF do paciente que deseja listar: ")
        encontrou = localizarPac(matrizPacientes,cpf)
        if encontrou:
            i=0
            for j in range(len(matrizPacientes[i])):
                print(matrizPacientes[i][j])

            digito = False
            
        else:
            print("CPF digitado incorretamente, tente novamente \n")
    return matrizPacientes

def listarElementoCons(matrizConsultas): ### Listar consulta

    print('=-' * 15, 'LISTAR CONSULTA', '=-' * 15, '\n')
    digito = True
    while digito:
        crm= input("Informe o CRM do médico: ")
        cpf = input("Informe o CPF do paciente: ")
        encontrou_crm = matrizConsultas(matrizConsultas,crm)
        encontrou_cpf = localizarCons_CPF(matrizConsultas, cpf)
        if encontrou_cpf and encontrou_crm:
            i = 0
            for j in range(len(matrizConsultas[i])):
                print(matrizConsultas[i][j])
            digito = False
        else:
            print("CPF digitado incorretamente, tente novamente \n")
    return matrizConsultas

###########################################################
#        FUNÇOES PARA VERIFICAR EXISTENCIA DE USUARIOS
###########################################################
def localizarMed(matrizMedicos,crm): ### Localizar medico
    existe=False
    if crm.isdigit():
        for i in range(len(matrizMedicos)):
            if matrizMedicos[i][0] == crm:
                existe=True
                return existe
            else:
                existe=False
    else:
        existe= True
    return existe

def localizarPac(matrizPacientes,cpf): ### Localizar paciente
    existe=False
    if cpf.isdigit():
        for i in range(len(matrizPacientes)):
            if matrizPacientes[i][0] == cpf:
                existe=True
                return existe
            else:
                existe=False
    else:
        existe=True
    return existe

###########################################################
#        FUNÇOES PARA LOCALIZAR ELEMENTOS DAS CONSULTAS
###########################################################
def localizarCons_CRM(matrizConsulta,crm): ### Localizar crm na matriz consulta
    existe=False
    if crm.isdigit():
        for i in range(len(matrizConsulta)):
            if matrizConsulta[i][0] == crm:
                existe=True
                return existe
            else:
                existe=False
    else:
        existe=False
    return existe

def localizarCons_CPF(matrizConsulta, cpf):### Localizar cpf na matriz consulta
    existe = False
    if cpf.isdigit():
        for i in range(len(matrizConsulta)):
            if matrizConsulta[i][1] == cpf:
                existe = True
                return existe
            else:
                existe = False
    else:
        existe=False
    return existe

def localizarCons_DATA(matrizConsulta, data):### Localizar data na matriz consulta
    existe = False
    sem_espaco=data.replace("-","")
    if sem_espaco.isdigit():
        for i in range(len(matrizConsulta)):
            for j in range(len(matrizConsulta[i])):
                if data == matrizConsulta[i][2]:
                     existe=True
                     return existe
                else:
                    existe= False
    else:
        existe = False

    return existe

def localizarCons_HORA(matrizConsulta, hora): ### Localizar hora na matriz consulta
    existe = False
    sem_espaco = hora.replace("-", "")
    if sem_espaco.isdigit():
        for i in range(len(matrizConsulta)):
            for j in range(len(matrizConsulta[i])):
                if hora == matrizConsulta[i][3]:
                    existe = True
                    return existe
                else:
                    existe = False
    else:
        existe = False

    return existe

###########################################################
#        FUNÇOES PARA ADICIONAR USUARIOS/CONSULTA
###########################################################
def incluirMed(matrizMedicos): ### adicionar medicos
    #with open('medicos', 'a', encoding="utf-8") as escrita_med:
    print('=-'*15, 'ADICIONAR USUÁRIO', '=-'*15, '\n')
    cadmed=False  ### se é numero
    novo_med = []
    while cadmed==False:

        crm=input('Digite o CRM: ')
        existe=localizarMed(matrizMedicos,crm)
        if existe==False:
            novo_med.append(crm)
            cadmed=True

        elif existe==True:
            print('Este usuário já está cadastrado ou digitado incorretmante')
            cadmed=False

    nomeletra=True
    while nomeletra:                                                    ############## VERIFICA SE O NOME É LETRA
        nomemed=(input('Digite o nome: '))
        sem_espaco=nomemed.replace(" ","")
        if sem_espaco.isalpha() is True:
            novo_med.append(nomemed)
            nomeletra=False
        else:
            print('Digite caracteres válidos ')
    data=True
    while data:                                                         ############# VERIFICA SE A DATA DE NASCIMENTO É NUMERO
        lista_nasc=[]
        nascimento=(input('Digite a data de nascimento (dd/mm/aaaa): '))
        numero=nascimento.replace("/","-").replace(" ","-").isdigit()
        if numero:
            lista_nasc.append(nascimento)
            novo_med.append(lista_nasc)
            data=False
        else:
            print('Digite corretamente')
    genero=True
    while genero:                                                       ############# VERIFICA SE O SEXO É LETRA
        sexo=(input('Digite o sexo: '))
        letra=sexo.isalpha()
        if letra:
            novo_med.append(sexo)
            genero=False
        else:
            print('Digite corretamente')
    novo_med.append(input('Digite a especialidade: '))
    novo_med.append(input('Digite a universidade: '))
    arroba=True
    while arroba:                                                      ############# VERIFICA SE O EMAIL TEM UM @
        email=input("Digite o email: ")
        if '@' not in email:
            print('digite corretamente')
        else:
            novo_med.append(email)
            arroba=False
            var1=True
            while var1:
                email=input("adicionar novo email? (S/N)")
                if email== 'N' or email=='n':
                    var1=False
                elif email== 'S' or email=='s':
                    novo_med.append(str(input('Digite outro email: ')))
                else:
                    print('digite novamente (S/N) ')
    phone=True
    while phone:                                                       ############# VERIFICA SE O TELEFORE TEM NUMEROS
        telefone=input('Digite o telefone: ')
        tele=telefone.isdigit()
        if not tele:
            print('Digite corretamente')
        else:
            novo_med.append(telefone)
            phone=False
            var2=True
            while var2:
                tele=input("adicionar novo telefone? (S/N)")
                if tele== 'N' or tele=='n':
                    var2=False
                elif tele== 'S' or tele=='s':
                    novo_med.append(input('Digite outro telefone: '))
                else:
                    print('digite novamente (S/N) ')

    matrizMedicos.append(novo_med)
    print('\n Usuário adicionado com sucesso! \n')
    return matrizMedicos

def incluirPac(matrizPacientes): ### Adicionar pacientes
    cadpac=False  ### se é numero
    novo_pac = []
    while cadpac==False:

        cpf=input('Digite o CPF: ')
        existe=localizarPac(matrizPacientes,cpf)
        if existe==False:
            novo_pac.append(cpf)
            cadpac=True
            
        elif existe==True:
            print('Este usuário já está cadastrado ou digitado incorretmante')
            cadpac=False
    nomeletra=True
    while nomeletra:                                                   ############# VERIFICA SE O NOME TEM LETRAS
        nomepac=(input('Digite o nome: '))
        sem_espaco=nomepac.replace(" ","")
        if sem_espaco.isalpha() is True:
            novo_pac.append(nomepac)
            nomeletra=False
        else:
            print('Digite caracteres válidos ')
    data=True
    while data:                                                         ############# VERIFICA SE A DATA DE NASCIMENTO É NUMERO
        lista_nasc=[]
        nascimento=(input('Digite a data de nascimento (dd mm aaaa): '))
        numero=nascimento.replace("/","-").replace(" ","-").isdigit()
        if numero:
            lista_nasc.append(nascimento)
            novo_pac.append(lista_nasc)
            data=False
        else:
            print('Digite corretamente')
    genero=True
    while genero:                                                       ############# VERIFICA SE O SEXO É LETRA
        sexo=(input('Digite o sexo: '))
        letra=sexo.isalpha()
        if letra:
            novo_pac.append(sexo)
            genero=False
        else:
            print('Digite corretamente')
    novo_pac.append(input('Digite a especialidade: '))
    novo_pac.append(input('Digite a universidade: '))
    arroba=True
    while arroba:                                                      ############# VERIFICA SE O EMAIL TEM UM @
        email=input("Digite o email: ")
        if '@' not in email:
            print('digite corretamente')
        else:
            novo_pac.append(email)
            arroba=False
            var1=True
            while var1:    
                email=input("adicionar novo email? (S/N)")
                if email== 'N' or email=='n':
                    var1=False
                elif email== 'S' or email=='s':    
                    novo_pac.append(str(input('Digite outro email: ')))
                else:
                    print('digite novamente (S/N) ')
    phone=True
    while phone:                                                       ############# VERIFICA SE O TELEFORE TEM NUMEROS
        telefone=input('Digite o telefone: ')
        tele=telefone.isdigit()
        if not tele:
            print('Digite corretamente')
        else:
            novo_pac.append(telefone)
            phone=False
            var2=True
            while var2:    
                tele=input("adicionar novo telefone? (S/N)")
                if tele== 'N' or tele=='n':
                    var2=False
                elif tele== 'S' or tele=='s':
                    novo_pac.append(input('Digite outro telefone: '))
                else:
                    print('digite novamente (S/N) ')
    matrizPacientes.append(novo_pac)                
    print('\n Usuário adicionado com sucesso! \n')
    return matrizPacientes

def incluirCons(matrizConsultas): ### adicionar consultas

    print('=-' * 15, 'ADICIONAR CONSULTA', '=-' * 15, '\n')
    medico = False  ### se é numero
    nova_cons = []
    while medico == False:
        crm = input('CRM do médico responsável: ')
        existe_crm = localizarCons_CRM(matrizConsultas, crm)
        if existe_crm == False:
            nova_cons.append(crm)
            medico = True
        elif existe_crm == True:
            print('Esta consulta já está cadastrada ou CRM foi digitado incorretmante')
            medico = False

    paciente = False  ### se é numero
    while paciente == False:
        cpf = input('Digite o CPF: ')
        existe_cpf = localizarCons_CPF(matrizConsultas, cpf)
        if existe_cpf == False:
            nova_cons.append(cpf)
            paciente = True
        elif existe_cpf == True:
            print('Esta consulta já está cadastrada ou CPF foi digitado incorretmante')
            paciente = False

    DAT=False           ### se é numero
    while DAT == False:
        lista_data = []
        data = (input('Digite a data da consulta (dd mm aaaa): '))
        existe_data= localizarCons_DATA(matrizConsultas,data)
        if existe_data == False:
            numero = data.replace("/", " ").replace("-", " ").isdigit()
            if numero:
                lista_data.append(data)
                nova_cons.append(lista_data)
                DAT = True
            else:
                print('Digite corretamente\n')
                DAT = False
        else:
            print('Esta consulta já está cadastrada ou DATA foi digitada incorretmante')

    hour=False      ### se é numero
    while hour == False:
        lista_hora=[]
        hora= input('Digite a hora (hh mm): ')
        existe_hora= localizarCons_HORA(matrizConsultas,hora)
        if existe_hora == False:
            numero = hora.replace(":"," ")
            if numero:
                lista_hora.append(hora)
                nova_cons.append(lista_hora)
                hour=True
            else:
                print('Digite corretamente\n')
                hour = False
        else:
            print('Esta consulta já está cadastrada ou HORA foi digitada incorretmante')


    nova_cons.append(input("Digite o diagnóstico: "))
    nova_cons.append(input('Digite os medicamentos: '))

    matrizConsultas.append(nova_cons)
    return matrizConsultas


###########################################################
#        FUNÇOES PARA ALTERAR USUARIOS/CONSULTA
###########################################################
def alterarMed(matrizMedicos):
   
    print('=-'*15, 'ALTERAR USUÁRIO', '=-'*15, '\n')
    #verificar se o medico existe
    digito = True
    indice = 0
    while digito:
        crm = input("Informe o CRM do médico: ")
        encontrou = localizarMed(matrizMedicos,crm)
        if encontrou:
            for i in range(len(matrizMedicos)):
                if matrizMedicos[i][0] == crm:
                    indice=i
            digito = False
        else:
            print("CRM digitado incorretamente, tente novamente")

    print("1. Alterar todos os dados do usuário")
    print("2. Alterar um dado específico")

    escolha=int(input())

    if escolha==1:                                                 ################ alterar completamente um usuário
        del matrizMedicos[indice]
        incluirMed(matrizMedicos)

    elif escolha==2:                                               ################ alterar info especifica
        info=0
        for i in range(len(matrizMedicos[indice])):
            print('\n',info,[matrizMedicos[indice][i]])
            info+=1
        dado=int(input('Qual informação gostaria de alterar? '))
        atualizacao=input('digite o novo dado: ')
        if dado == 2:
            for i in range(len(matrizMedicos[indice])):
                for j in range(len(matrizMedicos[indice][i])):
                    matrizMedicos[indice][dado] = atualizacao
        else:
            for i in range(len(matrizMedicos[indice])):
                matrizMedicos[indice][dado]=atualizacao
    print("Alteração realizada com sucesso \n")
    return matrizMedicos
    
def alterarPac(matrizPacientes):
    
    print('=-'*15, 'ALTERAR USUÁRIO', '=-'*15, '\n')
    digito = True
    indice = 0
    while digito:
        cpf = input("Informe o CPF do paciente: ")
        encontrou = localizarPac(matrizPacientes,cpf)
        if encontrou:
            for i in range(len(matrizPacientes)):
                if matrizPacientes[i][0] == cpf:
                    indice=i
            digito = False
        else:
            print("CPF digitado incorretamente, tente novamente")

    print("1. Alterar todos os dados de um usuário")
    print("2. Alterar um dado específico de um usuário")
    escolha=int(input())

    if escolha==1:                                                 ############# alterar completamente um usuário

        del matrizPacientes[indice]
        incluirPac(matrizPacientes)

    elif escolha==2:                                               ############## alterar info especifica
        info=0
        for i in range(len(matrizPacientes[indice])):
            print('\n',info,[matrizPacientes[indice][i]])
            info+=1
        dado=int(input('Qual informação gostaria de alterar? '))
        atualizacao=input('digite o novo dado: ')
        if dado == 2:
            for i in range(len(matrizPacientes[indice])):
                for j in range(len(matrizPacientes[indice][i])):
                    matrizPacientes[indice][dado] = atualizacao
        else:
            for i in range(len(matrizPacientes[indice])):
                matrizPacientes[indice][dado]=atualizacao
    print("Alteração realizada com sucesso \n")
    return matrizPacientes

def alterarCons(matrizConsultas):
    print('=-' * 15, 'ALTERAR CONSULTA', '=-' * 15, '\n')
    digito = True
    indice = 0
    while digito:
        crm = input("Informe o CRM do médico: ")
        cpf= input('Digite o CPF do paciente: ')
        data= input('Digite a data da consulta: ')
        hora = input('Digite a hora da consulta: ')
        encontrou_crm = localizarCons_CRM(matrizConsultas, crm)
        encontrou_cpf= localizarCons_CPF(matrizConsultas,cpf)
        encontou_data= localizarCons_DATA(matrizConsultas,data)
        encontrou_hora= localizarCons_HORA(matrizConsultas,hora)
        if encontrou_crm and encontrou_hora and encontrou_cpf and encontou_data:
            for i in range(len(matrizConsultas)):
                if matrizConsultas[i][0] == crm and matrizConsultas[i][1] == cpf and matrizConsultas[i][2] == data and matrizConsultas[i][3] == hora:
                    indice = i
            digito = False
        else:
            print("Informações não encontradas, tente novamente\n")

    print("1. Alterar todos os dados de um usuário")
    print("2. Alterar um dado específico de um usuário")
    escolha = int(input())

    if escolha == 1:  ############# alterar completamente uma consulta
        del matrizConsultas[indice]
        incluirCons(matrizConsultas)

    elif escolha == 2:
        info = 0
        for i in range(len(matrizConsultas[indice])):
            print('\n', info, [matrizConsultas[indice][i]])
            info += 1
        dado = int(input('Qual informação gostaria de alterar? '))
        atualizacao = input('digite o novo dado: ')
        for i in range(len(matrizConsultas[indice])):
            matrizConsultas[indice][dado] = atualizacao
    print("Alteração realizada com sucesso \n")

    return matrizConsultas

###########################################################
#        FUNÇOES PARA EXCLUIR USUARIOS/CONSULTA
###########################################################
def excluirMed(matrizMedicos):

    print('=-'*15, 'EXCLUIR USUÁRIOS', '=-'*15, '\n')

    digito = True
    while digito:
        crm = input("Informe o CRM do médico: ")
        encontrou = localizarMed(matrizMedicos,crm)
        if encontrou:
            i=0
            while i < len(matrizMedicos):
                if matrizMedicos[i][0]==crm:
                    del (matrizMedicos[i])
                    print('\n Dados excluídos com sucesso. \n')
                i+=1
            digito = False
        else:
            print("CRM incorreto, tente novamente")
    return matrizMedicos

def excluirPac(matrizPacientes):

    print('=-'*15, 'EXCLUIR USUÁRIOS', '=-'*15, '\n')
    digito = True
    while digito:
        cpf = input("Informe o CPF do paciente: ")
        encontrou = localizarPac(matrizPacientes,cpf)
        if encontrou:
            i=0
            while i < len(matrizPacientes):
                if matrizPacientes[i][0]==cpf:
                    del (matrizPacientes[i])
                    print('\n Dados excluídos com sucesso. \n')
                i+=1
            digito = False
        else:
            print("CPF incorreto, tente novamente")
    return matrizPacientes

def excluirCons(matrizConsultas):
    digito = True
    indice = 0
    while digito:
        crm = input("Informe o CRM do médico: ")
        cpf = input('Digite o CPF do paciente: ')
        data = input('Digite a data da consulta: ')
        hora = input('Digite a hora da consulta: ')
        encontrou_crm = localizarCons_CRM(matrizConsultas, crm)
        encontrou_cpf = localizarCons_CPF(matrizConsultas, cpf)
        encontou_data = localizarCons_DATA(matrizConsultas, data)
        encontrou_hora = localizarCons_HORA(matrizConsultas, hora)
        if encontrou_crm and encontrou_hora and encontrou_cpf and encontou_data:
            for i in range(len(matrizConsultas)):
                if matrizConsultas[i][0] == crm and matrizConsultas[i][1] == cpf and matrizConsultas[i][2] == data and matrizConsultas[i][3] == hora:
                    indice = i
                    del matrizConsultas[indice]
            digito = False
        else:
            print("Informações não encontradas, tente novamente\n")
    return matrizConsultas

###########################################################
#        FUNÇAO PARA IMPRIMIR OPÇOES DOS MENUS
###########################################################
def printopt():
    print('\n', '-='*15, 'SUB MENUS','-='*15, '\n')
    print('1. Listar todos')
    print('2. Listar elemento específico')
    print('3. incluir')
    print('4. alterar')
    print('5. excluir')
    print('0. Voltar ao Menu principal')

###########################################################
#        SUBMENU MEDICOS
###########################################################
def submenuMedicos(matrizMedicos):
    continuar=1
    while continuar != 0:
        printopt()
        operacao = int(input('Digite qual menu gostaria de acessar: \n'))

        if operacao == 1:
            matrizMedicos=listarTodosMed(matrizMedicos)
        elif operacao == 2:
            matrizMedicos=listarElementoMed(matrizMedicos)
        elif operacao == 3:
            matrizMedicos=incluirMed(matrizMedicos)
        elif operacao == 4:
            matrizMedicos=alterarMed(matrizMedicos)
        elif operacao == 5:
            matrizMedicos=excluirMed(matrizMedicos)
        elif operacao == 0:
            continuar=0
    escreve_med(matrizMedicos)


###########################################################
#        SUBMENU PACIENTES
###########################################################
def submenuPacientes(matrizPacientes):
    continuar=1
    while continuar != 0:
        printopt()        
        operacao = int(input('Digite qual menu gostaria de acessar: \n'))

        if operacao == 1:
            matrizPacientes=listarTodosPac(matrizPacientes)
        elif operacao == 2:
            matrizPacientes=listarElementoPac(matrizPacientes)
        elif operacao == 3:
            matrizPacientes=incluirPac(matrizPacientes)
        elif operacao == 4:
            matrizPacientes=alterarPac(matrizPacientes)
        elif operacao == 5:
            matrizPacientes=excluirPac(matrizPacientes)
        elif operacao == 0:
            continuar = 0
    escreve_pac(matrizPacientes)

###########################################################
#        SUBMENU CONSULTAS
###########################################################
def submenuConsultas(matrizConsultas):
    continuar=1
    while continuar != 0:
        printopt()
        operacao = int(input('Digite qual menu gostaria de acessar: \n'))

        if operacao == 1:
            matrizConsultas=listarTodosCons(matrizConsultas)
        elif operacao == 2:
            matrizConsultas=listarElementoCons(matrizConsultas)
        elif operacao == 3:
            matrizConsultas=incluirCons(matrizConsultas)
        elif operacao == 4:
            matrizConsultas=alterarCons(matrizConsultas)
        elif operacao == 5:
            matrizConsultas=excluirCons(matrizConsultas)
        elif operacao == 0:
            continuar = 0
    escreve_consulta(matrizConsultas)

###########################################################
#        SUBMENU RELATORIOS
###########################################################
def submenuRelatorios(matrizMedicos,matrizPacientes,matrizConsultas):
    continuar = 1
    while continuar != 0:
        print('1. Listar médicos por especialidades.')
        print('2. Listar pacientes por idade.')
        print('3. Listar consulta por data.')
        print('0. Sair.')
        operacao = int(input('Digite qual menu gostaria de acessar: \n'))

        if operacao == 1:
            relatorio_A(matrizMedicos)
        elif operacao == 2:
            relatorio_B(matrizPacientes)
        elif operacao == 3:
            relatorio_C(matrizMedicos,matrizPacientes,matrizConsultas)
        elif operacao == 0:
            continuar = 0

#        FUNÇÃO PARA LISTAR ESPECIALIDADES
def relatorio_A(matrizMedicos): # LISTAR MÉDICOS POR ESPECIALIDADES
    especialidade = input('Digite a especialidade: ')
    usuario = matrizMedicos[0]
    Lista=[]
    for i in range(len(matrizMedicos)):
        for j in range(len(matrizMedicos[i])):
            if especialidade in matrizMedicos[i][j]:
                usuario = matrizMedicos[i]
                Lista.append(usuario)
    print(Lista)

#        FUNÇÃO PARA LISTAR POR IDADE
def relatorio_B(matrizPacientes): # LISTAR USUARIOS ATÉ CERTA IDADE
    anos = int(input("Listar pacientes até que idade (em anos)?  "))
    idades = []
    for i in range(len(matrizPacientes)):
        for j in range(len(matrizPacientes[i])):
            nasc = matrizPacientes[i][2]
            teste = nasc[0]
            teste2 = teste.split(' ')
            for x in teste2:
                idades.append(int(x))

        ano = 2022
        if ano - idades[2] <= anos:
            print(matrizPacientes[i], end=" ")
            print('\n')

#        FUNÇÃO PARA LISTAR CONSULTA POR DATAS
def relatorio_C(matrizMedicos,matrizPacientes,matrizConsultas):
    data=input("Digite a data das consultas: ")
    lista = []
    existe= localizarCons_DATA(matrizConsultas,data)
    if existe:
        for i in range(len(matrizConsultas)):

            if data in matrizConsultas[i]:
                lista.append(matrizMedicos[i][0])
                lista.append(matrizMedicos[i][1])
                lista.append(matrizPacientes[i][0])
                lista.append(matrizPacientes[i][1])
                lista.append(matrizConsultas[i][2:])

        print(lista)
    else:
        print('Nenhum registro encontrado\n')


###########################################################
#        MENU PRINCIPAL
###########################################################
def menu_principal(matrizMedicos, matrizPacientes, matrizConsultas):
    continuar = 1
    while continuar != 0:
        print('\n','-='*15,'MENU PRINCIPAL','-='*15,'\n')
        print('1. Médicos')
        print('2. Pacientes')
        print('3. Consultas')
        print('4. Relatórios')
        print('5. Sair')

        opcaoSubmenu = int(input('Digite qual menu gostaria de acessar: \n'))

        if opcaoSubmenu == 1:
             matrizMedicos = submenuMedicos(matrizMedicos)
        elif opcaoSubmenu == 2:
            matrizPacientes = submenuPacientes(matrizPacientes)
        elif opcaoSubmenu == 3:
            matrizConsultas = submenuConsultas(matrizConsultas)
        elif opcaoSubmenu == 4:
            submenuRelatorios(matrizMedicos,matrizPacientes,matrizConsultas)
        elif opcaoSubmenu == 5:
            continuar = 0

###########################################################
#        MAIN
###########################################################
def main():
    matrizMedicos = abrir_med()
    matrizPacientes = abrir_pac()
    matrizConsultas = abrir_consulta()
    menu_principal(matrizMedicos, matrizPacientes, matrizConsultas)


###########################################################
#        ABRIR ARQUIVOS
###########################################################

#        FUNÇÃO PARA ABRIR O ARQUIVO DOS MEDICOS
def abrir_med():
    arq=open('medicos', 'r', encoding="utf-8")
    conteudo=arq.readlines()

    matrizMedicos = []
    for linha in conteudo:
        linha = linha.split()
        matrizMedicos.append(linha)

    arq.close()
    return matrizMedicos

#        FUNÇÃO PARA ABRIR O ARQUIVO DOS PACIENTES
def abrir_pac():
    arq = open('pacientes', 'r', encoding="utf-8")
    conteudo = arq.readlines()

    matrizPacientes = []
    for linha in conteudo:
        linha = linha.split()
        matrizPacientes.append(linha)

    arq.close()
    return matrizPacientes

#        FUNÇÃO PARA ABRIR O ARQUIVO DAS CONSULTAS
def abrir_consulta():
    arq = open('consultas', 'r', encoding="utf-8")
    conteudo = arq.readlines()

    matrizConsultas= []
    for linha in conteudo:
        linha = linha.split()
        matrizConsultas.append(linha)

    arq.close()
    return matrizConsultas

###########################################################
#        SOBRESCREVER ARQUIVOS
###########################################################

#        FUNÇÃO PARA ABRIR ACRESCENTAR INFORMAÇOES NO ARQUIVO DOS MEDICOS
def escreve_med(matrizMedicos):
    arq = open('medicos', 'w', encoding="utf-8")
    linha= ""
    for item in matrizMedicos:
        linha = str(item)
        linha = linha.replace("[","").replace("]","").replace(",","").replace("'","")

        arq.write(linha)
        arq.write('\n')
    arq.close()

#        FUNÇÃO PARA ABRIR ACRESCENTAR INFORMAÇOES NO ARQUIVO DOS PACIENTES
def escreve_pac(matrizPacientes):
    arq = open('pacientes', 'w', encoding="utf-8")
    linha = ""
    for item in matrizPacientes:
        linha = str(item)
        linha = linha.replace("[", "").replace("]", "").replace(",", "").replace("'", "")

        arq.write(linha)
        arq.write('\n')
    arq.close()

#        FUNÇÃO PARA ABRIR ACRESCENTAR INFORMAÇOES NO ARQUIVO DAS CONSULTAS
def escreve_consulta(matrizConsultas):
    arq = open('consultas', 'w', encoding="utf-8")
    linha = ""
    for item in matrizConsultas:
        linha = str(item)
        linha = linha.replace("[", "").replace("]", "").replace(",", "").replace("'", "")

        arq.write(linha)
        arq.write('\n')
    arq.close()


###########################################################
#        PROGRAMA PRINCIPAL
###########################################################
main()