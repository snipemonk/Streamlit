import streamlit as st

st.title('Sample Streamlit App')
st.header('This is a Header')
st.subheader('This is a subheader')

st.text('Hello Streamlit')
st.markdown('### This is a Markdown')

st.success('Successful')
st.info('Information')
st.warning('This is a warning')
st.error('This is an Error')
st.help(range)

st.write('Text with write')
st.write(range(10))

from PIL import Image
img=Image.open("C:/Users/Administrator/Pictures/nature.jfif")
st.image(img,width=300,caption="Simple App")

#Widget # Checkbox

if st.checkbox("Show/Hide"):
    st.text("Showing or Hiding Widget")

#Radio Button
status=st.radio("What is your status",("Active","Inactive"))
if status=='Active':
    st.success("You are Active")
else:
    st.warning("Inactive,Activate)

#This file will be pushed to Master Branch