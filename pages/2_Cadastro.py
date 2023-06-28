from db.firebase_db import consultar_db, cadastrar_peca
import streamlit as st
from datetime import date


get_dict_carros = consultar_db('veiculos')
if 'key' not in st.session_state:
    st.session_state.hoje = str(date.today())

st.title('Formulário de Cadastro')

input_marca = st.selectbox(
    'Qual a marca do veículo?',
    sorted(get_dict_carros.keys()),
    key='marca'
)
input_carro = st.selectbox(
    'Qual o nome do veículo?',
    sorted(get_dict_carros[st.session_state.marca]),
    key='carro'
)
input_modelo = st.text_input(
    'Qual o modelo do veículo?',
    placeholder='Insira qual o modelo especifico do veículo!',
    key='modelo'
)
lista_anos = []
for year in range(25):
    lista_anos.append(str(int(date.today().year)-year))
input_ano = st.multiselect(
    'Qual o ano do veículo?',
    options=reversed(sorted(lista_anos)),
    key='ano'
)
input_codigo = st.text_input(
    'Qual o código da peça?',
    placeholder='Insira todos os códigos que se aplica a peça!',
    key='codigo'
)
input_peca = st.text_input(
    'Qual a peça cadastrada?',
    placeholder='Insira o nome da peça cadastrada',
    key='peca'
)
input_estado = st.selectbox(
    'Qual a peça cadastrada?',
    ['Nova', 'Usada Boa', 'Usada Ruim'],
    key='estado'
)
input_descricao = st.text_area(
    'Qual a descrição da peça cadastrada?',
    placeholder='Insira a descrição da peça cadastrada',
    key='descricao'
)
input_locacao = st.text_input(
    'Qual a locação da peça?',
    placeholder='Insira a locação da peça!',
    key='locacao'
)
input_button = st.button(
    'Cadastrar',
    on_click=cadastrar_peca,
    kwargs=st.session_state
)
