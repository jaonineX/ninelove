import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

gender_data=pd.read_csv('./data/Transformed Data Set - Sheet1.csv')

plt.figure(figsize=(15,5))
sns.countplot(x='Gender', data=gender_data, hue='Favorite Color')
plt.title('Count of Favorite Colors by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')

st.pyplot(plt)

 