import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash.dependencies import Input, Output

electricity_csv = pd.read_csv('electricity.csv')
year_min = electricity_csv['Year'].min()
year_max = electricity_csv['Year'].max()
avg_price_electricity = electricity_csv.groupby('US_State')['Residential Price'].mean().reset_index()
map_figure = px.choropleth(avg_price_electricity,
                           locations='US_State',
                           locationmode='USA-states',
                           color='US_State',
                           scope='usa',
                           color_continuous_scale='blues')

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div([
    html.H1("SDC Sales per US state"),
    dcc.RangeSlider(
        id='year_slider',
        min=year_min,
        max=year_max,
        value=[year_min, year_max],
        marks={i: str(i) for i in range(year_min, year_max + 1)}),
    dbc.Row([
        dcc.Graph(id='bar_plot'),
        dcc.Graph(id='map-graph', figure=map_figure),
    ]),
    html.Div(id='sample_div'),
    dash_table.DataTable(id='price_info',
                         columns=[{'name': col, 'id': col} for col in electricity_csv.columns],
                         data=electricity_csv.to_dict('records')
                         )
])


@app.callback(
    Output('map-graph', 'figure'),
    Input('year_slider', 'value')
)
def updated_rangeslider(input_year_slider):
    filter_electricity = electricity_csv[(electricity_csv['Year'] >= input_year_slider[0]) &
                                         (electricity_csv['Year'] <= input_year_slider[1])]

    avg_price_electricity = filter_electricity.groupby('US_State')['Residential Price'].mean().reset_index()
    map_figure = px.choropleth(avg_price_electricity,
                               locations='US_State',
                               locationmode='USA-states',
                               color='Residential Price',
                               scope='usa',
                               color_continuous_scale='purples')
    return map_figure


@app.callback(
    Output('price_info', 'data'),
    Output('bar_plot', 'figure'),
    Input('map-graph', 'clickData'),  # Input component property is click data.
    Input('year_slider', 'value')

)
def update_data_table_when_clicked_on_map(click_data, input_year_slider):
    if click_data is None:
        return [], bar_fig([], [])
    us_state = click_data['points'][0]['location']
    records = electricity_csv[(electricity_csv['US_State'] == us_state) &
                              (electricity_csv['Year'] >= input_year_slider[0]) &
                              (electricity_csv['Year'] <= input_year_slider[1])
                              ]
    records_to_dict = records.to_dict('records')
    avg_price_electricity_state = electricity_csv[electricity_csv['US_State'] == us_state].reset_index()
    get_res_value_year = avg_price_electricity_state[(avg_price_electricity_state['Year'] >= input_year_slider[0]) &
                                                     (avg_price_electricity_state['Year'] <= input_year_slider[1])]
    get_years = list(get_res_value_year['Year'])
    res_price_list = list(get_res_value_year['Residential Price'])
    bar_figure = bar_fig(y_cordinate=res_price_list, x_cordinate=get_years, state=us_state)
    return records_to_dict, bar_figure


def bar_fig(x_cordinate=[], y_cordinate=[], state="."):
    bar_figure = go.Figure(
        data=[go.Bar(y=y_cordinate, x=x_cordinate)],
        layout_title_text=f"Bar Char for the state {state}"
    )
    return bar_figure


if __name__ == '__main__':
    app.run_server(debug=True)
