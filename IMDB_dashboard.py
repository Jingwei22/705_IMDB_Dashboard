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


fig = px.bar(df, x = 'genre', y = 'votes', title = 'Bar Chart for the relationship between genre and votes')
checklist_options = [{'label': genre, 'value':genre} for genre in set(df.genre)]
#print(checklist_options)
fig2 = px.bar(df, x = 'IMDB rating', y = 'movie gross', color = 'year', title = 'Bar Chart for the relationship between IMDB Rating and Movie Gross detailed by year')
fig3 = px.bar(df, x = 'runtime', y = 'movie gross', color = 'IMDB rating', title = 'Bar chart for the relationship between Movie Runtime and Movie Gross detailed by IMDB rating')
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
    dcc.Graph(figure=fig, id='plot'),
    html.Div([html.H4('Genres to Display:'),
              dcc.Checklist(
                  options=checklist_options,
                  value=['Drama', 'Action'],
                  id = 'checklist',style={"width": "20%"})],
             ),    
    dcc.Graph(figure=fig2),
    dcc.Graph(figure=fig3)
    ]
    )

@app.callback(
    Output('plot', 'figure'),
    Input('checklist', 'value'))
def update_plot(value):
    df2 = df[df.genre.isin(value)]
    fig = px.bar(df2, x = 'genre', y = 'votes', title = 'Bar Chart for the relationship between genre and votes')
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)