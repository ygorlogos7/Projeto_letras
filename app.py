import requests
import streamlit as st

def buscar_letra(banda, musica):
    endpoint = f"https://api.lyrics.ovh/v1/{banda}/{musica}"
    response = requests.get(endpoint)
    letra = response.json()['lyrics'] if response.status_code == 200 else "Letra não encontrada."
    return letra

st.image("img/letras.png")
st.title("Letras de Musica")

banda = st.text_input("Digite o nome da banda: ", key="banda")
musica = st.text_input("Digite o nome da música: ", key="musica")
pesquisar = st.button("Pesquisar")

if pesquisar:
    letra = buscar_letra(banda, musica)
    if letra:
        st.success("Letra encontrada!")
        st.text_area("Letra da música:", letra, height=300)
    else:
        st.error("Letra não encontrada. Verifique o nome da banda e da música.")

