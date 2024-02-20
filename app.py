import streamlit as st
from multiapp import MultiApp
from apps import home, numerology

app = MultiApp() 

app.add_app("Home", home.app)
app.add_app("numerology", numerology.app) 

app.run()