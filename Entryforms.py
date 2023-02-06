import streamlit as st
import plotly.graph_objects as go
from pandas import *
from streamlit_option_menu import option_menu
import database as db
import database as rb1
import pickle
from pathlib import Path
import streamlit_authenticator as stauth

names=["Thabo Mbonani"," Wandisile Lavisa", "Mr Bye"]
usernames=["CoachT", "CoachLavi", "CoachBye"]

#authenticator.logout("Logout","sidebar")
page_title="Entry form"
page_icon=":heartbeat:"
layout="centered"

hide_st_style=  """
 <style>
 #MainMenu {visibility:hidden;}
 footer{visibility:hidden;}
 header{visibility:hidden;}
 label{visibility:hidden;}
 </style
 """
st.markdown(hide_st_style,unsafe_allow_html=True)






#st.set_page_config(page_title=page_title,page_icon= page_icon,layout=layout)
st.title(page_title+ " " + page_icon)
Details= ["Name","Surname","Grade","Date of birth"]
health_comp_list= ["Resting HR(bpm)","Blood pressure(mm/Hg)"]
Body_Comp_list=["Height(m)", "Body mass(kg)","Sum of 7 skinfolds(mm)","Postural alignment"]
Flexibility_List= ["Sit and reach(Cm)","Shoulder internal rotation","Shoulder external rotation","Modified Thomas test","Ankle dorsiflexion Lunge"]
Stability=["Plank","Stork stand"]
Cardio_vascular=["Bleep test"]
Pace=["Repeat sprint(m)"]
Sprint=["5,20,40m Sprint(m.s) "]
Strength=["1REPmax Bench press(Kg)","1Repmax Leg press(Kg)"]
Strength_endurance=["Push ups"]
Power=["Vetical jump(cm)"]
Agility=["Illinois(s)"]
Acceleration=["5,20,40m Sprint(m.s2)"]


#hide streamlit style



selected=option_menu(menu_title= "Main menu",options=["DATA ENTRY","DATA VISUALIZATION"],
icons=["pencil-fil","bar-chart-fil"],orientation= "horizontal")


Sport_list=["Rugby","Hockey","Football","Cricket","Athletics"]

age_group_list=["u14","u15","u16","2nd team","1st team"]


def get_all_profiles():
	items=db.fetch_all_profiles()
	profiles= [item["key"]for item in items]
	return profiles

def get_all_domain():
	items=db.fetchall_all_domain()
	domain= [item["key2"] for item in items]
	return domain


if selected == "DATA ENTRY": 
	with st.form("entry_form",clear_on_submit= True):
		col1,col2= st.columns(2)
		col1.selectbox("Select Age group:",age_group_list,key="Age group")
		col2.selectbox("Select Sport :",Sport_list,key="Sport")

		"..."
		with st.expander("Details"):
			for Detail in Details:
				st.text_input(f"{Detail}:",key=Detail)

		with st.expander("Health components"):
			for health_component_loop in health_comp_list:
				st.text_input(f"{health_component_loop}:",key=health_component_loop)


		with st.expander("Body composition"):
			for body_composition_loop in Body_Comp_list:
				st.text_input(f"{body_composition_loop}:",key=body_composition_loop)

		with st.expander("Flexibility"):
			for Flex_loop in Flexibility_List:
				st.text_input(f"{Flex_loop}:",key=Flex_loop)

		with st.expander("Stamina"):
			for cardio_loop in Cardio_vascular:
				st.text_input(f"{cardio_loop}:",key=cardio_loop)


		with st.expander("Balance"):
			for stable in Stability:
				st.text_input(f"{stable}:",key=stable)

		with st.expander("Pace"):
			for pce in Pace:
				st.text_input(f"{pce}:",key=pce)

		with st.expander("Sprint"):
			for Sprint_loop in Sprint:
				st.text_input(f"{Sprint_loop}:",key=Sprint_loop)

		with st.expander("Strength"):
			for strength_loop in Strength:
				st.text_input(f"{strength_loop}:",key=strength_loop)

		with st.expander("Strength endurance"):
			for endurance_loop in Strength_endurance:
				st.text_input(f"{endurance_loop}:",key=endurance_loop)

		with st.expander("Power"):
			for Power_loop in Power:
				st.text_input(f"{Power_loop}:",key=Power_loop)

		with st.expander("Agility"):
			for agility_loop in Agility:
				st.text_input(f"{agility_loop}:",key=agility_loop)

		with st.expander("Acceleration"):
			for Accel in Acceleration:
				st.text_input(f"{Accel}:",key=Accel)

		with st.expander("Comment"):
			Comment=st.text_area("",placeholder= "Enter a comment here...")

		"..."

		submitted=st.form_submit_button("Save Data")
	

	if submitted:
		global profile

		profile=str(st.session_state["Name"])+"_"+ str(st.session_state["Surname"])
		domain=str(st.session_state["Sport"])+"_"+ str(st.session_state["Age group"])

		Details={Detail:st.session_state[Detail] for Detail in Details}
		health_components={health_component_loop:st.session_state[health_component_loop] for health_component_loop in health_comp_list }
		Body_Composition={body_composition_loop:st.session_state[body_composition_loop] for body_composition_loop in Body_Comp_list}
		Flexibility={Flex_loop:st.session_state[Flex_loop] for Flex_loop in Flexibility_List}
		Cardio_vascular={cardio_loop:st.session_state[cardio_loop] for cardio_loop in Cardio_vascular}
		Stability={stable:st.session_state[stable] for stable in Stability}
		Sprint={Sprint_loop:st.session_state[Sprint_loop] for Sprint_loop in Sprint}
		Power={Power_loop:st.session_state[Power_loop] for Power_loop in Power}
		Agility={agility_loop:st.session_state[agility_loop] for agility_loop in Agility}
		Pace={pce:st.session_state[pce] for pce in Pace}
		Strength={strength_loop:st.session_state[strength_loop] for strength_loop in Strength}
		Strength_endurance={endurance_loop:st.session_state[endurance_loop] for endurance_loop in Strength_endurance}
		Acceleration={Accel:st.session_state[Accel] for Accel in Acceleration}

		db.insert_profile(profile,domain,Details,health_comp_list,Body_Composition,Flexibility,Cardio_vascular,Stability,Power,Strength,Strength_endurance,Sprint,Pace,Agility,Acceleration,Comment)

		#fetches data from entries and puts it in database
		if domain =="1st team_Rugby":
			db.insert_profile(profile,domain,Details,health_comp_list,Body_Composition,Flexibility,Cardio_vascular,Stability,Power,Strength,Strength_endurance,Sprint,Pace,Agility,Acceleration,Comment)





		Successful=st.success("Data saved!")

	














