import streamlit as st
import utils as utl
from views import home, analysis

# st.set_page_config(layout="wide", page_title='Navbar sample')
# from home import page_bg_img

utl.inject_custom_css()
utl.navbar_component()

def navigation():
    route = utl.get_current_route()
    if route == "home":
        home.load_view()
    # elif route == "about":
    #     about.load_view()
    elif route == "analysis":
        analysis.load_view()
    elif route is None: # Changed from route == None to route is None
        home.load_view()
        
navigation()
