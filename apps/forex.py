import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import load_model
import streamlit as st
import datetime
import yfinance as yf
import tensorflow as tf


def forex_pred():
    st.title("FOREX PREDICTION WEB APPLICATION")
    st.header('Here you can select the currency you want to predict')

    choose_stock = st.selectbox('Choose the Forex', ['NONE', 'USD-INR', 'EUR-INR', 'CAD-INR'])
    if (choose_stock == 'USD-INR'):
        df1 = yf.download(tickers='USDINR=X',start_date='2021-01-01', end_date=datetime.date.today())
        #df1 = yf.download(tickers='USDINR=X',period ='5d', interval = '15m')
        df1['Date'] = df1.index
        st.header('FOREX')
        if st.checkbox('Show Raw Data'):
            st.subheader("Wanna See Raw Data")
            st.dataframe(df1.tail())

        new_df = df1.filter(['Close'])
        scaler = MinMaxScaler(feature_range=(0, 1))

        last_30_days = new_df[-100:].values
        last_30_days_scaled = scaler.fit_transform(last_30_days)
        X_test = []
        X_test.append(last_30_days_scaled)
        X_test = np.array(X_test)
        X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
        model = load_model('Models/Forex/USD-INR.h5')
        pred_price = model.predict(X_test)
        pred_price = scaler.inverse_transform(pred_price)

        NextDay_Date = datetime.date.today() + datetime.timedelta(days=1)

        get_pred = st.button('Get the Forecast of Forex (USD/INR) ')
        if get_pred:
            st.subheader("Predictions for the next upcoming day Close Price : " + str(NextDay_Date))
            st.markdown(pred_price)

        st.subheader("Close Price VS Date Interactive chart for analysis:")
        st.line_chart(df1['Close'])

        st.subheader("Line chart of Open and Close for analysis:")
        st.line_chart(df1[['Open', 'Close']])

        st.subheader("Line chart of High and Low for analysis:")
        st.line_chart(df1[['High', 'Low']])
    if (choose_stock == 'EUR-INR'):
        df1 = yf.download(tickers='EURINR=X',start_date='2021-01-01', end_date=datetime.date.today())
        #df1 = yf.download(tickers='USDINR=X',period ='5d', interval = '15m')
        df1['Date'] = df1.index
        st.header('FOREX')
        if st.checkbox('Show Raw Data'):
            st.subheader("Wanna See Raw Data")
            st.dataframe(df1.tail())

        new_df = df1.filter(['Close'])
        scaler = MinMaxScaler(feature_range=(0, 1))

        last_30_days = new_df[-100:].values
        last_30_days_scaled = scaler.fit_transform(last_30_days)
        X_test = []
        X_test.append(last_30_days_scaled)
        X_test = np.array(X_test)
        X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
        model = load_model('Models/Forex/EUR-INR.h5')
        pred_price = model.predict(X_test)
        pred_price = scaler.inverse_transform(pred_price)

        NextDay_Date = datetime.date.today() + datetime.timedelta(days=1)

        get_pred = st.button('Get the Forecast of Forex (EUR/INR) ')
        if get_pred:
            st.subheader("Predictions for the next upcoming day Close Price : " + str(NextDay_Date))
            st.markdown(pred_price)

        st.subheader("Close Price VS Date Interactive chart for analysis:")
        st.line_chart(df1['Close'])

        st.subheader("Line chart of Open and Close for analysis:")
        st.line_chart(df1[['Open', 'Close']])

        st.subheader("Line chart of High and Low for analysis:")
        st.line_chart(df1[['High', 'Low']])
    if (choose_stock == 'CAD-INR'):
        df1 = yf.download(tickers='CADINR=X',start_date='2021-01-01', end_date=datetime.date.today())
        #df1 = yf.download(tickers='USDINR=X',period ='5d', interval = '15m')
        df1['Date'] = df1.index
        st.header('FOREX')
        if st.checkbox('Show Raw Data'):
            st.subheader("Wanna See Raw Data")
            st.dataframe(df1.tail())

        new_df = df1.filter(['Close'])
        scaler = MinMaxScaler(feature_range=(0, 1))

        last_30_days = new_df[-100:].values
        last_30_days_scaled = scaler.fit_transform(last_30_days)
        X_test = []
        X_test.append(last_30_days_scaled)
        X_test = np.array(X_test)
        X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
        model = load_model('Models/Forex/CAD-INR.h5')
        pred_price = model.predict(X_test)
        pred_price = scaler.inverse_transform(pred_price)

        NextDay_Date = datetime.date.today() + datetime.timedelta(days=1)

        get_pred = st.button('Get the Forecast of Forex (CAD/INR) ')
        if get_pred:
            st.subheader("Predictions for the next upcoming day Close Price : " + str(NextDay_Date))
            st.markdown(pred_price)

        st.subheader("Close Price VS Date Interactive chart for analysis:")
        st.line_chart(df1['Close'])

        st.subheader("Line chart of Open and Close for analysis:")
        st.line_chart(df1[['Open', 'Close']])

        st.subheader("Line chart of High and Low for analysis:")
        st.line_chart(df1[['High', 'Low']])
#forex_pred()
