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

BTC = yf.download(Bitcoin, start="2021-11-07", end="2021-11-09")
ETH = yf.download(Ethereum, start="2021-11-07", end="2021-11-09")
XRP = yf.download(Ripple, start="2021-11-07", end="2021-11-09")
BCH = yf.download(BitcoinCash, start="2021-11-07", end="2021-11-09")


st.write("BITCOIN ($)")
imageBTC = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1.png'))
st.image(imageBTC)
st.table(BTC)
st.bar_chart(BTCHis.Close)
st.line_chart(BTCHis.Close) 


st.write("ETHERUM ($)")
imageETH = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png'))
st.image(imageETH)
st.table(ETH)
st.bar_chart(ETHHis.Close)
st.line_chart(ETHHis.Close) 


st.write("RIPPLE ($)")
imageXRP = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/52.png'))
st.image(imageXRP)
st.table(XRP)
st.bar_chart(XRPHis.Close) 
st.line_chart(XRPHis.Close) 


st.write("BITCOIN CASH ($)")
imageBCH = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1831.png'))
st.image(imageBCH)
st.table(BCH)
st.bar_chart(BCHHis.Close)
st.line_chart(BCHHis.Close) 



