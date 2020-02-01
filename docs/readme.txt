O projeto foi feito em Python 3.6.7.

# Crie um ambiente virtual pra não ter que instalar tudo na sua máquina, esses comandos são do linux porém
é possível utilizalos com o terminal do git (bash)

Esse é o comando pra criar o ambiente virtual com o python3, porém se ele disser que seu pc não tem virtualenv
instalado rode os comandos de baixo primeiro e depois roda esse primeiro.


virtualenv -p python3 env (Rode esse comando na pasta onde você vai criar o projeto)


sudo apt install virtualenv
sudo apt-get install python-virtualenv
sudo apt-get install software-properties-common
sudo apt-add-repository universe
sudo apt-get update
sudo apt-get install virtualenv

O banco de dados que estou usando é o postgresql, no windows para instalá-lo basta baixar o instalador
e fazer a instalação normal, em seguida abra o app pgAdmin4 e ele vai abrir uma pagina web com os teus bancos.
No projeto tem um backup do banco (backup.sql)
Lembre-se de mudar a configuração do banco de dados no arquivo conexao.py, lá tem a conexão que está na variável
engine, após a palavra postgres: é onde deve substituir sua senha. 

Exemplo se sua senha do banco for 123 a string do seu banco ficará assim.
engine = create_engine('postgresql://postgres:123@localhost:5432/cadastro')


Supondo que você agora tem o python3 instalado, o banco postgresql instalado e configurado
e tem um ambiente virtual instalado também, agora vamos rodar a aplicação.
Primeiro entre no seu ambiente virtual com o seguinte comando (também é linux, mas da pra usar no cmd do windows)
source env/bin/activate (você tem que estar na pasta onde o virtual env foi criado).
Após isso, use o comando pip install -r requirements.txt (são todas as dependencias usadas no projeto).
Agora vá até a pasta onde esta o arquivo run.py e dê o comando python run.py e ele vai aparecer uma mensagem
dizendo que a aplicação está rodando no endereço padrão (http://localhost:5000)







