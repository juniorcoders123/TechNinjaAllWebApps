import streamlit as st
from datetime import date
import yfinance as yf
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go

def app():
	import streamlit as st
	from datetime import date
	import yfinance as yf
	from plotly import graph_objs as go
	import pandas_datareader as data
	from fbprophet import Prophet
	from fbprophet.plot import plot_plotly
	import matplotlib.pyplot as plt

	start = "2010-01-01"
	end = date.today().strftime("%Y-%m-%d")
	st.header('Junior Coders Stock Forecast App')
	user_input = st.text_input('ENTER STOCK TICKER OR SYMBOL', 'AAPL')
	n_years = st.slider('Years of prediction:', 1, 20)
	period = n_years * 365
	df = data.DataReader(user_input, 'yahoo', start, end)
	df = df.reset_index()
	st.subheader("Data from 2010 to Present")
	st.write(df.describe())
	st.subheader("Closing Price vs Time Chart")
	fig = plt.figure(figsize=(12, 6))
	plt.plot(df.Close)
	st.pyplot(fig)
	# 50ma and 100ma
	st.subheader("Closing Price vs Time Chart with 50 and 100 Day MA")
	ma50 = df.Close.rolling(50).mean()
	ma100 = df.Close.rolling(100).mean()
	fig = plt.figure(figsize=(12, 6))
	plt.plot(ma50)
	plt.plot(ma100)
	plt.plot(df.Close)
	st.pyplot(fig)
	# 21wma and 200ma
	st.subheader("Closing Price vs Time Chart with 21 Week and 200 Day MA")
	wma21 = df.Close.rolling(21 * 7).mean()
	ma200 = df.Close.rolling(200).mean()
	fig = plt.figure(figsize=(12, 6))
	plt.plot(wma21)
	plt.plot(ma200)
	plt.plot(df.Close)
	st.pyplot(fig)

	# Different predicting for prophet

	# Plot raw data
	def plot_raw_data():
		fig = go.Figure()
		fig.add_trace(go.Scatter(x=df['Date'], y=df['Open'], name="stock_open"))
		fig.add_trace(go.Scatter(x=df['Date'], y=df['Close'], name="stock_close"))
		fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
		st.plotly_chart(fig)

	plot_raw_data()

	# Predict forecast with Prophet.
	df_train = df[['Date', 'Close']]
	df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

	m = Prophet()
	m.fit(df_train)
	future = m.make_future_dataframe(periods=period)
	forecast = m.predict(future)

	st.write(f'Forecast plot for {n_years} years')
	fig1 = plot_plotly(m, forecast)
	st.plotly_chart(fig1)

	# Show and plot forecast
	st.subheader('Forecast data')
	st.write(forecast.describe())

	st.write("Forecast components")
	fig2 = m.plot_components(forecast)
	st.write(fig2)