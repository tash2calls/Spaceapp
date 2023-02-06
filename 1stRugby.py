import os
from deta import Deta
from dotenv import load_dotenv
import streamlit as st


#load_dotenv("C:/Users/Thabo/pyproj/multiapp/.env")

hide="a0z8sv3g_Nqm1ASz4bKttx5EGX6zcChnuMXpCH8p8"

DETA_KEY = hide

deta = Deta(DETA_KEY)



rb1= deta.Base("1st_rugby")


def insert_profile(profile,domain,Details,health_componenents,Body_Composition,
	Flexibility,Cardio_vascular,Stability,Power,Strength,Strength_endurance,
	Sprint,Pace,Agility,Acceleration,Comment):

	return rb1.put({"key":profile,"key2":domain,
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
	fetch= rb1.fetch()
	return fetch.items


def get_profile(profile):
	return rb1.get(profile)



def get_domain(domain):
	return rb1.get(domain)

