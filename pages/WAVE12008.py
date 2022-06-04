import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit_theme as stt
import streamlit_theme as stt
def wave1():
    df = pd.read_csv('cleaneddata2.csv')
    select = st.sidebar.selectbox("EXPLORATORY DATA ANALYSIS WAVE1 2008",['TOTAL NUMBER OF STAFFS IN YEAR 2005 BY SECTORS ACORDING TO THEIR AREA OF SERVICES',
    'TOTAL NUMBER OF STAFFS IN YEAR 2006 BY SECTORS ACORDING TO THEIR AREA OF SERVICES',
        'TOTAL NUMBER OF STAFFS IN YEAR 2007 BY SECTORS ACORDING TO THEIR AREA OF SERVICES',
        'TOTAL AND AVERAGE TURNOVER FOR THE YEAR 2005 FOR EACH SECTOR GROUPED BY THEIR SERVICES',
        'TOTAL AND AVERAGE TURNOVER FOR THE YEAR 2006 FOR EACH SECTOR GROUPED BY THEIR SERVICES',
        'TOTAL AND AVERAGE TURNOVER FOR THE YEAR 2007 FOR EACH SECTOR GROUPED BY THEIR SERVICES'],key =1)
    if select == 'TOTAL NUMBER OF STAFFS IN YEAR 2005 BY SECTORS ACORDING TO THEIR AREA OF SERVICES':
        st.subheader('TOTAL NUMBER OF STAFFS IN YEAR 2005 BY SECTORS ACORDING TO THEIR AREA OF SERVICES',)
        fig = px.sunburst(df, path=['service', 'sector'], values='totalstaff05',width=800, height=500)
        fig.update_traces(textinfo='label+percent entry')
        fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),paper_bgcolor="#4233FF",)
        st.plotly_chart(fig)
    elif select == 'TOTAL NUMBER OF STAFFS IN YEAR 2006 BY SECTORS ACORDING TO THEIR AREA OF SERVICES':
                st.subheader('TOTAL NUMBER OF STAFFS IN YEAR 2006 BY SECTORS ACORDING TO THEIR AREA OF SERVICES')
                fig = px.sunburst(df, path=['service', 'sector'], values='totalstaff06',width=800, height=500)
                fig.update_traces(textinfo='label+percent entry')
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                    paper_bgcolor="#4233FF ",)
                st.plotly_chart(fig)
    elif select == 'TOTAL NUMBER OF STAFFS IN YEAR 2007 BY SECTORS ACORDING TO THEIR AREA OF SERVICES':
                st.subheader('TOTAL NUMBER OF STAFFS IN YEAR 2007 BY SECTORS ACORDING TO THEIR AREA OF SERVICES')
                fig = px.sunburst(df, path=['service', 'sector'], values='totalstaff07',width=800, height=500,color_continuous_scale='mint')
                fig.update_traces(textinfo='label+percent entry')
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                    paper_bgcolor="#4233FF ",)
                st.plotly_chart(fig)
    elif select == 'TOTAL AND AVERAGE TURNOVER FOR THE YEAR 2005 FOR EACH SECTOR GROUPED BY THEIR SERVICES':
                df = df[df['turnover05']!=0]
                st.subheader('TOTAL AND AVERAGE TURNOVER FOR THE YEAR 2005 FOR EACH SECTOR GROUPED BY THEIR SERVICES')
                fig = px.sunburst(df, path=['service', 'sector'], values='turnover05',width=800, height=500,color='turnover05', 
                color_continuous_scale='balance',color_continuous_midpoint=np.mean(df['turnover05']))
                fig.update_traces(textinfo='label+percent entry') 
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                    paper_bgcolor="#4233FF ",)
                st.plotly_chart(fig)
    elif select == 'TOTAL AND AVERAGE TURNOVER FOR THE YEAR 2006 FOR EACH SECTOR GROUPED BY THEIR SERVICES':
                df = df[df['turnover06']!=0]
                st.subheader('TOTAL AND AVERAGE TURNOVER FOR THE YEAR 2006 FOR EACH SECTOR GROUPED BY THEIR SERVICES')
                fig = px.sunburst(df, path=['service', 'sector'], values='turnover06',width=800, height=500,color='turnover06', 
                color_continuous_scale='redor',color_continuous_midpoint=np.mean(df['turnover06']))
                fig.update_traces(textinfo='label+percent entry') 
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                    paper_bgcolor="#4233FF ",)
                st.plotly_chart(fig)
    elif select == 'TOTAL AND AVERAGE TURNOVER FOR THE YEAR 2007 FOR EACH SECTOR GROUPED BY THEIR SERVICES':
                df = df[df['turnover07']!=0]
                st.subheader('TOTAL AND AVERAGE TURNOVER FOR THE YEAR 2007 FOR EACH SECTOR GROUPED BY THEIR SERVICES')
                fig = px.sunburst(df, path=['year','service', 'sector'], values='turnover07',width=800, height=500,color='turnover07', 
                color_continuous_scale='rainbow',color_continuous_midpoint=np.mean(df['turnover07']))
                fig.update_traces(textinfo='label+percent entry') 
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                    paper_bgcolor="#4233FF ",)

                st.plotly_chart(fig)
    

    
st.set_page_config(page_title="WAVE12008", page_icon="📈")
stt.set_theme({'primary': '#0E1117'})
st.markdown("#EXPLORATORY DATA ANALYSIS")
st.header(
        """This EXPLORATORY DATA ANALYSIS illustrates a combination of plotting for wave1 2008 Enjoy!""")
wave1()   

