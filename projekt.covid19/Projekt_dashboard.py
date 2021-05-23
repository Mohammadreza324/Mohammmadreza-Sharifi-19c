import plotly.express as px
import dash 
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np 



app = dash.dash(__name__)
#Genenera mockup data 

#skapa fig 
fig = px.bar() 

app.layout = HTML.Div(children=[
    HTML.H1(children="antal fall"),

    dcc.Dropdown(
        id="",
        options = [dict(label= "",value= ""),dict(label= "",value= "")],
        value=
    ),

    dcc.Graph(
        id="",
        figure = fig
    )
])

@app.callback(
    output("graph". "figure"),
    [input("drop","value")]
)

def uppdate_figure(value):
    if value == "": df = #datan
    elif values == "": df = 

    fig = px.bar()
    fig.uppdate_layout(transitioin_duration = 500)
    return fig 


if __name__ == "__main__":
    app.run_server(debug = True)
