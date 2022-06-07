import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def wave1_and_wave2():
    df = pd.read_csv('cleaneddata2.csv')
    select = st.sidebar.selectbox("EXPLORATORY DATA ANALYSIS WAVE1 AND WAVE2",['NO OF COMPANY IN EACH SECTOR',
        'PERCENTAGE RATE OF EACH SECTOR','GROUPING OF SECTORS ACORDING TO THEIR AREA OF SERVICE',
        'SECTORS AND THEIR INFORMATION SOURCE - INTERNAL',
        'SECTORS AND THEIR INFORMATION SOURCE - SUPPLIERS','SECTORS AND THEIR INFORMATION SOURCE -CUSTORMERS',
        'SECTORS AND THEIR INFORMATION SOURCE -COMPETITORS','SECTORS AND THEIR INFORMATION SOURCE -CONSULTANTS, COMMERCIAL LABS OR PRIVATE R&D INSTITUTES',
        'SECTORS AND THEIR INFORMATION SOURCE -UNIVERSITIES, OTHER HIGHER ED. INSTITUTIONS','SECTORS AND THEIR INFORMATION SOURCE -PUBLIC RESEARCH INSTITUTES',
        'SECTORS AND THEIR INFORMATION SOURCE -CONFERENCES, FAIRS, EXHIBITIONS','SECTORS AND THEIR INFORMATION SOURCE -JOURNALS, TRADE PUBLICATIONS',
        'SECTORS AND THEIR INFORMATION SOURCE -PROFESSIONAL, INDUSTRY ASSOCIATIONS'],key=1)
    if select == 'NO OF COMPANY IN EACH SECTOR':
               
                df2= df['sector'].value_counts()
                
                
                st.subheader('VARIOUS SECTOR AND THE TOTAL NUMBER OF INDUSTRIES UNDER EACH SECTORS')
                fig = px.bar(x=df2.index,y = df2.values ,labels={'x':'Sector','y':'Outcome'},width=800, height=800)
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44 ",)

                st.plotly_chart(fig)
                st.table(df2)
          
    elif select == 'PERCENTAGE RATE OF EACH SECTOR':
                df2= df['sector'].value_counts()
                st.subheader('PERCENTAGE RATE OF EACH SECTOR')
                fig =px.pie(names=df2.index,values=df2.values,color = df2.index,width=800, height=500)
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
            paper_bgcolor="#4233FF",)
                fig.update_traces(textposition='inside', textinfo='percent+label')
                st.plotly_chart(fig)
    elif select == 'GROUPING OF SECTORS ACORDING TO THEIR AREA OF SERVICE':
                st.subheader('GROUPING OF SECTORS ACORDING TO THEIR AREA OF SERVICES')
                fig = px.histogram(df, x="sector", color="service",width=800, height=600)
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                    paper_bgcolor="#4233FF ",)
                st.plotly_chart(fig)
    elif select == 'SECTORS AND THEIR INFORMATION SOURCE - INTERNAL':
                st.subheader(' SECTORS AND THEIR INFORMATION SOURCE - INTERNAL')
                fig = px.histogram(df, x="sector", color="sinfo1",width=800, height=500)
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                    paper_bgcolor="#4233FF ",)
                st.plotly_chart(fig)
    elif select == 'SECTORS AND THEIR INFORMATION SOURCE - SUPPLIERS':
                st.subheader('SECTORS AND THEIR INFORMATION SOURCE - SUPPLIERS')
                fig = px.histogram(df, x="sector", color="sinfo2",width=800, height=500)
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                    paper_bgcolor="#4233FF ",)
                st.plotly_chart(fig)
    elif select == 'SECTORS AND THEIR INFORMATION SOURCE -CUSTORMERS':
                st.subheader('SECTORS AND THEIR INFORMATION SOURCE -CUSTORMERS')
                fig = px.histogram(df, x="sector", color="sinfo3",width=800, height=500) 
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                    paper_bgcolor="#4233FF ",)
                st.plotly_chart(fig)
    elif select == 'SECTORS AND THEIR INFORMATION SOURCE -COMPETITORS':
                st.subheader('SECTORS AND THEIR INFORMATION SOURCE -COMPETITORS')
                fig = px.histogram(df, x="sector", color="sinfo4",width=800, height=500) 
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                    paper_bgcolor="#4233FF ",)
                st.plotly_chart(fig)
    elif select == 'SECTORS AND THEIR INFORMATION SOURCE -CONSULTANTS, COMMERCIAL LABS OR PRIVATE R&D INSTITUTES':
                st.subheader('SECTORS AND THEIR INFORMATION SOURCE -CONSULTANTS, COMMERCIAL LABS OR PRIVATE R&D INSTITUTES')
                fig = px.histogram(df, x="sector", color="sinfo5",width=800, height=500)
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                    paper_bgcolor="#4233FF ",)
                st.plotly_chart(fig)
    elif select == 'SECTORS AND THEIR INFORMATION SOURCE -UNIVERSITIES, OTHER HIGHER ED. INSTITUTIONS':
                st.subheader('SECTORS AND THEIR INFORMATION SOURCE -UNIVERSITIES, OTHER HIGHER ED. INSTITUTIONS')
                fig = px.histogram(df, x="sector", color="sinfo6",width=800, height=500)
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                    paper_bgcolor="#4233FF ",)
                st.plotly_chart(fig)
    elif select == 'SECTORS AND THEIR INFORMATION SOURCE -PUBLIC RESEARCH INSTITUTES':
                st.subheader('SECTORS AND THEIR INFORMATION SOURCE -PUBLIC RESEARCH INSTITUTES')
                fig = px.histogram(df, x="sector", color="sinfo7",width=800, height=500)
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                    paper_bgcolor="#4233FF ",)
                st.plotly_chart(fig)
    elif select == 'SECTORS AND THEIR INFORMATION SOURCE -CONFERENCES, FAIRS, EXHIBITIONS':
                st.subheader('SECTORS AND THEIR INFORMATION SOURCE -CONFERENCES, FAIRS, EXHIBITIONS')
                fig = px.histogram(df, x="sector", color="sinfo8",width=800, height=500)
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                    paper_bgcolor="#4233FF ",)
                st.plotly_chart(fig)
    elif select == 'SECTORS AND THEIR INFORMATION SOURCE -JOURNALS, TRADE PUBLICATIONS':
                st.subheader('SECTORS AND THEIR INFORMATION SOURCE -JOURNALS, TRADE PUBLICATIONS')
                fig = px.histogram(df, x="sector", color="sinfo9",width=800, height=500)
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                    paper_bgcolor="#4233FF ",)
                st.plotly_chart(fig)
    elif select == 'SECTORS AND THEIR INFORMATION SOURCE -PROFESSIONAL, INDUSTRY ASSOCIATIONS':
                st.subheader('SECTORS AND THEIR INFORMATION SOURCE -PROFESSIONAL, INDUSTRY ASSOCIATIONS')
                fig = px.histogram(df, x="sector", color="sinfo10",width=800, height=500)
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                    paper_bgcolor="#4233FF ",)
                st.plotly_chart(fig)
st.set_page_config(page_title="WAVE1&2", page_icon="📈")
st.markdown("#EXPLORATORY DATA ANALYSIS")
    
st.header(
        """This EXPLORATORY DATA ANALYSIS illustrates a combination of plotting for wave1 and wave2 Enjoy!""")
wave1_and_wave2() 
