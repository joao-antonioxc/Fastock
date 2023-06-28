from db.firebase_db import consultar_db, consultar_peca, alterar_peca
import streamlit as st
from datetime import date


get_dict_carros = consultar_db('veiculos')
get_peca = consultar_peca(st.session_state['index'])

if 'key' not in st.session_state:
    st.session_state.atualizacao = str(date.today())

st.title('Alterar Cadastro')

input_alter_marca = st.selectbox(
    'Qual a marca do veículo?',
    sorted(get_dict_carros.keys()),
    index=sorted(get_dict_carros.keys()).index(get_peca['marca']),
    key='marca'
)

if get_peca['marca'] == st.session_state['marca']:
    index_carro = sorted(get_dict_carros[st.session_state.marca]).index(get_peca['carro'])
else:
    index_carro = 0

input_alter_carro = st.selectbox(
    'Qual o nome do veículo?',
    sorted(get_dict_carros[st.session_state.marca]),
    index=index_carro,
    key='carro'
)

input_alter_modelo = st.text_input(
    'Qual o modelo do veículo?',
    value=get_peca['modelo'],
    placeholder='Insira qual o modelo especifico do veículo!',
    key='modelo'
)

lista_anos = []

for year in range(25):
    lista_anos.append(str(int(date.today().year)-year))

lista_default = []

for item in get_peca['ano']:
    if item in lista_anos:
        lista_default.append(item)

input_alter_ano = st.multiselect(
    'Qual o ano do veículo?',
    default=reversed(sorted(lista_default)),
    options=sorted(lista_anos),
    key='ano'
)

input_alter_codigo = st.text_input(
    'Qual o código da peça?',
    value=get_peca['codigo'],
    placeholder='Insira todos os códigos que se aplica a peça!',
    key='codigo'
)

input_alter_peca = st.text_input(
    'Qual a peça cadastrada?',
    value=get_peca['peca'],
    placeholder='Insira o nome da peça cadastrada',
    key='peca'
)

input_alter_estado = st.selectbox(
    'Qual a peça cadastrada?',
    ['Nova', 'Usada Boa', 'Usada Ruim'],
    index=['Nova', 'Usada Boa', 'Usada Ruim'].index(get_peca['estado']),
    key='estado'
)

input_alter_descricao = st.text_area(
    'Qual a descrição da peça cadastrada?',
    value=get_peca['descricao'],
    placeholder='Insira a descrição da peça cadastrada',
    key='descricao'
)

input_alter_locacao = st.text_input(
    'Qual a locação da peça?',
    value=get_peca['locacao'],
    placeholder='Insira a locação da peça!',
    key='locacao'
)

input_button = st.button(
    'Alterar',
    on_click=alterar_peca,
    kwargs=st.session_state
)
