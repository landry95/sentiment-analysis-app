"""By landry: jlandryf@gmail.com"""
import streamlit as st

import awesome_streamlit as ast
from PIL import Image

# pylint: disable=line-too-long


def write():
    st.balloons()
    image = Image.open("./src/img/logo.PNG")
    st.image(image, use_column_width=True)
    """Used to write the page in the app.py file"""
    st.markdown('<h2><b><font color=‘#5bc0de’><i><u>Project : </u></i> Sentiment Analysis !</font></b></h2>', unsafe_allow_html=True)
    with st.spinner("Loading About ..."):
        # ast.shared.components.title_awesome(" - About")
        st.markdown('''
            <h3 style="font-family: cursive; color: rgb(255, 127, 39)"><b>About</b></h3>
            <p style="margin-top: 10px"> 
                In this project, we are using the <b> Some tweets Database's </b> to analyse if people are talking positively or negatively
            </p>
            <p>
                I developed it using several libraries
            </p>
            SOme are :
            <ul>
                <li>python ; </li>
                <li>Streamlit ; </li>
                <li>PIL ; </li>
                <li>awesome_streamlit ; </li>
                <li>pandas ; </li>
                <li>and many other ones. </li>
            </ul>
            <hr style="border:1px solid black">
            <h3 style="font-family: cursive; color: rgb(255, 127, 39)"><b>Why did I chose this dataset ?</b></h3>
            <p>I chosed to work on this dataset because it refers to a public opinion. Since more than one year, the world is facing a lot of pression, so a such a system can analyse and get how people are talking and how they're changing</p>
            <p style="margin-bottom: 30px">
                We can therefore get the rates
            </p><hr style="border:1px solid black">
            <h3 style="font-family: cursive; color: rgb(255, 127, 39)"><b>What did I do ?</b></h3>
            <div>
                <p>Also you can enter a text in the homepage textbox to get if your text has a positive or negetive content.</p>
                <p></p>
            </div>
            ''', 
            unsafe_allow_html=True
        )
