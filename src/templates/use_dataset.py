"""This page is for searching and viewing the list of awesome resources"""
"""By landry: jlandryf@gmail.com"""
import logging

import streamlit as st
import pandas as pd

import awesome_streamlit as ast
from awesome_streamlit.core.services import resources
import matplotlib.pyplot as plt
import re
from random import random
from PIL import Image
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import streamlit as st
import plotly.figure_factory as ff
import numpy as np


logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)



def sentiment_analysis(text):
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(text)
    if sentiment_dict['compound'] >= 0.05 :
        return 1
    elif sentiment_dict['compound'] <= - 0.05 :
        return -1
    else :
        return 0
    





def get_df(file):
    # get extension and read file
    extension = file.name.split('.')[1]
    if extension.upper() == 'CSV':
        df = pd.read_csv(file)
    elif extension.upper() == 'XLSX':
        df = pd.read_excel(file, engine='openpyxl')
    elif extension.upper() == 'PICKLE':
        df = pd.read_pickle(file)
    return df





def write():

    st.markdown('<h2 style="text-align: center; font-family: cursive; color: rgb(41, 43, 44)"><b>Data Visualization</b></h3>', unsafe_allow_html=True)
    st.sidebar.markdown('<h2 style="margin-top: 20px; font-family: cursive; color: rgb(255, 127, 39)"><b>********</b></h3>', unsafe_allow_html=True)

    st.info(
            """Your will select a dataset, and let the **algorithm Analyse them and display the result!**"""
        )
    st.markdown('''<p style="color: #d9534f">
                            This data should content a: <b>countries</b> column  <b></b> 
                            </p>
                            <p>
                                I am sure you want to test it yourself.
                            </p>
                            <p><b>Please Select the data and take a cup of coffee.</b></p>
                        ''', unsafe_allow_html=True)
    st.markdown('''
        <p> Here is an example of visualisation we got from our test </p>
        
    ''', unsafe_allow_html=True)
    
    file = st.file_uploader("Upload file", type=['csv'])
    if not file:
        st.write("Upload a .csv or .xlsx file to get started")
        return
    df_i = get_df(file)
    text = df_i['text']
    result = list()
    i=0
    
    
    for t in text:
        i = i+1
        result.append(sentiment_analysis(t))
        

    
    data = {i:result.count(i) for i in result}
    nb = len(result)
    st.write("")
    st.write("")
    st.write("")
    st.write("NUMBER OF RECORDS")
    st.write(nb)
    st.write("")
    st.write("")
    st.write("")
    st.write("STATISTICS")
    data1 = {'Sentiment': ['Neutral', 'Negative', 'Positive'], 'Reccurence': [data[0], data[-1], data[1]], 'Rate': [str(100*data[0]/nb) + "%", str(100*data[-1]/nb)+"%", str(100*data[1]/nb)+"%"]}  
    df = pd.DataFrame(data1)
    st.write(df)
    
    
    st.write("## Some Positive content")
    count = 0
    #st.write("# ", df_i.head())
    pos = {'tweet_id': [], 'airline':[],'text':[], 'tweet_created':[], 'tweet_location':[], 'airline_sentiment': [], 'negativereason': [], 'negativereason_confidence': [], 'airline':[]}
    positive = list()
    i = 0
    for j in result:
        if j == 1:
            positive.append(text[i])
            count = count+1
        i=i+1
        if count==10: break
    
    
    # Calling DataFrame constructor on list  
    #positive = pd.DataFrame(pos)  
    st.write(positive)  
    
    
    st.write("")
    st.write("=============================================================================================")
    st.write("## Some Negative content")
    count = 0
    i = 0
    negative = list()
    for j in result:
        if j == -1:
            negative.append(text[i])
            count = count+1
        i = i+1
        if count==10: break
    st.write(negative)
    
    
    st.write("")
    st.write("=============================================================================================")
    st.write("## Some Neutral content")
    count = 0
    i = 0
    neutral = list()
    for j in result:
        if j == 0:
            neutral.append(text[i])
            count = count+1
        i = i+1
        if count==10: break
    st.write(neutral)





if __name__ == "__main__":
    write()