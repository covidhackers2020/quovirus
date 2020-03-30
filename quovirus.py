import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import os

# TRAVEL_STATUS_URL = "https://migration.iom.int/system/tdf/datasets/TRT_%s.xlsx?file=1&type=node&id=8083"
# import requests
# requests.get(TRAVEL_STATUS_URL%'27032020')

restrictions_df = pd.read_excel("data\\travel_restrictions.xlsx")
countries = restrictions_df['RESTRICTED ISO3'].unique()
countries.sort()
countries_df = pd.DataFrame({'ISO':countries})
countries_df['Selected'] = 0
country_names_map = dict(zip([c.upper() for c in restrictions_df['RESTRICTED COUNTRY']],  restrictions_df['RESTRICTED ISO3']))

def select_base_iso(base_iso):
    # base_iso = 'USA'
    restricted = restrictions_df[restrictions_df['IMPLEMENTING ISO3'] == base_iso]
    restricted_iso = restricted['RESTRICTED ISO3'].unique()
    
    countries_df['Selected'] = 'Normal'
    countries_df.loc[countries_df['ISO'] == base_iso, 'Selected'] = 'Base'#base_iso
    countries_df.loc[countries_df['ISO'].isin(restricted_iso), 'Selected'] = 'Restricted'
    return countries_df

app = dash.Dash(__name__, url_base_pathname='/quovirus/')
app.title = 'QuoVirus'
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True
server = app.server

app.layout = html.Div([
    html.Img(src=app.get_asset_url('banner-desktop.png')),
    # html.Div([dcc.])
    html.Div([dcc.Dropdown(id='country-select', 
                            options=[{'label': k, 'value': v} for k,v in country_names_map.items()],
                            value='USA', 
                            style={'width': '100%',
                            'fontSize' : 24,
                            
                            })]),
    dcc.Graph('travel-map-graph',
                className="map-central",
                config={'displayModeBar': False})
    ], className="embed-responsive"
    )

@app.callback(
    Output('travel-map-graph', 'figure'),
    [Input('country-select', 'value')]
)

def update_graph(base_iso):
    select_base_iso(base_iso)

    return px.choropleth(countries_df, 
            locations="ISO", 
            color="Selected",
            color_discrete_map={
                "Restricted": "red",
                "Normal": "green",
                "Base": "blue"})#,
            # title="Travel Restrictions")
    

if __name__ == '__main__':
    app.run_server()#debug=False)#, port=8888)


    
