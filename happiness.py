from lib2to3.pgen2.pgen import DFAState
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objs as go



st.set_page_config(page_title="Streamlit Dashboard",layout="wide")






# To create a graph showing the countries with the highest and lowest happiness scores:

data = pd.read_csv("2019new.csv")
# Filter the dataset to include only the country name and happiness score
df = data[['Country or region', 'Score']]
# Sort the dataset by happiness score in descending order
df = df.sort_values(by='Score', ascending=False)
# Get the top 10 and bottom 10 countries by happiness score
top_10 = df.head(10)
bottom_10 = df.tail(10)
# Define traces for the bar graph and set the marker color for each trace
trace1 = go.Bar(x=top_10['Score'], y=tuple(top_10['Country or region']), name='Top 10 countries', orientation='h', marker=dict(color='#0099ff'))
trace2 = go.Bar(x=bottom_10['Score'], y=tuple(bottom_10['Country or region']), name='Bottom 10 countries', orientation='h', marker=dict(color='#ff9999'))
# Customize the graph
layout = go.Layout(title='Happiness Scores of Top 10 and Bottom 10 Countries',
                   xaxis=dict(title='Happiness Score'))
# Create a Figure object with the defined traces and layout
fig = go.Figure(data=[trace1, trace2], layout=layout)



# Create a correlation matrix using Plotly
corr_matrix = data.corr()

fig = go.Figure(data=go.Heatmap(
                   z=corr_matrix.values,
                   x=corr_matrix.columns,
                   y=corr_matrix.index,
                   colorscale='RdBu'))

fig.update_layout(
    title='Correlation Matrix',
    height=600, width=800,
    xaxis_title='Variables',
    yaxis_title='Variables'
)


# st.tabs() - used to create tabs just like web browsers
tab1 , tab2, tab3, tab4, tab5, tab6, tab7= st.tabs(["Dataset", "Boxplot", "Pie Charts", "Scatterplots", "Line Graphs", "Bar Graph","Correlation Matrix"])
with tab1:
    data = pd.read_csv("Correctcountry.csv")
    st.title("World Happiness Report :smile:")
    st.sidebar.header("Please filter here")
    options = ['All'] + data['Region'].unique().tolist()
    Category = st.sidebar.multiselect("Select the Region",
                                      options =  data['Region'].unique().tolist(),
                                      default = data['Region'].unique().tolist())
    data = data.query('Region in @Category')
    st.write(data)

     
with tab2:
     # Create a boxplot using Plotly
     st.header("Summary of Happiness Score values")
     fig = px.box(data, y='Score', 
     title='Boxplot of Happiness Scores',
     labels={'Happiness Score': 'Happiness Score'})
     st.plotly_chart(fig)
with tab3:
     st.header("Pie Chart depicting No of Countries in each Region")
     df = pd.read_csv("2019new (2).csv")
     # Group data by continent and count the number of countries in each
     Region_counts = df.groupby('Region')['Country or region'].nunique()

     # Create a pie chart
     fig = px.pie(values=Region_counts.values, names=Region_counts.index, title='Distribution of Countries by Region')
     fig.update_traces(marker=dict(colors=px.colors.qualitative.Pastel))
     fig.update_layout(title_text='Distribution of Countries by Region')
     st.plotly_chart(fig)
     # Pie charts for top 10 and bottom 10 countries

     st.header("Which Regions do the Happiest Countries belong to?")
     # Create a new dataframe with 'Country or region', 'Region', and 'Score'
     data2 = data[['Country or region', 'Region', 'Score']]
     # Merge the 'data2' dataframe with the 'top_10' and 'bottom_10' dataframes
     top_10_region = pd.merge(top_10, data2, on='Country or region', how='left')
     bottom_10_region = pd.merge(bottom_10, data2, on='Country or region', how='left')
     # Group the top 10 and bottom 10 countries by region
     top_10_region_count = top_10_region.groupby('Region').count()['Country or region']
     # Define the traces for the pie chart
     trace1 = go.Pie(labels=top_10_region_count.index, values=top_10_region_count.values, name='Top 10 countries')
     # Customize the graph
     layout = go.Layout(title='Distribution of Regions among Top 10')
     # Create a Figure object with the defined traces and layout
     fig = go.Figure(data=[trace1], layout=layout)

     st.plotly_chart(fig)


     st.header("Which Regions do the least happy Countries belong to?")
     bottom_10_region_count = bottom_10_region.groupby('Region').count()['Country or region']
     trace2 = go.Pie(labels=bottom_10_region_count.index, values=bottom_10_region_count.values, name='Bottom 10 countries')
     layout = go.Layout(title='Distribution of Regions among Bottom 10 Countries')
     fig = go.Figure(data=[trace2], layout=layout)
     st.plotly_chart(fig)
