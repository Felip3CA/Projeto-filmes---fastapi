import streamlit as st
import requests

#URL da API do FastAPI
API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Escolhi a Diversão", page_icon="🎭")

st.title("🎨 Gerenciador de Filmes")

#Menu lateral sidebar
menu = st.sidebar.radio("Menu", ["Catálogo"])

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

elif menu == "Adicionar Filme":
    st.subheader("➕ Adicionar Filme")
    titulo = st.text_input("Título do Filme")
    genero = st.text_input("Gênero")
    ano = st.number_input("Ano de Lançamento", min_value=1900, max_value=2100)
    avaliacao = st.number_input("Avaliação de (0 a 10)", min_value=0, max_value=10, step=1)
    if st.button("Salvar filme"):
     params = {"titulo": titulo, "genero": genero, "ano": ano, "avaliacao": avaliacao}
     response = requests.post(f"{API_URL}/filmes", params=params)
     if response.status_code == 200:
        st.success("Filme adicionado com sucesso!")
    else:
        st.error("Erro ao adicionar o filme")