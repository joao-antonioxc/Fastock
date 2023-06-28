import pandas as pd
import streamlit as st
from db.firebase_db import consultar_db


st.title('Consulta de Peças')

get_dict_pecas = consultar_db('pecas')

col1, col2, col3 = st.columns(3)

with col1:
    lista_marca = []
    for peca in get_dict_pecas:
        if get_dict_pecas[peca]['marca'] not in lista_marca:
            lista_marca.append(get_dict_pecas[peca]['marca'])
    input_marca_filter = st.selectbox(
        'Marca',
        sorted(sorted(lista_marca)),
        key='marca_filter'
    )
    input_codigo_filter = st.text_input(
        'Código',
        key='codigo_filter'
    )

with col2:
    lista_carro = []
    for peca in get_dict_pecas:
        if get_dict_pecas[peca]['marca'] == st.session_state.marca_filter:
            if get_dict_pecas[peca]['carro'] not in lista_carro:
                lista_carro.append(get_dict_pecas[peca]['carro'])
    input_carro_filter = st.selectbox(
        'Carro',
        sorted(lista_carro),
        key='carro_filter'
    )
    input_peca_filter = st.text_input(
        'Peça',
        key='peca_filter'
    )

with col3:
    lista_ano = []
    for peca in get_dict_pecas:
        if get_dict_pecas[peca]['marca'] == st.session_state.marca_filter and get_dict_pecas[peca][
            'carro'] == st.session_state.carro_filter:
            lista_ano = (get_dict_pecas[peca]['ano'])
    input_ano_filter = st.selectbox(
        'Ano',
        sorted(lista_ano),
        key='ano_filter'
    )

st.divider()

df = pd.DataFrame(get_dict_pecas).transpose()
df['selected'] = False

df_filtrado = df[
    (df['marca'] == st.session_state.marca_filter)
    & (df['carro'] == st.session_state.carro_filter)
    # & (df['ano'].str.contains(st.session_state.ano_filter))
    & (df['codigo'].str.contains(st.session_state.codigo_filter))
    & (df['peca'].str.contains(st.session_state.peca_filter))
    # & (df['estado'] == st.session_state.estado_filter)
]

st.data_editor(
    data=df_filtrado,
    disabled=('codigo', 'peca', 'estado', 'descricao', 'ano'),
    use_container_width=True,
    hide_index=True,
    column_order=('selected', 'codigo', 'peca', 'estado', 'descricao', 'ano'),
    key='selected'
)

update_count = 0
update_index = ''

for k in st.session_state['selected']['edited_rows']:
    if st.session_state['selected']['edited_rows'][k]['selected'] == True:
        update_count += 1

update_button = False if update_count == 1 else True

def index():
    if 'index' not in st.session_state:
        st.session_state['index'] = ''
    for k in st.session_state['selected']['edited_rows']:
        if st.session_state['selected']['edited_rows'][k]['selected'] == True:
            st.session_state['index'] = df_filtrado.index[k]
    st.success('Index Salvo!')

st.divider()

col4, col5, col6 = st.columns(3)

with col4:
    st.button(
        'Alterar',
        use_container_width=True,
        disabled=update_button,
        on_click=index
    )

with col5:
    st.button(
        'Vender',
        use_container_width=True
    )

with col6:
    st.button(
        'Excluir',
        use_container_width=True
    )
