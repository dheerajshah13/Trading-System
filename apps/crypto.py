import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import load_model
import streamlit as st
import datetime
import yfinance as yf
import tensorflow as tf

def crypto_pred():
    st.title("Crypto-Currency Price Prediction")
    st.header('Here you can select the currency you want to predict')

    choose_stock = st.selectbox('Choose the CryptoCurrency', ['NONE', 'Bitcoin','Ethereum','Dogecoin','Cardano','Polkadot','Litecoin','Stellar'])
    if (choose_stock == 'Bitcoin'):
        df1 = yf.download(tickers='BTC-INR',start_date='2021-01-01', end_date=datetime.date.today())
        #df1 = yf.download(tickers='USDINR=X',period ='5d', interval = '15m')
        df1['Date'] = df1.index
        st.header('CRYPTO')
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
        model = load_model('/Users/dheeraj/PycharmProjects/CSFC/Models/Crypto/BTC.h5')
        pred_price = model.predict(X_test)
        pred_price = scaler.inverse_transform(pred_price)

        NextDay_Date = datetime.date.today() + datetime.timedelta(days=1)

        get_pred = st.button('Get the Forecast of CRYPTO (BTC/INR) ')
        if get_pred:
            st.subheader("Predictions for the next upcoming day Close Price : " + str(NextDay_Date))
            st.markdown(pred_price)

        st.subheader("Close Price VS Date Interactive chart for analysis:")
        st.line_chart(df1['Close'])

        st.subheader("Line chart of Open and Close for analysis:")
        st.line_chart(df1[['Open', 'Close']])

        st.subheader("Line chart of High and Low for analysis:")
        st.line_chart(df1[['High', 'Low']])


    if (choose_stock == 'Ethereum'):
        df1 = yf.download(tickers='ETH-INR',start_date='2021-01-01', end_date=datetime.date.today())
        #df1 = yf.download(tickers='USDINR=X',period ='5d', interval = '15m')
        df1['Date'] = df1.index
        st.header('CRYPTO')
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
        model = load_model('/Users/dheeraj/PycharmProjects/CSFC/Models/Crypto/ETH.h5')
        pred_price = model.predict(X_test)
        pred_price = scaler.inverse_transform(pred_price)

        NextDay_Date = datetime.date.today() + datetime.timedelta(days=1)

        get_pred = st.button('Get the Forecast of CRYPTO (ETH/INR) ')
        if get_pred:
            st.subheader("Predictions for the next upcoming day Close Price : " + str(NextDay_Date))
            st.markdown(pred_price)

        st.subheader("Close Price VS Date Interactive chart for analysis:")
        st.line_chart(df1['Close'])

        st.subheader("Line chart of Open and Close for analysis:")
        st.line_chart(df1[['Open', 'Close']])

        st.subheader("Line chart of High and Low for analysis:")
        st.line_chart(df1[['High', 'Low']])

    if (choose_stock == 'Dogecoin'):
        df1 = yf.download(tickers='DOGE-INR',start_date='2021-01-01', end_date=datetime.date.today())
        #df1 = yf.download(tickers='USDINR=X',period ='5d', interval = '15m')
        df1['Date'] = df1.index
        st.header('CRYPTO')
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
        model = load_model('/Users/dheeraj/PycharmProjects/CSFC/Models/Crypto/DOGE.h5')
        pred_price = model.predict(X_test)
        pred_price = scaler.inverse_transform(pred_price)

        NextDay_Date = datetime.date.today() + datetime.timedelta(days=1)

        get_pred = st.button('Get the Forecast of CRYPTO (DOGE/INR) ')
        if get_pred:
            st.subheader("Predictions for the next upcoming day Close Price : " + str(NextDay_Date))
            st.markdown(pred_price)

        st.subheader("Close Price VS Date Interactive chart for analysis:")
        st.line_chart(df1['Close'])

        st.subheader("Line chart of Open and Close for analysis:")
        st.line_chart(df1[['Open', 'Close']])

        st.subheader("Line chart of High and Low for analysis:")
        st.line_chart(df1[['High', 'Low']])

    if (choose_stock == 'Cardano'):
        df1 = yf.download(tickers='ADA-INR',start_date='2021-01-01', end_date=datetime.date.today())
        #df1 = yf.download(tickers='USDINR=X',period ='5d', interval = '15m')
        df1['Date'] = df1.index
        st.header('CRYPTO')
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
        model = load_model('/Users/dheeraj/PycharmProjects/CSFC/Models/Crypto/ADA.h5')
        pred_price = model.predict(X_test)
        pred_price = scaler.inverse_transform(pred_price)

        NextDay_Date = datetime.date.today() + datetime.timedelta(days=1)

        get_pred = st.button('Get the Forecast of CRYPTO (ADA/INR) ')
        if get_pred:
            st.subheader("Predictions for the next upcoming day Close Price : " + str(NextDay_Date))
            st.markdown(pred_price)

        st.subheader("Close Price VS Date Interactive chart for analysis:")
        st.line_chart(df1['Close'])

        st.subheader("Line chart of Open and Close for analysis:")
        st.line_chart(df1[['Open', 'Close']])

        st.subheader("Line chart of High and Low for analysis:")
        st.line_chart(df1[['High', 'Low']])

    if (choose_stock == 'Polkadot'):
        df1 = yf.download(tickers='DOT1-INR',start_date='2021-01-01', end_date=datetime.date.today())
        #df1 = yf.download(tickers='USDINR=X',period ='5d', interval = '15m')
        df1['Date'] = df1.index
        st.header('CRYPTO')
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
        model = load_model('/Users/dheeraj/PycharmProjects/CSFC/Models/Crypto/DOT.h5')
        pred_price = model.predict(X_test)
        pred_price = scaler.inverse_transform(pred_price)

        NextDay_Date = datetime.date.today() + datetime.timedelta(days=1)

        get_pred = st.button('Get the Forecast of CRYPTO (DOT1/INR) ')
        if get_pred:
            st.subheader("Predictions for the next upcoming day Close Price : " + str(NextDay_Date))
            st.markdown(pred_price)

        st.subheader("Close Price VS Date Interactive chart for analysis:")
        st.line_chart(df1['Close'])

        st.subheader("Line chart of Open and Close for analysis:")
        st.line_chart(df1[['Open', 'Close']])

        st.subheader("Line chart of High and Low for analysis:")
        st.line_chart(df1[['High', 'Low']])

    if (choose_stock == 'Litecoin'):
        df1 = yf.download(tickers='LTC-INR',start_date='2021-01-01', end_date=datetime.date.today())
        #df1 = yf.download(tickers='USDINR=X',period ='5d', interval = '15m')
        df1['Date'] = df1.index
        st.header('CRYPTO')
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
        model = load_model('/Users/dheeraj/PycharmProjects/CSFC/Models/Crypto/LTC.h5')
        pred_price = model.predict(X_test)
        pred_price = scaler.inverse_transform(pred_price)

        NextDay_Date = datetime.date.today() + datetime.timedelta(days=1)

        get_pred = st.button('Get the Forecast of CRYPTO (LTC/INR) ')
        if get_pred:
            st.subheader("Predictions for the next upcoming day Close Price : " + str(NextDay_Date))
            st.markdown(pred_price)

        st.subheader("Close Price VS Date Interactive chart for analysis:")
        st.line_chart(df1['Close'])

        st.subheader("Line chart of Open and Close for analysis:")
        st.line_chart(df1[['Open', 'Close']])

        st.subheader("Line chart of High and Low for analysis:")
        st.line_chart(df1[['High', 'Low']])

    if (choose_stock == 'Stellar'):
        df1 = yf.download(tickers='XLM-INR', start_date='2021-01-01', end_date=datetime.date.today())
        # df1 = yf.download(tickers='USDINR=X',period ='5d', interval = '15m')
        df1['Date'] = df1.index
        st.header('CRYPTO')
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
        model = load_model('/Users/dheeraj/PycharmProjects/CSFC/Models/Crypto/XLM.h5')
        pred_price = model.predict(X_test)
        pred_price = scaler.inverse_transform(pred_price)

        NextDay_Date = datetime.date.today() + datetime.timedelta(days=1)

        get_pred = st.button('Get the Forecast of CRYPTO (XLM/INR) ')
        if get_pred:
            st.subheader("Predictions for the next upcoming day Close Price : " + str(NextDay_Date))
            st.markdown(pred_price)

        st.subheader("Close Price VS Date Interactive chart for analysis:")
        st.line_chart(df1['Close'])

        st.subheader("Line chart of Open and Close for analysis:")
        st.line_chart(df1[['Open', 'Close']])

        st.subheader("Line chart of High and Low for analysis:")
        st.line_chart(df1[['High', 'Low']])


#crypto_pred()