import yfinance as yf
import streamlit as st
from multipage import MultiApp
from apps import forex
from apps import stock
from apps import crypto, Commodity
import base64
from helper import *
#st.image("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.mpnvva.in%2FHome%2FUProfile%3FinstituteID%3D18&psig=AOvVaw1bvMjVTXeTOq9_BIKesNlt&ust=1637740837940000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCMiIwJmCrvQCFQAAAAAdAAAAABAD")
app = MultiApp()


st.set_page_config(
    page_title="Trading System",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded")

#set_png_as_page_bg('/Users/dheeraj/PycharmProjects/CSFC/bg/5591276.png')

display_app_header(main_txt='Forecasting Price of CSFC',
                   sub_txt='Clean, describe, visualise and Predict using AI models')

#st.title("""Forecasting Price of CSFC""")


st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #030303;">
  <a class="navbar-brand" href="" target="_blank">Trade Future</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link" href="https://www.reddit.com/r/CryptoCurrency/" target="_blank">Reddit</a>
      </li>  
      <li class="nav-item">
        <a class="nav-link" href="https://zerodha.com" target="_blank">Zerodha</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://wazirx.com" target="_blank">WazirX</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://nonfungible.com/blog" target="_blank">Non Fungible Token</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)


#st.sidebar.markdown("<p class='big-font'><font color='White'>Select the Market</font></p>", unsafe_allow_html=True)


# Add all your application here
st.sidebar.title(":floppy_disk: Dashboard")
app.add_app("Crypto",crypto.crypto_pred)
app.add_app("Stock", stock.stock_pred)
app.add_app("Forex", forex.forex_pred)
app.add_app("Commodity",Commodity.commodity_pred)
#app.add_app("Model", model.app)
# The main app
app.run()
