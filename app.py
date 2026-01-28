import streamlit as st
import yfinance as yf

# Configuração da página
st.set_page_config(
    page_title="Painel da B3",
    layout="wide"
)

st.header("**PAINEL DE PREÇO E DIVIDENDOS DA B3**")

# Input do usuário
ticker = st.text_input('Digite o ticker da ação', 'BBAS3')

# Pegando dados
empresa = yf.Ticker(f"{ticker}.SA")
tickerDF = empresa.history(
    start="2014-01-01",
    end="2025-12-31",
)

# Colunas de informação
col1, col2, col3 = st.columns(3)

# Usamos .get para evitar erro se a informação não existir na API
info = empresa.info

with col1:
    st.write(f"**Empresa:** {info.get('longName', 'Não encontrado')}")
with col2:
    st.write(f"**Setor:** {info.get('industry', 'Não encontrado')}")
with col3:
    preco = info.get('currentPrice')
    if preco:
        st.write(f"**Preço Atual:** R$ {preco:.2f}")
    else:
        st.write("**Preço Atual:** Não disponível")

# Gráficos
st.subheader("Histórico de Fechamento")
st.line_chart(tickerDF['Close'])

st.subheader("Histórico de Dividendos")
st.bar_chart(tickerDF['Dividends'])