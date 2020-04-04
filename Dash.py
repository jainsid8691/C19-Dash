
import pandas as pd
url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
df = pd.read_csv(url, sep=',', error_bad_lines=False)


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import plotly.graph_objs as go


# Step 1. Launch the application
app = dash.Dash()
#%%

df1_date = df.groupby('date', as_index=False)[['cases']].sum()
df1_date
df1_date_March10 = df1_date[df1_date['date'] > '2020-03-10']

#%%

trace_1 = go.Scatter(x = df1_date_March10.date, y = df1_date_March10.cases,
                     name = 'Total COVID19 Cases',
                    line = dict(width = 2,
                                color = 'rgb(229, 151, 50)'))
layout = go.Layout(title = 'COVID19 Cases',
                   hovermode = 'closest')
fig = go.Figure(data = [trace_1], layout = layout)


#%%

# Step 4. Create a Dash layout
app.layout = html.Div([
                dcc.Graph(id = 'plot', figure = fig)
                      ])
# Step 6. Add the server clause
if __name__ == '__main__':
    app.run_server(debug = True)



#%%

