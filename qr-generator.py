#----------------------------------------------------------------------------------------------------------------------------
# Imports
import streamlit as st
from pyqrcode import QRCode
import pyqrcode
from PIL import Image
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
#----------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------
# Body
with st.form(key='my_form', clear_on_submit=True):
    content = st.text_input('Enter Link')
    submit_button = st.form_submit_button(label='Check')

st.text(content)
#----------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------
# User Input

#----------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------
# Main Function
url = pyqrcode.create(content)
url.svg("myyoutube.svg", scale = 8)
#----------------------------------------------------------------------------------------------------------------------------



#---------------------------------------------------------------------------------------------------------------------------
# Footer


footer="""<style>

#MainMenu {visibility: hidden;}
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
