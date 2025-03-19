import bcrypt

def gerar_senha_hash(senha):
    return bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verificar_senha(senha, hash_senha):
    return bcrypt.checkpw(senha.encode('utf-8'), hash_senha.encode('utf-8'))
