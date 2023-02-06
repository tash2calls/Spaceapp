import streamlit as st

st.set_page_config(
	"multipage app")

st.title("Main page")
st.sidebar.success("Select a page above")


#hide streamlit style
hide_st_style=  """
         <style>
         #MainMenu {visibility:hidden;}
         footer{visibility:hidden;}
         header{visibility:hidden;}
         </style
         """
st.markdown(hide_st_style,unsafe_allow_html=True)
