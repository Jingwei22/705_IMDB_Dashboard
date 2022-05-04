# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 22:21:02 2022

@author: jingw
"""

import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

df = pd.read_csv('C:/Users/jingw/OneDrive/Desktop/Bentley Spring 2022/MA705/individual project/final_IMDB_dataset.csv')
#print(df)
stylesheet = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=stylesheet)
server = app.server

def generate_table(dataframe, max_rows=250):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


fig = px.bar(df, x = 'genre', y = 'votes', title = 'Bar Chart for the total votes in each genre')
checklist_options = [{'label': genre, 'value':genre} for genre in set(df.genre)]
checklist_options1 = [{'label': IMDBrating, 'value':IMDBrating} for IMDBrating in set(df.IMDBrating)]
#print(checklist_options)
fig2 = px.bar(df, x = 'IMDBrating', y = 'movieGross', title = 'Bar Chart for the total Movie Gross from IMDB rating 8 to 9.3')

app.layout = html.Div(
    [
    html.H1('Top IMDB Movie Analysis Dashboard', style = {'textAlign':'center'}),
    html.H3('By Jingwei Cui', id ='author', style = {'textAlign':'center'}),
    html.Div([
        dcc.Markdown("""
        This dataset comes from the link below, which including almost every information about the top 250 movies.
        
        You can browser the website and look at every movie poster. 
        """),
    ]),
    html.A('Click here to go to IMDB "Top 250" movies website', 
           href = 'https://www.imdb.com/search/title/?groups=top_250&sort=num_votes,desc',
           target = '_blank'),
    html.Div(generate_table(df)),
    html.H3('This table will show you the gap of total votes between each movie genre, you can see action movies have the highest total votes, and Film-Noir has the lowest total votes',style = {'textAlign':'center'}),
    dcc.Graph(figure=fig, id='plot'),
    html.Div([html.H4('Genres to Display:'),
              dcc.Checklist(
                  options=checklist_options,
                  value=['Drama', 'Action'],
                  id = 'checklist',style={"width": "20%"})],
             ),
    html.H3('This table will show you the gap of total movie gross between each IMDB rating from 8 to 9.3, you can see the movies at score 8.1 has the highest total movie gross',style = {'textAlign':'center'}),    
    dcc.Graph(figure=fig2, id='plot1'),
    html.Div([html.H4('IMDB rating to Display:'),
              dcc.Checklist(
                  options=checklist_options1,
                  value=[8, 8.1],
                  id = 'checklist1',style={"width": "20%"})])
    ]
    )

@app.callback(
    Output('plot', 'figure'),
    Input('checklist', 'value'))
def update_plot(value):
    df2 = df[df.genre.isin(value)]
    fig = px.bar(df2, x = 'genre', y = 'votes', title = 'Bar Chart for the total votes in each genre')
    return fig

@app.callback(
    Output('plot1', 'figure'),
    Input('checklist1', 'value'))

def update_plot1(value):
    df3 = df[df.IMDBrating.isin(value)]
    fig = px.bar(df3, x = 'IMDBrating', y = 'movieGross', title = 'Bar Chart for the total Movie Gross from IMDB rating 8 to 9.3')
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)