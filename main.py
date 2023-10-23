import streamlit as st 
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# a = [1,2,3,4,5,6]
# b = np.array(a)


# a ={
#     'name':['mahi','seema'],
#     'marks':[87,88]
# } 
# df = pd.read_csv('data.csv')
# st.write(a)

# df = pd.read_csv('data.csv')
#st.json(df)

# df = pd.read_csv('data.csv')
#st.dataframe(df, height=300, width=800)

# df = pd.read_csv('data.csv')
# st.write(df)


#data mining
df = pd.read_csv('data.csv')
st.title("Data Analysis")
df1 = df.drop(['SALARY'],axis='columns')
st.write(df1)
# st.map(df1)


#create button
if st.button('load Dataset'):
    st.write(df)
if st.button('load description'):
    st.write(df.describe())


#show chart
a1 = pd.DataFrame(df['NAME'],df['EMPID'])
st.line_chart(a1)


# if st.button('load bar chart'):
#  df2 = df.head(20)
# fig = plt.figure(figsize=(8,6))
# plt.bar(df2['NAME'],df2['EMPID'])
# st.pyplot(fig)


col1,col2,col3=st.columns(3)
col1.metric("NAME",'ABC','XYZ')
col2.metric('EMPID',1,2)


if st.sidebar.button('hii'):
    st.button('')
  