import json
import streamlit as st
import pandas as pd
import base64
import streamlit.components.v1 as components
from PIL import Image
import pandas as pd

def display_app_header(main_txt,sub_txt,is_sidebar = False):
    """
    function to display major headers at user interface
    ----------
    main_txt: str -> the major text to be displayed
    sub_txt: str -> the minor text to be displayed
    is_sidebar: bool -> check if its side panel or major panel
    """

    html_temp = f"""
    <h1 style = "color:#DFB722; text_align:center; font-weight: bold;"> {main_txt} </h1>
    <p style = "color:#FFFFFF; text_align:center;"> {sub_txt} </p>
    </div>
    """
    if is_sidebar:
        st.sidebar.markdown(html_temp, unsafe_allow_html = True)
    else:
        st.markdown(html_temp, unsafe_allow_html = True)
