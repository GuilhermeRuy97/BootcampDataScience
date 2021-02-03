import streamlit as st
import pandas as pd

#Para rodar o código: streamlit run src/app_streamlit.py

def carrega_dados(caminho):
    dados = pd.read_csv(caminho)
    return dados

def main():

    st.title("Minha primeira aplicação :D")

    obitos_2019 = carrega_dados("dados\obitos-2019.csv")

    st.dataframe(obitos_2019)
    st.text("Minha aplicação")

if __name__ == "__main__":
    main()