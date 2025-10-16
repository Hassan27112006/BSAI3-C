import streamlit as st
from logic import FizzBuzz


class manager:
    def __init__(self):
        self.fizzbuzz=FizzBuzz()
        if 'number' not in st.session_state:
            st.session_state.number=1
            st.session_state.score=0
            st.session_state.game_over=False
            st.session_state.history=[]

    def get_correct_value(self):
            return self.fizzbuzz.getvalue(st.session_state.number)



    def Reset(self):
        st.session_state.number=1
        st.session_state.score=0
        st.session_state.game_over=False
        st.session_state.history=[]
