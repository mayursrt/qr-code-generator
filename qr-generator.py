#----------------------------------------------------------------------------------------------------------------------------
# Imports
import streamlit as st
from pyqrcode import QRCode
import pyqrcode
from PIL import Image
import png
from generate import *
#----------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------
# Title and Logo
title_container = st.beta_container()
col1, col2 = st.beta_columns([1, 5])
image = Image.open('assets/logo.jpg')
with title_container:
    with col1:
       st.image(image)
    with col2:
        st.title('QR Code Generator')
        st.markdown("""
Turn your personal links into QR Codes.
""")
st.title('')
#----------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------
# Body


#----------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------
# User Input
size = st.slider('Adjust the image size', min_value = 6, max_value = 12, value = 9)
clear_on_submit = st.checkbox('Clear on submit')

with st.form(key='my_form', clear_on_submit=clear_on_submit):
    content = st.text_input('Enter Link or Text')
    submit_button = st.form_submit_button(label='Generate')

#----------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------
# Main Function
if content:
    st.markdown("<h3 style='text-align: center; color: black;'>Here is your QR Code</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.beta_columns([5,10,1])
    col1.empty()
    col2.image(generate_qr(content, size), caption=f'QR Code Content : {content}')
    col3.empty()
#----------------------------------------------------------------------------------------------------------------------------



#---------------------------------------------------------------------------------------------------------------------------
# Footer
#MainMenu {visibility: hidden;}

footer="""<style>


a:link , a:visited{
color: black;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Made in Streamlit with ❤️ by <a href='https://github.com/mayursrt'>Mayur</a>.

</p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
#---------------------------------------------------------------------------------------------------------------------------



############################################################################################################################# 
#############################################################################################################################