if selected == "DATA VISUALIZATION":
	st.header("SPACE DATA INTEPRETATION")
	with st.form("Saved profiles"):

		profiles= st.selectbox("Select Profile:",get_all_profiles(),key="profile")
		submitted =st.form_submit_button("Plot profile")
		
		if submitted:
			

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
			bleep19=["2/4","2/5","2/6","2/7","3/1","3/2","3/3","3/4","3/5","3/6"]
			bleep29=["3/7","3/8","4/1","4/2","4/3","4/4","4/5","4/6","4/7","4/8","5/1"]
			bleep39=["5/2","5/3","5/4","5/5","5/6","5/7","5/8","5/9","6/1","6/2","6/3","6/6","6/7","6/8","6/9"]
			bleep49=["7/1","7/2","7/3","7/4","7/5","7/6","7/7","7/8","7/9","7/10","8/1","8/2","8/3"]
			bleep59=["8/4","8/5","8/6","8/7","8/8","8/9","8/10","8/11","9/1","9/2","9/3","9/4","9/5","9/6","9/7","9/8","9/9"]
			bleep69=["9/10","9/11","10/1","10/2","10/3","10/4","10/5","10/6","10/7","10,8","10/9","10/10","10/11","10/11","11/1","11/2","11/3"]
			bleep79=["11/4","11/5","11/6","11/7","11/8","11/9","11/10","11/11","11/12","12/1","12/2","12/3","12/4","12/5","12/6","12/7"]
			bleep80=["12/8","12/9","12/10","12/11","12/12","13/1","13/2","13/3","13/4","13/5","13/6","13/7"]

			Bleeplist=[bleep9,bleep19,bleep29,bleep39,bleep49,bleep59,bleep69,bleep79]

			b10="10%"
			b20="19%"
			b30="29%"
			b40="39%"
			b50="49%"
			b60="59%"
			b70="69%"
			b80="79%"
			b100="80%"


			col1,col2,col3= st.columns(3)
			perc=(Cardio_vascular.get("Bleep test"))
			
			for bleep2 in bleep9:
				if perc==bleep2:
					column1=col1.metric("Stamina",b10, "2")
					column2=col2.metric("Bleep test",str(perc), "")
					column3=col3.metric("Norm","Very poor", "")
			for bleep2 in bleep19:
				if perc==bleep2:
					column1=col1.metric("Stamina",b20, "2")
					column2=col2.metric("Bleep test",str(perc), "")
					column3=col3.metric("Norm","Very poor ", "")
			for bleep2 in bleep29:
				if perc==bleep2:
					column1=col1.metric("Stamina",b30, "2")
					column2=col2.metric("Bleep test",str(perc), "")
					column3=col3.metric("Norm","Poor", "")
			for bleep2 in bleep39:
				if perc==bleep2:
					column1=col1.metric("Stamina",b40, "3")
					column2=col2.metric("Bleep test",str(perc), "")
					column3=col3.metric("Norm","Fair", "")
			for bleep2 in bleep49:
				if perc==bleep2:
					column1=col1.metric("Stamina",b50, "1")
					column2=col2.metric("Bleep test",str(perc), "")
					column3=col3.metric("Norm","Average", "")
			for bleep2 in bleep59:
				if perc==bleep2:
					column1=col1.metric("Stamina",b60, "1")
					column2=col2.metric("Bleep test",str(perc), "")
					column3=col3.metric("Norm","Good", "")
			for bleep2 in bleep69:
			    if perc==bleep2:
			    	column1=col1.metric("Stamina",b70, "1")
			    	column2=col2.metric("Bleep test",str(perc), "")
			    	column3=col3.metric("Norm","Very Good", "")
			for bleep2 in bleep79:
				if perc==bleep2:
					column1=col1.metric("Stamina",b80, "1")
					column2=col2.metric("Bleep test",str(perc), "")
					column3=col3.metric("Norm","Excellent", "")
			for bleep2 in Bleeplist:
				if perc== None:
					st.error("User bleep result missing")

			


			a1,a2,a3= st.columns(3)

			a1.metric("Flexibility","50", "0")

			a2.metric("","", "")
			a3.metric("","", "")

			b1,b2,b3= st.columns(3)


			b1.metric("Stability","40", "0")
			b2.metric("","", "")
			b3.metric("","", "")

			c1,c2,c3= st.columns(3)



			c1.metric("Sprint Speed","70", "0")
			c2.metric("","", "")
			c3.metric("","", "")

			d1,d2,d3= st.columns(3)


			d1.metric("Strength","50", "0")
			d2.metric("","", "")
			d3.metric("","", "")

			e1,e2,e3= st.columns(3)

			e1.metric("Power","40", "0")
			e2.metric("","", "")
			e3.metric("","", "")

			f1,f2,f3= st.columns(3)

			f1.metric("Agility","60", "0")
			f2.metric("","", "")
			f3.metric("","", "")

			g1,g2,g3= st.columns(3)


			g1.metric("Acceleration","70", "0")
			g2.metric("","", "")
			g3.metric("","", "")

			h1,h2,h3= st.columns(3)


			h1.metric("Strength_endurance","40", "0")
			h2.metric("","", "")
			h3.metric("","", "")

			i1,i2,i3= st.columns(3)


			i1.metric("Pace","79", "0")
			i2.metric("","", "")
			i3.metric("","", "")


			st.write("Be the best of the best")














				
					
					
					
					
					
					
					



			
				

				
				

				





				

				#col1=col1.metric("Stamina",, "0")
				#col2=col2.metric("Strength_endurance", "75%", "0")
				#col3=col3.metric("Strength", "9 mph", "-8%")
				#col4.metric("Power", "86%", "4%")


				#col3,col4,col5= st.columns(3)


				#col3.metric("Stamina", "75%", "0")

				#bleeplist=["1/1","1/2","1/3","1/4","1/5","1/6","1/7","2/1","2/2","2/3"]

				
				#bleeplist19=[2/4,2/5,2/6,2/7,3/1,3/2,3/3,3/4,3/5,3/6]
				

				#bleep29=[3/7,3/8,4/1,4/2,4/3,4/4,4/5,4/6,4/7,4/8,5/1]

				#bleep39=[5/2,5/3,5/4,5/5,5/6,5/7,5/8,5/9,6/1,6/2,6/3/6/6,6/7,6/8,6/9]
				#bleep49=[7/1,7/2,7/3,7/4,7/5,7/6,7/7,7/8,7/9,7/10,8/1,8/2,8/3]
				#bleep59=[8/4,8/5,8/6,8/7,8/8,8/9,8/10,8/11,9/1,9/2,9/3,9/4,9/5,9/6,9/7,9/8,9/9]
				#bleep69=[9/10,9/11,10/1,10/2,10/3,10/4,10/5,10/6,10/7,10,8/10/9,10/10,10/11,10/11,11/1,11/2,11/3]
				#bleep79=[11/4,11/5,11/6,11/8,11/9,11/10/,11/11,11/12,12/1,12/2,12/3,12/4,12/5,12/6,12/7]
				
				














