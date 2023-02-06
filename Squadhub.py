import streamlit as st
import sqlite3
from tkinter import *


###page_icon=";)"
#)


st.title("Squad hub")
st.sidebar.success("Select a page above")


Sport_list=["Rugby","Hockey","Football","Cricket","Athletics"]

age_group_list=["u14","u15","u16","2nd team","1st team"]

with st.form("entry_form",clear_on_submit= True):
	col1,col2= st.columns(2)
	col1.selectbox("Select Age group:",age_group_list,key="Age group")
	col2.selectbox("Select Sport :",Sport_list,key="Sport")

	Submit= st.form_submit_button("Submit")


