import streamlit as st
import requests

#URL da API do FastAPI
API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Escolhi a Diversão", page_icon="🎭")

st.title("🎨 Gerenciador de Filmes")

#Menu lateral sidebar
menu = st.sidebar.radio("Menu", ["Catálogo","Adicionar Filme", "Atualizar Filme"])

if menu == "Catálogo":
    st.subheader("Todos os filmes 🎬")
    response = requests.get(f"{API_URL}/escolhi_diversão")
    if response.status_code == 200:
        filmes = response.json().get("filmes",[])
        if filmes:
            for filme in filmes:
                st.write(f"{filme['título']} ( {filme['ano']})  -  {filme['gênero']}  -  🔍 {filme['avaliação']}")
        else:
            st.info("Nenhum filme encontrado")
    else:
       st.error("Erro ao conectar com a API")

elif menu == "Adicionar filme":
    st.subheader("Adicionar Filme ao catálogo")
    titulo = st.text_input("Título do filme")
    genero = st.text_input("Gênero")
    ano = st.number_input("Ano de lançamento", min_value=0, max_value=10)
    avaliacao = st.number_input("Avaliação (0 à 10)", min_value=0.0, max_value=10.0, step=1)

    if st.button("Salvar"):
        params = {"titulo": titulo,
                  "genero": genero,
                  "ano": ano,
                  "avaliacao": avaliacao}
        response = requests.post(f"{API_URL}/filmes",params=params)
        if response.status_code == 200:
            st.success("FIlme adicionado com sucesso")
        else:
            st.error("Erro ao adicionar o filme")

elif menu == "Atualizar Filme":
    st.subheader("Atualizar Filme")
    id_filme = st.number_input("ID do filme a atualizar", min_value=1, step=1)
    nova_avaliacao = st.number_input("Nova avaliação", min_value=0.0, max_value=10.0, step=0.1)
    if st.button("Atualizar"):
        dados = {"nova_avaliacao":nova_avaliacao}
        response = requests.put(f"{API_URL}/filmes{id_filme}", params=dados)
        if response.status_code == 200:
            data = response.json()
            if "erro" in data:
                st.warning(data["erro"])
            else:
                st.success("Filme atualizado com sucesso!")
        else:
            st.error("Erro no seu código... lascado")