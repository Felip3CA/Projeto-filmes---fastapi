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
