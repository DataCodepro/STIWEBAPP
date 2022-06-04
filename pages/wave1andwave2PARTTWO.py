import streamlit as st
import streamlit_theme as stt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
def wave1_and_wave2():
    df = pd.read_csv('cleaneddata2.csv')
    select = st.sidebar.selectbox("EXPLORATORY DATA ANALYSIS WAVE1 AND WAVE2",['Suggestions on how govt can encourage innovation1',
        'Suggestions on how govt can encourage innovation2','Suggestions on how govt can encourage innovation3',
        'Suggestions on how govt can encourage innovation4L','Suggestions on how govt can encourage innovation5',
        'Suggestions on how govt can encourage innovation6',
        'Suggestions on how govt can encourage innovation7','Suggestions on how govt can encourage innovation8',
        'State market', 'National market','ECOWAS market','Other Africa market','Europe market','US market','Asia market','Other markets'],key=1)
    if select == 'Suggestions on how govt can encourage innovation1':
                    st.subheader('VARIOUS SECTOR AND THIER SUGGESTION ON HOW GOVERNMENT CAN ENCOURAGE INNOVATION 1')
                    fig = px.histogram(df, x="sector", color="policy_suggestion1",width=800, height=600)
                    fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#4233FF ",)

                    st.plotly_chart(fig)
                

    elif select == 'Suggestions on how govt can encourage innovation2':
                st.subheader('VARIOUS SECTOR AND THIER SUGGESTION ON HOW GOVERNMENT CAN ENCOURAGE INNOVATION 2')
                fig = px.histogram(df, x="sector", color="policy_suggestion2",width=800, height=600)
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                    paper_bgcolor="#4233FF ",)
                st.plotly_chart(fig)
    elif select == 'Suggestions on how govt can encourage innovation3':
                st.subheader('VARIOUS SECTOR AND THIER SUGGESTION ON HOW GOVERNMENT CAN ENCOURAGE INNOVATION 3')
                fig = px.histogram(df, x="sector", color="policy_suggestion3",width=800, height=500)
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                    paper_bgcolor="#4233FF ",)
                st.plotly_chart(fig)
    elif select == 'Suggestions on how govt can encourage innovation4':
                st.subheader('VARIOUS SECTOR AND THIER SUGGESTION ON HOW GOVERNMENT CAN ENCOURAGE INNOVATION 4')
                fig = px.histogram(df, x="sector", color="policy_suggestion4",width=800, height=500)
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                    paper_bgcolor="#4233FF ",)
                st.plotly_chart(fig)
    elif select == 'Suggestions on how govt can encourage innovation5':
                st.subheader('VARIOUS SECTOR AND THIER SUGGESTION ON HOW GOVERNMENT CAN ENCOURAGE INNOVATION 5')
                fig = px.histogram(df, x="sector", color="policy_suggestion5",width=800, height=500) 
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                    paper_bgcolor="#4233FF ",)
                st.plotly_chart(fig)
    elif select == 'Suggestions on how govt can encourage innovation6':
                st.subheader('VARIOUS SECTOR AND THIER SUGGESTION ON HOW GOVERNMENT CAN ENCOURAGE INNOVATION 6')
                fig = px.histogram(df, x="sector", color="policy_suggestion6",width=800, height=500) 
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                    paper_bgcolor="#4233FF ",)
                st.plotly_chart(fig)
    elif select == 'Suggestions on how govt can encourage innovation7':
                st.subheader('VARIOUS SECTOR AND THIER SUGGESTION ON HOW GOVERNMENT CAN ENCOURAGE INNOVATION 7')
                fig = px.histogram(df, x="sector", color="policy_suggestion7",width=800, height=500)
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                    paper_bgcolor="#4233FF ",)
                st.plotly_chart(fig)
    elif select == 'Suggestions on how govt can encourage innovation8':
                st.subheader('VARIOUS SECTOR AND THIER SUGGESTION ON HOW GOVERNMENT CAN ENCOURAGE INNOVATION 8')
                fig = px.histogram(df, x="sector", color="policy_suggestion8",width=800, height=500)
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                    paper_bgcolor="#4233FF ",)
                st.plotly_chart(fig)
    elif select == 'State market':
                st.subheader('SECTORS AND THEIR INVOLVEMENT IN THE STATE MARKET')
                fig = px.histogram(df, x="sector", color="market1",width=800, height=500)
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                    paper_bgcolor="#4233FF ",)
                st.plotly_chart(fig)
    elif select == 'National market':
                st.subheader('SECTORS AND THEIR INVOLVEMENT IN THE NATIONAL MARKET')
                fig = px.histogram(df, x="sector", color="market2",width=800, height=500)
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                    paper_bgcolor="#4233FF ",)
                st.plotly_chart(fig)
    elif select == 'ECOWAS market':
                st.subheader('SECTORS AND THEIR INVOLVEMENT IN THE ECOWAS MARKET')
                fig = px.histogram(df, x="sector", color="market3",width=800, height=500)
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                    paper_bgcolor="#4233FF ",)
                st.plotly_chart(fig)
    elif select == 'Other Africa market':
                st.subheader('SECTORS AND THEIR INVOLVEMENT IN OTHER AFRICA MARKET')
                fig = px.histogram(df, x="sector", color="market4",width=800, height=500)
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                    paper_bgcolor="#4233FF ",)
                st.plotly_chart(fig)
    elif select == 'Europe market':
                st.subheader('SECTORS AND THEIR INVOLVEMENT IN THE EUROPE MARKET')
                fig = px.histogram(df, x="sector", color="market5",width=800, height=500)
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                    paper_bgcolor="#4233FF ",)
                st.plotly_chart(fig)
    elif select == 'US market':
                st.subheader('SECTORS AND THEIR INVOLVEMENT IN THE US MARKET')
                fig = px.histogram(df, x="sector", color="market6",width=800, height=500)
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                    paper_bgcolor="#4233FF ",)
                st.plotly_chart(fig)
    elif select == 'Asia market':
                st.subheader('SECTORS AND THEIR INVOLVEMENT IN THE ASIA MARKET')
                fig = px.histogram(df, x="sector", color="market7",width=800, height=500)
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                    paper_bgcolor="#4233FF ",)
                st.plotly_chart(fig)
    elif select == 'Other markets':
                st.subheader('SECTORS AND THEIR INVOLVEMENT IN OTHER MARKET')
                fig = px.histogram(df, x="sector", color="market8",width=800, height=500)
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                    paper_bgcolor="#4233FF ",)
                st.plotly_chart(fig)
   
st.set_page_config(page_title="WAVE1&2PART2", page_icon="📈")
st.markdown("#EXPLORATORY DATA ANALYSIS")
    
st.header(
        """This EXPLORATORY DATA ANALYSIS illustrates a combination of plotting for wave1 and wave2 Enjoy!""")
wave1_and_wave2() 