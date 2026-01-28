# 📊 Painel de Ações da B3

Este é um mini-projeto de análise de dados financeiros desenvolvido em Python. Ele utiliza a biblioteca **Streamlit** para criar um dashboard interativo que consulta dados reais da B3 (Bolsa de Valores do Brasil) através do **Yahoo Finance**.

## 🚀 Funcionalidades

-   **Busca por Ticker:** O usuário pode digitar o código de qualquer ação (ex: `BBAS3`, `PETR4`, `VALE3`).
-   **Dados Fundamentais:** Exibe o nome da empresa, setor de atuação e preço atual em tempo real.
-   **Histórico de Cotações:** Gráfico de linha interativo mostrando o fechamento das ações desde 2014.
-   **Histórico de Dividendos:** Gráfico de barras mostrando os pagamentos de proventos ao longo do tempo.

## 🛠️ Tecnologias Utilizadas

-   **Python 3.12+**
-   [Streamlit](https://streamlit.io/): Para a criação da interface web.
-   [yfinance](https://pypi.org/project/yfinance/): Para coleta de dados do mercado financeiro.

## 📦 Como Instalar e Rodar

Siga os passos abaixo para executar o projeto na sua máquina:

### 1. Pré-requisitos
Certifique-se de ter o Python instalado.

### 2. Instalação das Dependências
No terminal, dentro da pasta do projeto, execute o comando para instalar as bibliotecas listadas no `requirements.txt`:

```bash
pip install -r requirements.txt