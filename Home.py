import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

gender_data=pd.read_csv('./data/Transformed Data Set - Sheet1.csv')


html_0 = """
<div style="background-color:#0E1117;border-bottom: 3px solid #ffffff;border-top: 3px solid #ffffff;">
<center><h3>Example data table</h3></center>
</div>
"""



st.markdown(html_0, unsafe_allow_html=True)
st.markdown("")
st.write(gender_data.head(10))
plt.figure(figsize=(15,5))
sns.countplot(x='Gender', data=gender_data, hue='Favorite Color')
plt.title('Count of Favorite Colors by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')

st.pyplot(plt)

 