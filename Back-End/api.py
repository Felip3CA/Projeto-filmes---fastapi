from fastapi import FastAPI

import funcao

#Rodar FastAPI = python -m uvicorn api:app --reload

#Testar as rotas no fastapi
# /docs > Documentação Swagger
# /redoc > Documentação redoc

app = FastAPI(title= "Gerenciador de Filmes")

#GET > Pegar/Listar
#POST > Enviar/Cadastar
#PUT > Atualizar
#DELETE > Deletar

#API sempre retorna dados em JSON (Chave: Valor)
@app.get("/")
def home():
    return {"Mensagem":"Bom dia... quero café!!"}

@app.get("/escolhi_diversão")
def catalogo():
    filmes = funcao.listar_movies()
    lista = []
    for filme in filmes:
        lista.append({ "id": filme[0], "título": filme[1], "gênero": filme[2], "ano": filme[3], "avaliação": filme[4]})
    return {"filmes": lista}

@app.post("/filmes")
def adicionar_filme(titulo: str, genero: str, ano: int, avaliacao: float):
    funcao.criar_filme(titulo, genero, ano, avaliacao)
    return {"mensagem": "Filme adicionado com sucesso!"}

@app.put("/filmes/{id_filme}")
def atualizar_filme(id_filme:int,nova_avaliacao: float):
    filmes = funcao.listar_movies()
    if filmes:
        funcao.atualizar_movies(id_filme, nova_avaliacao)
        return{"mensagem": "Filme atualizado com sucesso!"}
    else:
        return{"erro":"Filme não encontrado"}
    
@app.delete("/filmes/{titulo}")
def deletar_filme(titulo):
    filmes = funcao.listar_movies()
    if filmes:
        funcao.deletar_filme(titulo)
        return{"mensagem": "Você deletou o filme com sucesso!"}
    else:
        return{"erro":"Filme não deletado"}

