Projeto desenvolvido na linguagem Python na versão 3.6.7.

#Crie um ambiente virtual pra não ter que instalar tudo na sua máquina, esses comandos são do linux porém é possível utilizalos com outros terminais como o git bash.

Esse é o comando pra criar o ambiente virtual com o python 3, porém se ao rodar o comando for exibida uma mensagem informando que seu computador não tem virtualenv instalado, rode os comandos de baixo primeiro e depois rode o primeiro.


virtualenv -p python3 env (Rode esse comando na pasta onde você vai criar o projeto).


sudo apt install virtualenv
sudo apt-get install python-virtualenv
sudo apt-get install software-properties-common
sudo apt-add-repository universe
sudo apt-get update
sudo apt-get install virtualenv

O banco de dados que foi utilizado é o PostgreSQL, no windows para instalá-lo basta baixar o instalador e realizar a instalação normal, em seguida abra o app pgAdmin4 e ele vai abrir uma pagina web com os teus bancos, ou se preferir pode se instalar algum client, sugiro o Dbeaver, é um ótimo cliente e ferramenta de administração de BD.

Lembre-se de mudar a configuração do banco de dados no arquivo conexao.py, a variável engine contém dados como o nome do banco, nome de usuario e também senha.

engine = create_engine('postgresql://usuario:senha@host:porta/nome_base')


Supondo que você agora tem o python3 instalado, o banco postgresql instalado e configuradoe tem um ambiente virtual instalado também, agora rode a aplicação.
Primeiro vá até onde está instalado seu ambiente virtual, lá utilize o comando source env/bin/activate (você tem que estar na pasta onde o virtual env foi criado).
Após isso, use o comando pip install -r requirements.txt, serão instaladas todas as dependências e suas respectivas versões, se estiver utilizando o ambiente virtual será instalado somente nele e não global. Para verificar se foram instaladas utilize o comando pip freeze.
Com as dependências instaladas navegue até pasta onde esta o arquivo run.py e execete o comando python run.py o servidor será inicializado se não houver nenhum erro e retornará uma mensagem informando o endereço em que a sua aplicação está rodando, esse é o endereço padrão (http://localhost:5000).







