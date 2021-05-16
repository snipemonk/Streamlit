
import streamlit as st
import pandas as pd
import seaborn as sns
st.set_option('deprecation.showPyplotGlobalUse', False)
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image,ImageFilter,ImageEnhance

def main():
	st.title("Iris EDA App")
	st.subheader("EDA Web App with Streamlit ")
	my_dataset = "C:/Users/Administrator/Desktop/Work/Datasets/Iris.csv"

	@st.cache(persist=True)
	def explore_data(dataset):
		df = pd.read_csv(dataset)
		return df

	data = explore_data(my_dataset)
	if st.checkbox("Preview DataFrame"):
		if st.button("Head"):
			st.write(data.head())
		if st.button("Tail"):
			st.write(data.tail())
		else:
			st.write(data.head(2))
	if st.checkbox("Show All DataFrame"):
		st.dataframe(data)

	# Show All Column Names
	if st.checkbox("Show All Column Name"):
		st.text("Columns:")
		st.write(data.columns)

	# Show Dimensions and Shape of Dataset
	data_dim = st.radio('What Dimension Do You Want to Show', ('Rows', 'Columns'))
	if data_dim == 'Rows':
		st.text("Showing Length of Rows")
		st.write(len(data))
	if data_dim == 'Columns':
		st.text("Showing Length of Columns")
		st.write(data.shape[1])

	# Show Summary of Dataset
	if st.checkbox("Show Summary of Dataset"):
		st.write(data.describe())
	species_option = st.selectbox('Select Columns',
								  ('SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species'))
	if species_option == 'SepalLengthCm':
		st.write(data['SepalLengthCm'])
	elif species_option == 'SepalWidthCm':
		st.write(data['SepalWidthCm'])
	elif species_option == 'PetalLengthCm':
		st.write(data['PetalLengthCm'])
	elif species_option == 'PetalWidthCm':
		st.write(data['PetalWidthCm'])
	elif species_option == 'Species':
		st.write(data['Species'])
	else:
		st.write("Select A Column")

	# Show Plots
	if st.checkbox("Simple Bar Plot with Matplotlib "):
		data.plot(kind='bar')
		st.pyplot()

	# Show Correlation Plots
	if st.checkbox("Simple Correlation Plot with Matplotlib "):
		plt.matshow(data.corr())
		st.pyplot()

	# Show Correlation Plots with Sns
	if st.checkbox("Simple Correlation Plot with Seaborn "):
		st.write(sns.heatmap(data.corr(), annot=True))
		# Use Matplotlib to render seaborn
		st.pyplot()

	# Show Plots
	if st.checkbox("Bar Plot of Groups or Counts"):
		v_counts = data.groupby('species')
		st.bar_chart(v_counts)

	# About
	if st.button("About App"):
		st.subheader("Iris Dataset EDA App")
		st.text("Built with Streamlit")


	if st.checkbox("By"):
		st.text("Created by Shriraj Misra")



if __name__ == "__main__":
	main()
