# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 22:12:03 2022

@author: PC-2022
"""

import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import numpy as np

import awesome_streamlit as ast

#st.title('Sentiment Analysis Application')

import src.templates.home

PAGES = {
    "Home": src.templates.home
}


st.markdown('<h4 style="text-align: center; font-family: cursive; color: rgb(255, 127, 39)"><b>WELCOME TO THE SENTIMENT ANALYSIS APPLICATION</b></h4>', unsafe_allow_html=True)



#THis function Analysis the text passed in parameter
def sentiment_analysis(text):
 
    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()
 
    # polarity_scores method of SentimentIntensityAnalyzer
    # object gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(text)
     
    print("Overall sentiment dictionary is : ", sentiment_dict)
    print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative")
    print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral")
    print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive")
 
    print("Sentence Overall Rated As", end = " ")
 
    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05 :
        print("Positive")
        st.markdown('<h2><b><font color="#5bc0de"><i>POSITIVE </i></font></b></h2>', unsafe_allow_html=True)
 
    elif sentiment_dict['compound'] <= - 0.05 :
        print("Negative")
        st.markdown('<h2><b><font color="#FF4F33"><i>NEGATIVE</i></font></b></h2>', unsafe_allow_html=True)
    else :
        print("Neutral")
        st.markdown('<h2><b><font ><i>NEUTRAL</i></font></b></h2>', unsafe_allow_html=True)
        

#This is executed when the page loads
#Form with a textarea
with st.form("my_form"):
    st.markdown('<b>So Exited to analyse your text.:</b>', unsafe_allow_html=True)
    text = st.text_area("Write here", value="", height=None, max_chars=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)
    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("Your Text : ", text)
        #st.markdown('<br><br><b>Sentiment:</b>', unsafe_allow_html=True)
        sentiment_analysis(text)



