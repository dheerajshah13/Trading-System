import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import load_model
import streamlit as st
import datetime
import yfinance as yf
import tensorflow as tf

def commodity_pred():
    st.title("Global Commodity Price Prediction")
    st.header('Here you can select the currency you want to predict')

    choose_stock = st.selectbox('Choose the Commodity', ['NONE', 'Gold','Silver','Platinum',"Copper",'Crude Oil'])
    if (choose_stock == 'Gold'):
        df1 = yf.download(tickers='GC=F',start_date='2021-01-01', end_date=datetime.date.today())
        #df1 = yf.download(tickers='USDINR=X',period ='5d', interval = '15m')
        df1['Date'] = df1.index
        st.header('GOLD')
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
        model = load_model('/Users/dheeraj/PycharmProjects/CSFC/Models/Commodity/gold.h5')
        pred_price = model.predict(X_test)
        pred_price = scaler.inverse_transform(pred_price)

        NextDay_Date = datetime.date.today() + datetime.timedelta(days=1)

        get_pred = st.button('Get the Forecast of CRYPTO Gold ')
        if get_pred:
            st.subheader("Predictions for the next upcoming day Close Price : " + str(NextDay_Date))
            st.markdown(pred_price)

        st.subheader("Close Price VS Date Interactive chart for analysis:")
        st.line_chart(df1['Close'])

        st.subheader("Line chart of Open and Close for analysis:")
        st.line_chart(df1[['Open', 'Close']])

        st.subheader("Line chart of High and Low for analysis:")
        st.line_chart(df1[['High', 'Low']])

    if (choose_stock == 'Silver'):
        df1 = yf.download(tickers='SI=F',start_date='2021-01-01', end_date=datetime.date.today())
        #df1 = yf.download(tickers='USDINR=X',period ='5d', interval = '15m')
        df1['Date'] = df1.index
        st.header('Silver')
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
        model = load_model('/Users/dheeraj/PycharmProjects/CSFC/Models/Commodity/Silver.h5')
        pred_price = model.predict(X_test)
        pred_price = scaler.inverse_transform(pred_price)

        NextDay_Date = datetime.date.today() + datetime.timedelta(days=1)

        get_pred = st.button('Get the Forecast of Silver ')
        if get_pred:
            st.subheader("Predictions for the next upcoming day Close Price : " + str(NextDay_Date))
            st.markdown(pred_price)

        st.subheader("Close Price VS Date Interactive chart for analysis:")
        st.line_chart(df1['Close'])

        st.subheader("Line chart of Open and Close for analysis:")
        st.line_chart(df1[['Open', 'Close']])

        st.subheader("Line chart of High and Low for analysis:")
        st.line_chart(df1[['High', 'Low']])

    if (choose_stock == 'Platinum'):
        df1 = yf.download(tickers='PL=F',start_date='2021-01-01', end_date=datetime.date.today())
        #df1 = yf.download(tickers='USDINR=X',period ='5d', interval = '15m')
        df1['Date'] = df1.index
        st.header('Platinum')
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
        model = load_model('/Users/dheeraj/PycharmProjects/CSFC/Models/Commodity/Platinum.h5')
        pred_price = model.predict(X_test)
        pred_price = scaler.inverse_transform(pred_price)

        NextDay_Date = datetime.date.today() + datetime.timedelta(days=1)

        get_pred = st.button('Get the Forecast of Platinum ')
        if get_pred:
            st.subheader("Predictions for the next upcoming day Close Price : " + str(NextDay_Date))
            st.markdown(pred_price)

        st.subheader("Close Price VS Date Interactive chart for analysis:")
        st.line_chart(df1['Close'])

        st.subheader("Line chart of Open and Close for analysis:")
        st.line_chart(df1[['Open', 'Close']])

        st.subheader("Line chart of High and Low for analysis:")
        st.line_chart(df1[['High', 'Low']])

    if (choose_stock == 'Copper'):
        df1 = yf.download(tickers='HG=F',start_date='2021-01-01', end_date=datetime.date.today())
        #df1 = yf.download(tickers='USDINR=X',period ='5d', interval = '15m')
        df1['Date'] = df1.index
        st.header('Copper')
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
        model = load_model('/Users/dheeraj/PycharmProjects/CSFC/Models/Commodity/Copper.h5')
        pred_price = model.predict(X_test)
        pred_price = scaler.inverse_transform(pred_price)

        NextDay_Date = datetime.date.today() + datetime.timedelta(days=1)

        get_pred = st.button('Get the Forecast of Copper')
        if get_pred:
            st.subheader("Predictions for the next upcoming day Close Price : " + str(NextDay_Date))
            st.markdown(pred_price)

        st.subheader("Close Price VS Date Interactive chart for analysis:")
        st.line_chart(df1['Close'])

        st.subheader("Line chart of Open and Close for analysis:")
        st.line_chart(df1[['Open', 'Close']])

        st.subheader("Line chart of High and Low for analysis:")
        st.line_chart(df1[['High', 'Low']])

    if (choose_stock == 'Crude Oil'):
        df1 = yf.download(tickers='CL=F',start_date='2021-01-01', end_date=datetime.date.today())
        #df1 = yf.download(tickers='USDINR=X',period ='5d', interval = '15m')
        df1['Date'] = df1.index
        st.header('Crude Oil')
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
        model = load_model('/Users/dheeraj/PycharmProjects/CSFC/Models/Commodity/Crude_oil.h5')
        pred_price = model.predict(X_test)
        pred_price = scaler.inverse_transform(pred_price)

        NextDay_Date = datetime.date.today() + datetime.timedelta(days=1)

        get_pred = st.button('Get the Forecast of Crude Oil')
        if get_pred:
            st.subheader("Predictions for the next upcoming day Close Price : " + str(NextDay_Date))
            st.markdown(pred_price)

        st.subheader("Close Price VS Date Interactive chart for analysis:")
        st.line_chart(df1['Close'])

        st.subheader("Line chart of Open and Close for analysis:")
        st.line_chart(df1[['Open', 'Close']])

        st.subheader("Line chart of High and Low for analysis:")
        st.line_chart(df1[['High', 'Low']])

#commodity_pred()