import pickle
from pathlib import Path
import streamlit_authenticator as stauth

names=["Thabo Mbonani"," Wandisile Lavisa", "Mr Bye"]
username=["CoachT", "CoachLavi", "CoachBye"]
passwords= ["abc123","def456","ghi789"]


hashed_passwords= stauth.Hasher(passwords).generate()

file_path= Path(__file__).parent/ "C:/users/Thabo/pyproj/Multiapp/hashed_pw.pkl.txt"
with file_path.open("wb") as file:
	pickle.dump(hashed_passwords,file)

