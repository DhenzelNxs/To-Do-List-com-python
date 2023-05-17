import mysql.connector


conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='gamer@gamer',
    database='atividades_pessoais',
)

cursor = conexao.cursor()

def criar(atividade, status='A fazer'):
    comando = f'''Insert into atividades values('{atividade}', '{status}')'''
    cursor.execute(comando)
    conexao.commit()
    print('Sua Atividade foi adicionada\n')

# READ

class Ler:
    def ler_tudo():
        comando = f'select * from atividades'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        return resultado
    def ler_feitos():
        comando = f'''select * from atividades where stats = 'feito' '''
        cursor.execute(comando)
        resultado = cursor.fetchall()
        return resultado
    def ler_Fazendo():
        comando = f'''select * from atividades where stats = 'fazendo' '''
        cursor.execute(comando)
        resultado = cursor.fetchall()
        return resultado
    def ler_afazer():
        comando = f'''select * from atividades where stats = 'A fazer' '''
        cursor.execute(comando)
        resultado = cursor.fetchall()
        return resultado

# UPDATE

def atualizar(atividade = str, status = str):
    comando = f'''update atividades set stats = '{status}' where nome_ativ = '{atividade}' '''
    cursor.execute(comando)
    conexao.commit()
    print('atividade atualizada com sucesso\n')

# DELETE

def deletar(atividade):
    comando = f'''delete from atividades where nome_ativ = '{atividade}' '''
    cursor.execute(comando)
    conexao.commit()
    print('A atividade foi deletada com sucesso\n')


run = True
while run:
    opcoes = input('''Oque deseja Fazer hoje ? \n1 - Adicionar Atividade \n2 - Atualizar status da atividade \n3 - Apagar atividade \n4 - mostrar atividades \n5 - Exit \ninforme: ''')

    if opcoes == '':
        print('Por favor digite um numero valido \n')

    elif int(opcoes) == 1:
        atividade = input('Informe a atividade que você quer adicionar: \n')
        criar(atividade)

    elif int(opcoes) == 2:
        resultado = Ler.ler_tudo()
        for i in range(len(resultado)):
            print(resultado[i])
        atividade = input('Informe a atividade:\n')
        status = input('Informe o status:\n')
        atualizar(atividade, status)

    elif int(opcoes) == 3:
        resultado = Ler.ler_tudo()
        for i in range(len(resultado)):
            print(resultado[i])
        atividade = input('Informe a atividade que você quer deletar:\n')
        deletar(atividade)

    elif int(opcoes) == 4:
        opcao = input('''1 - Ver Tudo \n2 - A fazer \n3 - Fazendo \n4 - Feitos \ninforme: ''')
        
        if int(opcao) == 1:
            resultado = Ler.ler_tudo()
            for i in range(len(resultado)):
                print(resultado[i])
        
        elif int(opcao) == 2:
            resultado = Ler.ler_afazer()
            for i in range(len(resultado)):
                print(resultado[i])

        elif int(opcao) == 3:
            resultado = Ler.ler_Fazendo()
            for i in range(len(resultado)):
                print(resultado[i])

        if int(opcao) == 4:
            resultado = Ler.ler_feitos()
            for i in range(len(resultado)):
                print(resultado[i])


    elif int(opcoes) == 5:
        print('Encerrando...')
        break



#\
        

    