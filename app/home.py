import streamlit as st
import random
from scripts import update_weights

machine_choice = {0: 'Орел', 1: 'Решка'}
st.title("Произнеси вслух слово орел или решка")

st.header("И нажми на кнопку получить предсказание")

start_pred = st.button("получить предсказание")

if 'clear_all' in st.session_state:
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

if 'first' not in st.session_state:
    st.session_state['machine_win_count'], st.session_state['human_win_count'] = 0, 0
    st.session_state['strategy'] = {"win": {"change": 0, "same": 0}, "loss": {"change": 0, "same": 0}}
    st.session_state['all_human_choice'] = []
    st.session_state['all_human_results'] = []
    st.session_state['prediction_num'] = random.randint(0,1)
    st.session_state['prediction'] = machine_choice[st.session_state['prediction_num']]
    st.session_state['first'] = True

if start_pred and st.session_state['machine_win_count'] < 30 and st.session_state['human_win_count']<30:
    if 'second' not in st.session_state:
        st.session_state['prediction_num'] = random.randint(0,1)
        st.session_state['prediction'] = machine_choice[st.session_state['prediction_num']]
        st.session_state['second'] = True
    else:
        prev_choice = st.session_state['all_human_choice'][-1]
        prev_res = st.session_state['all_human_results'][-1]
        if st.session_state['strategy'][prev_res]['same'] > st.session_state['strategy'][prev_res]['change']:
            st.session_state['prediction_num'] = prev_choice
        elif st.session_state['strategy'][prev_res]['same'] < st.session_state['strategy'][prev_res]['change']:
            st.session_state['prediction_num'] = int((prev_choice - 1) ** 2)
        else:
            st.session_state['prediction_num'] = random.randint(0,1)
        
        st.session_state['prediction'] = machine_choice[st.session_state['prediction_num']]
        
if start_pred or 'second' in st.session_state:
    st.subheader(st.session_state['prediction'])
    st.subheader("Я угадал?")

    col1, col2 = st.columns([.5, .5])
    with col1:
        machine_win = st.button("Да")
        if machine_win:
            st.session_state['machine_win_count'] += 1
            st.session_state['all_human_choice'].append(st.session_state['prediction_num'])
            st.session_state['all_human_results'].append('loss')
            st.session_state['first_guess']=True
            if len(st.session_state['all_human_results'])>1 and len(st.session_state['all_human_choice'])>1:
                st.session_state = update_weights(st.session_state)

    with col2:
        machine_lose = st.button("Нет")
        if machine_lose:
            st.session_state['human_win_count'] += 1
            st.session_state['all_human_choice'].append(int((st.session_state['prediction_num'] - 1) ** 2))
            st.session_state['all_human_results'].append('win')
            st.session_state['first_guess']=True
            if len(st.session_state['all_human_results'])>1 and len(st.session_state['all_human_choice'])>1:
                st.session_state = update_weights(st.session_state)

if 'first_guess' in st.session_state: 

    progress_machine = st.session_state['machine_win_count'] / 30
    progress_human = st.session_state['human_win_count'] / 30

    st.progress(progress_machine, text='машина')
    st.progress(progress_human, text='ты')

    if st.session_state['machine_win_count'] > 29 or st.session_state['human_win_count']>29:
        st.subheader("Игра завершена")
        
        if st.session_state['machine_win_count'] > st.session_state['human_win_count']:
            st.subheader("Победила машина")
        elif st.session_state['machine_win_count'] < st.session_state['human_win_count']:
            st.subheader("Поздравляю. Теперь проваливай отсюда")
        else:
            st.subheader("Ничья")
            
        clear = st.button("Начать заново")
        st.session_state['clear_all'] = True
    