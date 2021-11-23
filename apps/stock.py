import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import load_model
import streamlit as st
import datetime
import yfinance as yf
import tensorflow as tf


def stock_pred():
    st.title("STOCK PREDICTION WEB APPLICATION")
    st.header('Here you can select the stock you want to predict')

    choose_stock = st.selectbox('Choose the stock', ['NONE', 'ITC', 'MRF','Tata Motors','Tata Power','Reliance','Airtel','BPCL'])
    if (choose_stock == 'ITC'):
        df1 = yf.download(tickers='ITC.NS',start_date='2021-01-01', end_date=datetime.date.today())
        #df1 = yf.download(tickers='USDINR=X',period ='5d', interval = '15m')
        df1['Date'] = df1.index
        st.header('Stock')
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
        X_test = np.reshape(X_test,(X_test.shape[0],1,X_test.shape[1],1))
        print(X_test.shape[0], X_test.shape[1])
        model = load_model('Models/Stock/ITC2.h5')
        pred_price = model.predict(X_test)
        pred_price = scaler.inverse_transform(pred_price)

        NextDay_Date = datetime.date.today() + datetime.timedelta(days=1)

        get_pred = st.button('Get the Forecast of ITC ')
        if get_pred:
            st.subheader("Predictions for the next upcoming day Close Price : " + str(NextDay_Date))
            st.markdown(pred_price)

        st.subheader("Close Price VS Date Interactive chart for analysis:")
        st.line_chart(df1['Close'])

        st.subheader("Line chart of Open and Close for analysis:")
        st.line_chart(df1[['Open', 'Close']])

        st.subheader("Line chart of High and Low for analysis:")
        st.line_chart(df1[['High', 'Low']])

    if (choose_stock == 'MRF'):
        df1 = yf.download(tickers='MRF.NS',start_date='2021-01-01', end_date=datetime.date.today())
        #df1 = yf.download(tickers='USDINR=X',period ='5d', interval = '15m')
        df1['Date'] = df1.index
        st.header('Stock')
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
        X_test = np.reshape(X_test,(X_test.shape[0],1,X_test.shape[1],1))
        print(X_test.shape[0], X_test.shape[1])
        model = load_model('Models/Stock/MRF.h5')
        pred_price = model.predict(X_test)
        pred_price = scaler.inverse_transform(pred_price)

        NextDay_Date = datetime.date.today() + datetime.timedelta(days=1)

        get_pred = st.button('Get the Forecast of MRF ')
        if get_pred:
            st.subheader("Predictions for the next upcoming day Close Price : " + str(NextDay_Date))
            st.markdown(pred_price)

        st.subheader("Close Price VS Date Interactive chart for analysis:")
        st.line_chart(df1['Close'])

        st.subheader("Line chart of Open and Close for analysis:")
        st.line_chart(df1[['Open', 'Close']])

        st.subheader("Line chart of High and Low for analysis:")
        st.line_chart(df1[['High', 'Low']])

    if (choose_stock == 'Tata Motors'):
        df1 = yf.download(tickers='TATAMOTORS.NS',start_date='2021-01-01', end_date=datetime.date.today())
        #df1 = yf.download(tickers='USDINR=X',period ='5d', interval = '15m')
        df1['Date'] = df1.index
        st.header('Stock')
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
        X_test = np.reshape(X_test,(X_test.shape[0],1,X_test.shape[1],1))
        print(X_test.shape[0], X_test.shape[1])
        model = load_model('Models/Stock/TataMotors.h5')
        pred_price = model.predict(X_test)
        pred_price = scaler.inverse_transform(pred_price)

        NextDay_Date = datetime.date.today() + datetime.timedelta(days=1)

        get_pred = st.button('Get the Forecast of Tata Motors ')
        if get_pred:
            st.subheader("Predictions for the next upcoming day Close Price : " + str(NextDay_Date))
            st.markdown(pred_price)

        st.subheader("Close Price VS Date Interactive chart for analysis:")
        st.line_chart(df1['Close'])

        st.subheader("Line chart of Open and Close for analysis:")
        st.line_chart(df1[['Open', 'Close']])

        st.subheader("Line chart of High and Low for analysis:")
        st.line_chart(df1[['High', 'Low']])

    if (choose_stock == 'Tata Power'):
        df1 = yf.download(tickers='TATAPOWER.NS',start_date='2021-01-01', end_date=datetime.date.today())
        #df1 = yf.download(tickers='USDINR=X',period ='5d', interval = '15m')
        df1['Date'] = df1.index
        st.header('Stock')
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
        X_test = np.reshape(X_test,(X_test.shape[0],1,X_test.shape[1],1))
        print(X_test.shape[0], X_test.shape[1])
        model = load_model('Models/Stock/TataPower.h5')
        pred_price = model.predict(X_test)
        pred_price = scaler.inverse_transform(pred_price)

        NextDay_Date = datetime.date.today() + datetime.timedelta(days=1)

        get_pred = st.button('Get the Forecast of Tata Power ')
        if get_pred:
            st.subheader("Predictions for the next upcoming day Close Price : " + str(NextDay_Date))
            st.markdown(pred_price)

        st.subheader("Close Price VS Date Interactive chart for analysis:")
        st.line_chart(df1['Close'])

        st.subheader("Line chart of Open and Close for analysis:")
        st.line_chart(df1[['Open', 'Close']])

        st.subheader("Line chart of High and Low for analysis:")
        st.line_chart(df1[['High', 'Low']])

    if (choose_stock == 'ONGC'):
        df1 = yf.download(tickers='ONGC.NS',start_date='2021-01-01', end_date=datetime.date.today())
        #df1 = yf.download(tickers='USDINR=X',period ='5d', interval = '15m')
        df1['Date'] = df1.index
        st.header('Stock')
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
        X_test = np.reshape(X_test,(X_test.shape[0],1,X_test.shape[1],1))
        print(X_test.shape[0], X_test.shape[1])
        model = load_model('Models/Stock/ONGC.h5')
        pred_price = model.predict(X_test)
        pred_price = scaler.inverse_transform(pred_price)

        NextDay_Date = datetime.date.today() + datetime.timedelta(days=1)

        get_pred = st.button('Get the Forecast of ONGC ')
        if get_pred:
            st.subheader("Predictions for the next upcoming day Close Price : " + str(NextDay_Date))
            st.markdown(pred_price)

        st.subheader("Close Price VS Date Interactive chart for analysis:")
        st.line_chart(df1['Close'])

        st.subheader("Line chart of Open and Close for analysis:")
        st.line_chart(df1[['Open', 'Close']])

        st.subheader("Line chart of High and Low for analysis:")
        st.line_chart(df1[['High', 'Low']])


  

    if (choose_stock == 'Reliance'):
        df1 = yf.download(tickers='Reliance.NS',start_date='2021-01-01', end_date=datetime.date.today())
        #df1 = yf.download(tickers='USDINR=X',period ='5d', interval = '15m')
        df1['Date'] = df1.index
        st.header('Stock')
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
        X_test = np.reshape(X_test,(X_test.shape[0],1,X_test.shape[1],1))
        print(X_test.shape[0], X_test.shape[1])
        model = load_model('Models/Stock/Reliance.h5')
        pred_price = model.predict(X_test)
        pred_price = scaler.inverse_transform(pred_price)

        NextDay_Date = datetime.date.today() + datetime.timedelta(days=1)

        get_pred = st.button('Get the Forecast of Reliance ')
        if get_pred:
            st.subheader("Predictions for the next upcoming day Close Price : " + str(NextDay_Date))
            st.markdown(pred_price)

        st.subheader("Close Price VS Date Interactive chart for analysis:")
        st.line_chart(df1['Close'])

        st.subheader("Line chart of Open and Close for analysis:")
        st.line_chart(df1[['Open', 'Close']])

        st.subheader("Line chart of High and Low for analysis:")
        st.line_chart(df1[['High', 'Low']])

    if (choose_stock == 'Airtel'):
        df1 = yf.download(tickers='BHARTIARTL.NS',start_date='2021-01-01', end_date=datetime.date.today())
        #df1 = yf.download(tickers='USDINR=X',period ='5d', interval = '15m')
        df1['Date'] = df1.index
        st.header('Stock')
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
        X_test = np.reshape(X_test,(X_test.shape[0],1,X_test.shape[1],1))
        print(X_test.shape[0], X_test.shape[1])
        model = load_model('Models/Stock/Airtel.h5')
        pred_price = model.predict(X_test)
        pred_price = scaler.inverse_transform(pred_price)

        NextDay_Date = datetime.date.today() + datetime.timedelta(days=1)

        get_pred = st.button('Get the Forecast of Airtel ')
        if get_pred:
            st.subheader("Predictions for the next upcoming day Close Price : " + str(NextDay_Date))
            st.markdown(pred_price)

        st.subheader("Close Price VS Date Interactive chart for analysis:")
        st.line_chart(df1['Close'])

        st.subheader("Line chart of Open and Close for analysis:")
        st.line_chart(df1[['Open', 'Close']])

        st.subheader("Line chart of High and Low for analysis:")
        st.line_chart(df1[['High', 'Low']])


    if (choose_stock == 'BPCL'):
        df1 = yf.download(tickers='BPCL.NS',start_date='2021-01-01', end_date=datetime.date.today())
        #df1 = yf.download(tickers='USDINR=X',period ='5d', interval = '15m')
        df1['Date'] = df1.index
        st.header('Stock')
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
        X_test = np.reshape(X_test,(X_test.shape[0],1,X_test.shape[1],1))
        print(X_test.shape[0], X_test.shape[1])
        model = load_model('Models/Stock/BPCL.h5')
        pred_price = model.predict(X_test)
        pred_price = scaler.inverse_transform(pred_price)

        NextDay_Date = datetime.date.today() + datetime.timedelta(days=1)

        get_pred = st.button('Get the Forecast of BPCL ')
        if get_pred:
            st.subheader("Predictions for the next upcoming day Close Price : " + str(NextDay_Date))
            st.markdown(pred_price)

        st.subheader("Close Price VS Date Interactive chart for analysis:")
        st.line_chart(df1['Close'])

        st.subheader("Line chart of Open and Close for analysis:")
        st.line_chart(df1[['Open', 'Close']])

        st.subheader("Line chart of High and Low for analysis:")
        st.line_chart(df1[['High', 'Low']])

#stock_pred()
