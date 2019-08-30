from random import shuffle
from random import gauss
from random import random

import os
os.system('cls' if os.name == 'nt' else 'clear')

def database(file_data):
    
    file = open(file_data,"r")
    lines = file.readlines()
    file.close()

    customers = []
    for i in range(len(lines)):
        index_list = lines[i].split('\t')
        customers.append(index_list)

    return customers

def integerList(data_list):

    age = data_list[0]

    sex = 0
    if data_list[2] == 'female': sex = 2
    if data_list[2] == 'male': sex = 1

    employment = int(data_list[2])

    home = 0
    if data_list[3]=='free': home = -10
    if data_list[3]=='rent': home = 1
    if data_list[3]=='own': home = 30

    savings_account = 0
    if data_list[4] == 'no': savings_account = -200
    if data_list[4] == 'little': savings_account = -5
    if data_list[4] == 'moderate': savings_account = 1
    if data_list[4] == 'rich': savings_account = 5
    if data_list[4] == 'quite rich': savings_account = 50

    checking_account = 0
    if data_list[5] == 'no': checking_account = -200
    if data_list[5] == 'little': checking_account = -5
    if data_list[5] == 'moderate': checking_account = 1
    if data_list[5] == 'rich': checking_account = 5
    if data_list[5] == 'quite rich': checking_account = 50

    credit_claim = int(data_list[6])

    time = int(data_list[7])

    purpose = 0
    if data_list[8]=='radio/TV': purpose = 50
    if data_list[8]=='domestic appliances': purpose = 20
    if data_list[8]=='repairs': purpose = 10
    if data_list[8]=='furniture/equipment': purpose = 1
    if data_list[8]=='car': purpose = -20
    if data_list[8]=='vacation/others': purpose = -21
    if data_list[8]=='education': purpose = -30
    if data_list[8]=='business': purpose = -50

    approval = int(data_list[9])
    
    integer_list = [age, sex, employment, home, savings_account, checking_account, credit_claim, time, purpose, approval]
    
    return integer_list

def entireCustomerData(data_list):

    age = data_list[0]

    sex = 0
    if data_list[2] == 'female': sex = 2
    if data_list[2] == 'male': sex = 1

    employment = int(data_list[2])

    home = 0
    if data_list[3]=='free': home = -10
    if data_list[3]=='rent': home = 1
    if data_list[3]=='own': home = 30

    savings_account = 0
    if data_list[4] == 'no': savings_account = -200
    if data_list[4] == 'little': savings_account = -5
    if data_list[4] == 'moderate': savings_account = 1
    if data_list[4] == 'rich': savings_account = 5
    if data_list[4] == 'quite rich': savings_account = 50

    checking_account = 0
    if data_list[5] == 'no': checking_account = -200
    if data_list[5] == 'little': checking_account = -5
    if data_list[5] == 'moderate': checking_account = 1
    if data_list[5] == 'rich': checking_account = 5
    if data_list[5] == 'quite rich': checking_account = 50

    credit_claim = int(data_list[6])

    time = int(data_list[7])

    purpose = 0
    if data_list[8]=='radio/TV': purpose = 50
    if data_list[8]=='domestic appliances': purpose = 20
    if data_list[8]=='repairs': purpose = 10
    if data_list[8]=='furniture/equipment': purpose = 1
    if data_list[8]=='car': purpose = -20
    if data_list[8]=='vacation/others': purpose = -21
    if data_list[8]=='education': purpose = -30
    if data_list[8]=='business': purpose = -50
    
    integer_list = [age, sex, employment, home, savings_account, checking_account, credit_claim, time, purpose]
    
    return integer_list

def calibrateList(data_list):

    alphas_list = []

    for a in range(9):
        alphas = gauss(0.00005,0.00000001)
        alphas_list.append(alphas)
    
    for e in range(50):
        shuffle(data_list)
        for i in data_list:       
            customer_list = i

            alphas_table = []            

            adder = 0
            for o in range (9):
                adder = adder + (int(customer_list[o]) * int(alphas_list[o]))

            prediction = 0    

            prediction = +1 if adder >= 0 else -1      

            alphas_table.append(alphas_list)

            #proximaListaDePesos = []

            for n in range(9):
                alphas_list[n] = alphas_list[n] + 0.001 * (prediction - int(customer_list[-1])) * int(customer_list[n])
        
    return alphas_list

def calibrateCustomerData(data):

    alphas_list = []

    for a in range(9):
        alphas = gauss(0.00005,0.00000001)
        alphas_list.append(alphas)
         
        customer_list = data
    
    alphas_table = []

    adder = 0
    for i in range (9):
        adder = adder + (int(customer_list[i]) * int(alphas_list[i]))

    prediction = 0    

    prediction = +1 if adder >= 0 else -1      

    alphas_table.append(alphas_list)

    return prediction

def creditRequest():
    print("Solitação de crédito")
    print('')
    
    client              = []
    age                 = int(input("Informe sua idade: "))
    sex                 = input("Informe o seu sexo: ")
    employment          = int(input("Informe o nivel do seu emprego: "))
    home                = input("Informe o tipo da sua habitação: ")
    savings_account     = input("Condição da sua conta poupança: ")
    checking_account    = input("Condição da sua conta corrente: ")
    credit_claim        = int(input("Informe o valor solicitado: "))
    time                = int(input("Tempo de pagamento (em meses): "))
    purpose             = input("Informe sua pretensão com esse emprestimo: ")

    client = [age, sex, employment, home, savings_account, checking_account, credit_claim, time, purpose]
    return client

#Area de testes


#Area de execução do programa    

print('Digite o número da opção desejada \n')
print('1. Calibrar os coeficientes \n')
print('2. Porcentagem de acertos \n')
print('3. Predizer solicitação de credito \n')

option = int(input('Qual operação você deseja? '))
print('') 

if(option == 1): 
    print('Você escolheu \'Calibrar os coeficientes\'')
    
    data_list = database('listacalibragem.txt')

    list_of_customers = []
    
    for a in range(len(data_list)):
        
        list_of_customers.append(integerList(data_list[a]))
            
    calibrated_list = calibrateList(list_of_customers)
    
    print('') 
    print("Alfas calibrados: ",calibrated_list) 

if(option == 2): 
    print('Você escolheu \'Porcentagem de acertos\'')

    data_list = database('listacalibragem.txt')

    list_of_customers = []
    
    for a in range(len(data_list)):
        
        list_of_customers.append(integerList(data_list[a]))
            
    calibrated_list = calibrateList(list_of_customers)

    success = 0
    positive = 0

    for e in range (len(list_of_customers)):
        adder = 0
        for i in range (len(calibrated_list)):
            adder = adder + (int(calibrated_list[i]) * int(list_of_customers[e][i]))
        
        result = 1 if adder >= 0 else -1 

        if list_of_customers[e][-1] == result:
            success = success + 1

        if list_of_customers[e][-1] == 1:
            positive = positive + 1

    print('') 
    print("Positivos: ", success, " de ", len(list_of_customers) ) 
    rate = round(success / (len(list_of_customers) / 100), 2)
    print('Taxa de sucesso: ', rate, '%')
    
if(option == 3):
    print('Você escolheu \'Predizer solicitação de credito\'')
    
    client = creditRequest()
    entire_customer_data = entireCustomerData(client)
            
    calibrated_list = calibrateCustomerData(entire_customer_data)
    
    if calibrated_list == 1:
        print('')
        print('Sua solicitação de credito foi aprovada')
    else:
        print('')
        print('Sua solicitação de credito foi reprovada')