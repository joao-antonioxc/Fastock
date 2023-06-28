import requests
import streamlit as st
import json

link_firebase_db = 'https://fastok-db-default-rtdb.firebaseio.com/'

def consultar_db(local):
    req_get = requests.get(f'{link_firebase_db}/{local}/.json')
    get_dict = req_get.json()
    return get_dict


def cadastrar_peca(**peca):
    req_post = requests.post(f'{link_firebase_db}/pecas/.json', data=json.dumps(peca))
    st.success('Peça Cadastrada com Sucesso!')
    st.session_state.clear()


def consultar_peca(index):
    req_get = requests.get(f'{link_firebase_db}/pecas/{index}/.json')
    get_peca = req_get.json()
    return get_peca


def alterar_peca(**peca):
    index = peca['index']
    del peca['index']
    req_patch = requests.patch(f'{link_firebase_db}/pecas/{index}/.json', data=json.dumps(peca))
    print(req_patch)
    print(req_patch.text)
    st.success('Peça Alterada com Sucesso!')
    st.session_state.clear()
