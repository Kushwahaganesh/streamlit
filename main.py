import yfinance as yf
import streamlit as st
from PIL import Image
from urllib.request import urlopen


st.title("Cryptocurrency Daily Prices | ₿")
st.header("Main Dashboard")

Bitcoin = 'BTC-USD'
Ethereum = 'ETH-USD'
Ripple = 'XRP-USD'
BitcoinCash = "BCH-USD"

BTC_Data = yf.Ticker(Bitcoin)
ETH_Data = yf.Ticker(Ethereum)
XRP_Data = yf.Ticker(Ripple)
BCH_Data = yf.Ticker(BitcoinCash)



BTCHis = BTC_Data.history(period="max")
ETHHis = ETH_Data.history(period="max")
XRPHis = XRP_Data.history(period="max")
BCHHis = BCH_Data.history(period="max")

BTC = yf.download(Bitcoin, start="2021-11-19", end="2021-11-19")
ETH = yf.download(Ethereum, start="2021-11-19", end="2021-11-19")
XRP = yf.download(Ripple, start="2021-11-19", end="2021-11-19")
BCH = yf.download(BitcoinCash, start="2021-11-19", end="2021-11-19")


st.write("BITCOIN ($)")
imageBTC = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1.png'))
#Display image
st.image(imageBTC)
#Display dataframe
st.table(BTC)
#Display a chart
st.bar_chart(BTCHis.Close)


st.write("ETHERUM ($)")
imageETH = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png'))
#Display image
st.image(imageETH)
#Display dataframe
st.table(ETH)
#Display a chart
st.bar_chart(ETHHis.Close)


st.write("RIPPLE ($)")
imageXRP = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/52.png'))
#Display image
st.image(imageXRP)
#Display dataframe
st.table(XRP)
#Display a chart
st.bar_chart(XRPHis.Close)


st.write("BITCOIN CASH ($)")
imageBCH = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1831.png'))
#Display image
st.image(imageBCH)
#Display dataframe
st.table(BCH)
#Display a chart
st.bar_chart(BCHHis.Close)



