# importing modules 
import pandas as pd
import plotly.express as px

# reading csv file 
df = pd.read_csv('covid-data.csv')

# drawing graph 
fig = px.scatter(df, x='date', y='cases', color='country', title='Covid-19')

# showing graph 
fig.show()