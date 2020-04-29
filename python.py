#step-1 describe 
# step-2 create 
import streamlit as st
import pandas as pd
import numpy as np
import plotly_express as px
import altair as alt
import datetime
import plotly.graph_objects as go
# get the dataset and read dataset into a dataframe and cache it 
df = st.cache(pd.read_csv,allow_output_mutation=True)("https://health-infobase.canada.ca/src/data/covidLive/covid19.csv")
 
# formate the date column to dd-mm-yyyy formate 
df['date']=pd.to_datetime(df['date'], format= '%d-%m-%Y')

#
##the first sidebar
pr= st.sidebar.multiselect('Province',df['prname'].unique())
##
m=df['date'].count()
dd=df['date'][m-1]-df['date'][0]
x = st.sidebar.slider('Timeline (Days)',0,dd.days,dd.days)
start_date = df['date'][0]
df=df[(df['date'] > start_date) & (df['date'] <= start_date+datetime.timedelta(days=x))]

#Province selection
new_df = df[(df['prname'].isin(pr))]

#showing count selection
value = st.sidebar.selectbox("Showing", ["numtotal", "numdeaths"])
var="This is the trend for {}".format(pr)
st.text(var)

#First plot
fig = px.scatter(new_df, x ='date', y=value,color=new_df['prname'])
st.plotly_chart(fig)
var1="This is the distribution in provinces"

#second plot

df1=df.groupby(['prname'], as_index=False)[value].max()
df1=df1.drop(index=2)
fig = px.treemap(df1,path=['prname'], values=value)
st.plotly_chart(fig)

#third table
st.write(new_df)



######notes for me :
## using Quicklab 
## posibility to use it for Datanalyst 
## Kunbernetees 

