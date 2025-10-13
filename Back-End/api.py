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
