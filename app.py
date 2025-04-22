import dash
from dash import html, dcc, dash_table
import pandas as pd

# Sample dictionary
data_dict = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 30, 22],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data_dict)

# Initialize Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Data from Dictionary"),
    dash_table.DataTable(
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        style_table={'width': '60%', 'margin': 'auto'},
        style_cell={'textAlign': 'center'}
    )
])

if __name__ == '__main__':
    app.run(debug=True)

