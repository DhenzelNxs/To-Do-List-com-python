# To-Do-List-com-python
Uma Aplicação no modelo To-Do List feita por mim em python(É nescessário mys
ql para utilizá-la)

Instalação 

1- Instalar a biblioteca mysql.connector

pip install mysql.connector

usando mysql worckbech crie um banco de dado e em seguida uma tabela chamada "atividade"(pode ser qualquer variavel, mas terá que mudar no codigo depois)

Deve haver os seguintes campos

nome_ativ varchar(30),
status_ativ varchar(30));

É nescessário alterar a função criar_conexao de acordo com seu servidor

conexao= mysql.connector.connect(
host=""
user=""
password=""
database="")
