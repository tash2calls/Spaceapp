import os
from deta import Deta
from dotenv import load_dotenv
import streamlit as st


load_dotenv("C:/Users/Thabo/pyproj/multiapp/dt.env.txt")

#DETA_KEY = os.getenv("DETA_KEY")


deta = Deta(st.secretes["DETA_KEY"])



db= deta.Base("SBHS")


def insert_profile(profile,domain,Details,health_componenents,Body_Composition,
	Flexibility,Cardio_vascular,Stability,Power,Strength,Strength_endurance,
	Sprint,Pace,Agility,Acceleration,Comment):

	return db.put({"key":profile,"key2":domain,
		"Details":Details,
		"health_comp_list":health_componenents,
		"Body_Comp_list":Body_Composition,
		"Flexibility_List":Flexibility,
		"Stability" :Stability,
		"Cardio_vascular":Cardio_vascular,
		"Pace":Pace,
		"Sprint":Sprint,
		"Strength":Strength,
		"Strength_endurance":Strength_endurance,
		"Power":Power,
		"Agility":Agility,
		"Acceleration":Acceleration,
		"Comment" :Comment
		})


def fetch_all_profiles():
	fetch= db.fetch()
	return fetch.items


def get_profile(profile):
	return db.get(profile)



def get_domain(domain):
	return db.get(domain)
