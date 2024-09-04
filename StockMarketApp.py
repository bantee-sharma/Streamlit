import streamlit as st
import datetime
import yfinance as yf 

ticker_symbol = st.text_input("Enter the Stock name","AAPL")



col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input("Start date",value=datetime.date(2019,7,6))

with col2:
    end_date = st.date_input("End date",value=datetime.date(2020,7,6))


data = yf.download(ticker_symbol,start=start_date,end=end_date)


st.write(data)

st.line_chart(data["Close"])

st.bar_chart(data["Volume"])