with tab4:
     st.header("Relationship between Happiness Scores and Independent Variables")
     data = pd.read_csv("2019new.csv")
     # create differet columns using columns() 
     with st.container():
        col1, col2= st.columns(2)
        with col1:
            fig = px.scatter(data, x="Generosity",y="Score", color="Country or region", title = "Happiness Score vs Generosity")
            width = 700
            st.plotly_chart(fig, use_container_width=True, width=width)
            fig = px.scatter(data, x="GDP per capita",y="Score", color="Country or region", title = "Happiness Score vs GDP per Capita")
            width = 700
            st.plotly_chart(fig, use_container_width=True, width=width)
            fig = px.scatter(data, x="Healthy life expectancy",y="Score", color="Country or region", title = "Happiness Score vs Healthy Life Expectancy")
            width = 700
            st.plotly_chart(fig, use_container_width=True, width=width)
            # set the width of both plots to 500 pixels

        with col2:
            
            fig = px.scatter(data, x="Social support",y="Score", color="Country or region", title = "Happiness Score vs Social support")
            width = 700
            st.plotly_chart(fig, use_container_width=True, width=width)
            fig = px.scatter(data, x="Freedom to make life choices",y="Score", color="Country or region", title = "Happiness Score vs Freedom to make life choices")
            width = 700
            st.plotly_chart(fig, use_container_width=True, width=width)
            fig = px.scatter(data, x="Perceptions of corruption",y="Score", color="Country or region", title = "Happiness Score vs Perceptions of corruption")
            width = 700
            st.plotly_chart(fig, use_container_width=True, width=width)
with tab5:
     st.header("India Over the Years")
     # Create a dictionary with the happiness scores and rankings for each year
     data = {'Ranking': [117,118,122,133,140], 
        'score': [4.565,4.404,4.315000057,4.19,4.015]}

     # Create a DataFrame from the dictionary
     df = pd.DataFrame(data, index=['2015', '2016', '2017', '2018', '2019'])

     # Define a trace for the line graph
     trace = go.Scatter(x=df.index, y=df['score'], mode='lines+markers', name='Happiness Score')
     # Customize the graph
     layout = go.Layout(title='Happiness Score of India from 2015 to 2019',
                   xaxis=dict(title='Year'),
                   yaxis=dict(title='Happiness Score'))
     # Create a Figure object with the defined trace and layout
     fig = go.Figure(data=[trace], layout=layout)
     # Use show() method to display the graph in a browser
     st.plotly_chart(fig)

     # Define a trace for the line graph
     trace = go.Scatter(x=df.index, y=df['Ranking'], mode='lines+markers', name='Happiness Ranking')
     # Customize the graph
     layout = go.Layout(title='Happiness Ranking of India from 2015 to 2019',
                   xaxis=dict(title='Year'),
                   yaxis=dict(title='Happiness Ranking'))
     # Create a Figure object with the defined trace and layout
     fig = go.Figure(data=[trace], layout=layout)
     # Use show() method to display the graph in a browser
     st.plotly_chart(fig)
with tab6:
     data = pd.read_csv("2019new.csv")

     st.header("Which are the Happiest and the Saddest Countries? ")
     # Filter the dataset to include only the country name and happiness score
     df = data[['Country or region', 'Score']]
     # Sort the dataset by happiness score in descending order
     df = df.sort_values(by='Score', ascending=False)
     # Get the top 10 and bottom 10 countries by happiness score
     top_10 = df.head(10)
     bottom_10 = df.tail(10)
     # Define traces for the bar graph and set the marker color for each trace
     trace1 = go.Bar(x=top_10['Score'], y=tuple(top_10['Country or region']), name='Top 10 countries', orientation='h', marker=dict(color='#0099ff'))
     trace2 = go.Bar(x=bottom_10['Score'], y=tuple(bottom_10['Country or region']), name='Bottom 10 countries', orientation='h', marker=dict(color='#ff9999'))
     # Customize the graph
     layout = go.Layout(title='Happiness Scores of Top 10 and Bottom 10 Countries',
                   xaxis=dict(title='Happiness Score'))
     # Create a Figure object with the defined traces and layout
     fig = go.Figure(data=[trace1, trace2], layout=layout)
     st.plotly_chart(fig)


with tab7:
     # Create a correlation matrix using Plotly

     st.header("How do the different variables relate to each other?")
     corr_matrix = data.corr()

     fig = go.Figure(data=go.Heatmap(
                   z=corr_matrix.values,
                   x=corr_matrix.columns,
                   y=corr_matrix.index,
                   colorscale='RdBu'))

     fig.update_layout(
     title='Correlation Matrix',
     height=600, width=800,
     xaxis_title='Variables',
     yaxis_title='Variables'
      )

     # Display the chart in the Streamlit app
     st.plotly_chart(fig)




          
     
    




















