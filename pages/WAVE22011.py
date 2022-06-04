import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


def wave2():
    df = pd.read_csv('cleaneddata2.csv')
    select = st.sidebar.selectbox("EXPLORATORY DATA ANALYSIS WAVE2 2011",['TOTAL NUMBER OF STAFFS IN YEAR 2008 BY SECTORS ACORDING TO THEIR AREA OF SERVICES',
    'TOTAL NUMBER OF STAFFS IN YEAR 2009 BY SECTORS ACORDING TO THEIR AREA OF SERVICES',
        'TOTAL NUMBER OF STAFFS IN YEAR 2010 BY SECTORS ACORDING TO THEIR AREA OF SERVICES',
        'TOTAL AND AVERAGE TURNOVER FOR THE YEAR 2008 FOR EACH SECTOR GROUPED BY THEIR SERVICES',
        'TOTAL AND AVERAGE TURNOVER FOR THE YEAR 2009 FOR EACH SECTOR GROUPED BY THEIR SERVICES',
        'TOTAL AND AVERAGE TURNOVER FOR THE YEAR 2010 FOR EACH SECTOR GROUPED BY THEIR SERVICES'],key =1)
    if select == 'TOTAL NUMBER OF STAFFS IN YEAR 2008 BY SECTORS ACORDING TO THEIR AREA OF SERVICES':
        st.subheader('TOTAL NUMBER OF STAFFS IN YEAR 2008 BY SECTORS ACORDING TO THEIR AREA OF SERVICES',)
        fig = px.sunburst(df, path=['service', 'sector'], values='totalstaff08',width=800, height=500)
        fig.update_traces(textinfo='label+percent entry')
        fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),paper_bgcolor="#4233FF",)
        st.plotly_chart(fig)
    elif select == 'TOTAL NUMBER OF STAFFS IN YEAR 2009 BY SECTORS ACORDING TO THEIR AREA OF SERVICES':
                st.subheader('TOTAL NUMBER OF STAFFS IN YEAR 2009 BY SECTORS ACORDING TO THEIR AREA OF SERVICES')
                fig = px.sunburst(df, path=['service', 'sector'], values='totalstaff09',width=800, height=500)
                fig.update_traces(textinfo='label+percent entry')
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                    paper_bgcolor="#4233FF ",)
                st.plotly_chart(fig)
    elif select == 'TOTAL NUMBER OF STAFFS IN YEAR 2010 BY SECTORS ACORDING TO THEIR AREA OF SERVICES':
                st.subheader('TOTAL NUMBER OF STAFFS IN YEAR 2010 BY SECTORS ACORDING TO THEIR AREA OF SERVICES')
                fig = px.sunburst(df, path=['service', 'sector'], values='totalstaff10',width=800, height=500,color_continuous_scale='mint')
                fig.update_traces(textinfo='label+percent entry')
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                    paper_bgcolor="#4233FF ",)
                st.plotly_chart(fig)
    elif select == 'TOTAL AND AVERAGE TURNOVER FOR THE YEAR 2008 FOR EACH SECTOR GROUPED BY THEIR SERVICES':
                df = df[df['turnover08']!=0]
                st.subheader('TOTAL AND AVERAGE TURNOVER FOR THE YEAR 2008 FOR EACH SECTOR GROUPED BY THEIR SERVICES')
                fig = px.sunburst(df, path=['service', 'sector'], values='turnover08',width=800, height=500,color='turnover08', 
                color_continuous_scale='balance',color_continuous_midpoint=np.mean(df['turnover08']))
                fig.update_traces(textinfo='label+percent entry') 
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                    paper_bgcolor="#4233FF ",)
                st.plotly_chart(fig)
    elif select == 'TOTAL AND AVERAGE TURNOVER FOR THE YEAR 2009 FOR EACH SECTOR GROUPED BY THEIR SERVICES':
                df = df[df['turnover09']!=0]
                st.subheader('TOTAL AND AVERAGE TURNOVER FOR THE YEAR 2009 FOR EACH SECTOR GROUPED BY THEIR SERVICES')
                fig = px.sunburst(df, path=['service', 'sector'], values='turnover09',width=800, height=500,color='turnover09', 
                color_continuous_scale='redor',color_continuous_midpoint=np.mean(df['turnover09']))
                fig.update_traces(textinfo='label+percent entry') 
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                    paper_bgcolor="#4233FF ",)
                st.plotly_chart(fig)
    elif select == 'TOTAL AND AVERAGE TURNOVER FOR THE YEAR 2010 FOR EACH SECTOR GROUPED BY THEIR SERVICES':
                df = df[df['turnover10']!=0]
                st.subheader('TOTAL AND AVERAGE TURNOVER FOR THE YEAR 2010 FOR EACH SECTOR GROUPED BY THEIR SERVICES')
                fig = px.sunburst(df, path=['service', 'sector'], values='turnover10',width=800, height=500,color='turnover10', 
                color_continuous_scale='rainbow',color_continuous_midpoint=np.mean(df['turnover10']))
                fig.update_traces(textinfo='label+percent entry') 
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                    paper_bgcolor="#4233FF ",)

                st.plotly_chart(fig)
    

    
st.set_page_config(page_title="WAVE22011", page_icon="📈",)
st.markdown("#EXPLORATORY DATA ANALYSIS")
    
st.header(
        """This EXPLORATORY DATA ANALYSIS illustrates a combination of plotting for wave2 2011 Enjoy!""")
wave2()   
