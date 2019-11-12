from models import Usuario
from conexao import Session

session = Session()


def criar(Usuario):
    try:   
        session.add(Usuario)
        session.commit()
        return Usuario
    except Exception as e:
        print(e)
    finally:
        session.close()

def listar_por_nome(nome):
    try:
        usuario = session.query(Usuario).filter(Usuario.nome == nome).first()
        return usuario
    except Exception as e:
        print(e)
    finally:
        session.close()

def atualizar(id,usuario):
    try:
        session.query(Usuario).filter(Usuario.id == id).update({
        Usuario.nome: usuario.nome,
        Usuario.senha: usuario.senha
        }, synchronize_session=False)
        session.commit()
    except Exception as e:
        print(e)
    finally:
        session.close()

def deletar(id):
    try:
        usuario = session.query(Usuario).get(id)
        session.delete(usuario)  
        session.commit()  
    except Exception as e:
        print(e)
    finally:
        session.close()

def listar():
    try:
        usuarios = session.query(Usuario).all()  
        return usuarios
    except Exception as e:
        print(e)
    finally:
        session.close()