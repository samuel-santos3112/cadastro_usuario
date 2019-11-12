from flask import Flask, jsonify, redirect, render_template,url_for,request,flash,session
import controllers as control
from models import Usuario


app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdhasdugqutw1623ashbd'



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/criar_usuario' , methods = ['POST'])
def criar_usuario():
    try:
        data = request.json
        usuario = Usuario(nome = data['nome'], senha = data['senha'])
        control.criar(usuario)
        flash('Criado com sucesso')
        return jsonify({data['nome'] : " inserido com sucesso"})
    except Exception as e:
        return jsonify({'Erro ao inserir' : e})


@app.route('/autenticar', methods= ['POST'])
def autenticar():
    try:
        nome = request.form['nome']
        senha = request.form['senha']

        usuario = control.listar_por_nome(nome)
        if not usuario or usuario.senha != senha:
            flash('Usuario ou senha não cadastrados')
            return redirect(url_for('index'))
        else:
            session['usuario_logado'] = usuario.id
            return redirect('http://www.google.com.br')
            
    except Exception as e:
        print(e)
    

@app.route('/logout')
def logout():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        flash('Nenhum usuario logado')
        return redirect(url_for('index'))
    else:
        session['usuario_logado'] = None
        return redirect(url_for('index'))


@app.route('/stream')
def stream():
    if 'usuario_logado' not in session or session[' usuario_logado'] == None:
        flash('Faça login')
        return redirect(url_for('index'))
    else:
        return redirect('http://www.google.com.br')

#@app.route('/control')
#def control():
#    pass
    #return redirect('control')


#@app.route('capture')
#def capture():
    #return redirect(capture)
#    pass


app.run(debug=True)

# Para rodar a aplicação usando seu computador como servidor.
#app.run(host='seu endereço ipv4',debug=False)
