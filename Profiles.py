import streamlit as st
import database as db

#st.set_page_config(
	##page_icon=";)"
#)

#hide streamlit style
hide_st_style=  """
         <style>
         #MainMenu {visibility:hidden;}
         footer{visibility:hidden;}
         header{visibility:hidden;}
         </style
         """
st.markdown(hide_st_style,unsafe_allow_html=True)



st.title(" Search Player Profiles")



Sport_list=["Rugby","Hockey","Football","Cricket","Athletics","All"]


age_group_list=["u14","u15","u16","2nd team","1st team","All"]

Details= ["Name","Surname","Grade","Date of birth"]

Search_List=[">10",">20",">40",">50",">60",">70",">80",">90"]

Attributes=[
"Flexability",
"Balance",
"Stamina",
"Speed",
"Strength",
"speed_endurance",
"Power",
"Acceleration",
"Agility",
"Pace"]

with st.form("entry_form",clear_on_submit= True):
	col1,col2= st.columns(2)

	col1.selectbox("Select Age group:",age_group_list,key="Age group")
	col2.selectbox("Select Sport :",Sport_list,key="Sport")

	with st.expander("Details"):
		for Detail in Details:
			st.text_input(f"{Detail}:",key=Detail)

	with st.expander("Attributes"):
		for Attribute in Attributes:
			st.number_input(f"{Attribute}:",step=10,key=Attribute)

	Submit= st.form_submit_button("Search")

	if Submit:
		profile=str(st.session_state["Name"])+"_"+ str(st.session_state["Surname"])
		domain=str(st.session_state["Sport"])+"_"+ str(st.session_state["Age group"])

		profile_data=db.get_profile(st.session_state["profile"])

		Details=profile_data.get("Details")
		health_components=profile_data.get("health_comp_list")
		Body_Comp_list=profile_data.get("Body_Comp_list")
		Flexibility_List=profile_data.get("Flexibility_List")
		Stability=profile_data.get("Stability")
		Cardio_vascular=profile_data.get("Cardio_vascular")
		Pace=profile_data.get("Pace")
		Sprint=profile_data.get("Sprint")
		Strength=profile_data.get("Strength")
		Strength_endurance=profile_data.get("Strength_endurance")
		Power=profile_data.get("Power")
		Agility=profile_data.get("Agility")
		Acceleration=profile_data.get("Acceleration")
		Comment=profile_data.get("Comment")


		


			
		with open('C:/users/Thabo/pyproj/multiapp/style.css') as f:
			st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
				

			bleep9=["1/1","1/2","1/3","1/4","1/5","1/6","1/7""2/1","2/2","2/3 "]
			bleeplist19=["2/4","2/5","2/6","2/7","3/1","3/2","3/3","3/4","3/5","3/6"]
			bleep29=["3/7","3/8","4/1","4/2","4/3","4/4","4/5","4/6","4/7","4/8","5/1"]
			bleep39=["5/2","5/3","5/4","5/5","5/6","5/7","5/8","5/9","6/1","6/2","6/3","6/6","6/7","6/8","6/9"]
			bleep49=["7/1","7/2","7/3","7/4","7/5","7/6","7/7","7/8","7/9","7/10","8/1","8/2","8/3"]
			bleep59=["8/4","8/5","8/6","8/7","8/8","8/9","8/10","8/11","9/1","9/2","9/3","9/4","9/5","9/6","9/7","9/8","9/9"]
			bleep69=["9/10","9/11","10/1","10/2","10/3","10/4","10/5","10/6","10/7","10,8","10/9","10/10","10/11","10/11","11/1","11/2","11/3"]
			bleep79=["11/4","11/5","11/6","11/7","11/8","11/9","11/10","11/11","11/12","12/1","12/2","12/3","12/4","12/5","12/6","12/7"]
			bleep80=[]

			Bleepist[bleep9,bleep19,bleep29,bleep39,bleep49,bleep59,bleep69,bleep79,bleep80]

			



			col1,col2,col3= st.columns(3)
			perc=(Cardio_vascular.get("Bleep test"))


