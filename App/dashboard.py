import requests
import pandas as pd
from dash import Dash, dcc, html, Input, Output, State, dash_table
import plotly.express as px

# Initialize Dash app
app = Dash(__name__, suppress_callback_exceptions=True)
app.title = "Enhanced Telegram Messages Dashboard"

# Custom HTML and CSS for styling
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        <title>Telegram Messages Dashboard</title>
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap" rel="stylesheet">
        <style>
            body {
                margin: 0;
                font-family: 'Roboto', sans-serif;
                background-color: #f5f5f5;
            }
            .navbar {
                background-color: #4CAF50;
                padding: 15px;
                color: white;
                text-align: center;
                font-size: 24px;
                font-weight: bold;
            }
            .container {
                max-width: 1200px;
                margin: auto;
                padding: 20px;
            }
            .card {
                background: white;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                padding: 20px;
                margin: 15px 0;
            }
            .btn {
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                font-size: 16px;
                cursor: pointer;
            }
            .btn:hover {
                background-color: #45a049;
            }
            .form-control, .form-select {
                margin-bottom: 10px;
                padding: 10px;
                border-radius: 5px;
                border: 1px solid #ddd;
            }
            .form-label {
                font-weight: bold;
                margin-bottom: 5px;
                display: block;
            }
            .tab-content {
                animation: fadeIn 0.5s;
            }
            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }
            table {
                width: 100%;
                border-collapse: collapse;
            }
            th {
                background-color: #4CAF50;
                color: white;
                text-align: left;
                padding: 10px;
            }
            td {
                padding: 10px;
                border-bottom: 1px solid #ddd;
            }
        </style>
    </head>
    <body>
        <div class="navbar">Telegram Messages Dashboard</div>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

# API Base URL
API_BASE_URL = "http://127.0.0.1:5000"

# App Layout
app.layout = html.Div([
    # Tabs
    dcc.Tabs(
        id="tabs",
        value="view",
        children=[
            dcc.Tab(
                label="View Messages",
                value="view",
                children=[
                    html.Div(
                        className="container",
                        children=[
                            html.Div(
                                className="card",
                                children=[
                                    html.H3("Filter and View Messages", className="text-primary"),
                                    # Filters Section
                                    html.Div(
                                        className="row",
                                        children=[
                                            html.Div(
                                                className="col-md-4",
                                                children=[
                                                    html.Label("Search by Source", className="form-label"),
                                                    dcc.Input(
                                                        id="source-filter",
                                                        type="text",
                                                        placeholder="Enter source...",
                                                        className="form-control"
                                                    ),
                                                ]
                                            ),
                                            html.Div(
                                                className="col-md-4",
                                                children=[
                                                    html.Label("Search by Sender ID", className="form-label"),
                                                    dcc.Input(
                                                        id="sender-filter",
                                                        type="number",
                                                        placeholder="Enter sender ID...",
                                                        className="form-control"
                                                    ),
                                                ]
                                            ),
                                            html.Div(
                                                className="col-md-4",
                                                children=[
                                                    html.Label("Sort by Timestamp", className="form-label"),
                                                    dcc.Dropdown(
                                                        id="sort-filter",
                                                        options=[
                                                            {"label": "Ascending", "value": "asc"},
                                                            {"label": "Descending", "value": "desc"}
                                                        ],
                                                        placeholder="Select sorting order...",
                                                        className="form-select"
                                                    ),
                                                ]
                                            ),
                                        ]
                                    ),
                                    html.Button(
                                        "Apply Filters",
                                        id="filter-button",
                                        n_clicks=0,
                                        className="btn mt-3"
                                    ),
                                ]
                            ),
                            # Data Table
                            html.Div(
                                className="card",
                                children=[
                                    html.H4("Messages Table", className="text-primary"),
                                    dash_table.DataTable(
                                        id="messages-table",
                                        columns=[
                                            {"name": "ID", "id": "id"},
                                            {"name": "Source", "id": "source"},
                                            {"name": "Message", "id": "message"},
                                            {"name": "Sender ID", "id": "sender_id"},
                                            {"name": "Timestamp", "id": "timestamp"},
                                            {"name": "Status Description", "id": "status_description"},
                                        ],
                                        style_table={"overflowX": "auto"},
                                        style_cell={"textAlign": "left", "padding": "10px"},
                                        style_header={"backgroundColor": "#4CAF50", "color": "white"},
                                        page_size=10,
                                        sort_action="native",
                                        filter_action="native",
                                    ),
                                ]
                            ),
                        ]
                    )
                ]
            ),
            dcc.Tab(
                label="Create Message",
                value="create",
                children=[
                    html.Div(
                        className="container",
                        children=[
                            html.Div(
                                className="card",
                                children=[
                                    html.H3("Create a New Message", className="text-primary"),
                                    html.Div(
                                        children=[
                                            html.Label("Source", className="form-label"),
                                            dcc.Input(
                                                id="source-input",
                                                type="text",
                                                placeholder="Enter source...",
                                                className="form-control"
                                            ),
                                            html.Label("Message", className="form-label"),
                                            dcc.Textarea(
                                                id="message-input",
                                                placeholder="Enter message...",
                                                className="form-control"
                                            ),
                                            html.Label("Sender ID", className="form-label"),
                                            dcc.Input(
                                                id="sender-id-input",
                                                type="number",
                                                placeholder="Enter sender ID...",
                                                className="form-control"
                                            ),
                                            html.Label("Timestamp", className="form-label"),
                                            dcc.Input(
                                                id="timestamp-input",
                                                type="text",
                                                placeholder="YYYY-MM-DD HH:MM:SS",
                                                className="form-control"
                                            ),
                                            html.Label("Status Description", className="form-label"),
                                            dcc.Input(
                                                id="status-description-input",
                                                type="text",
                                                placeholder="Enter status description...",
                                                className="form-control"
                                            ),
                                            html.Button(
                                                "Create Message",
                                                id="create-button",
                                                n_clicks=0,
                                                className="btn mt-3"
                                            ),
                                            html.Div(id="create-response", className="mt-3"),
                                        ]
                                    )
                                ]
                            )
                        ]
                    )
                ]
            ),
        ]
    )
])

# Callbacks for filtering messages
@app.callback(
    Output("messages-table", "data"),
    Input("filter-button", "n_clicks"),
    State("source-filter", "value"),
    State("sender-filter", "value"),
    State("sort-filter", "value")
)
def fetch_messages(n_clicks, source, sender_id, sort_order):
    params = {}
    if source:
        params["source"] = source
    if sender_id:
        params["sender_id"] = sender_id

    response = requests.get(f"{API_BASE_URL}/messages/", params=params)
    if response.status_code == 200:
        messages = response.json()
        if sort_order == "asc":
            messages.sort(key=lambda x: x["timestamp"])
        elif sort_order == "desc":
            messages.sort(key=lambda x: x["timestamp"], reverse=True)
        return messages
    return []

# Callback for creating a message
@app.callback(
    Output("create-response", "children"),
    Input("create-button", "n_clicks"),
    State("source-input", "value"),
    State("message-input", "value"),
    State("sender-id-input", "value"),
    State("timestamp-input", "value"),
    State("status-description-input", "value")
)
def create_message(n_clicks, source, message, sender_id, timestamp, status_description):
    if n_clicks > 0:
        payload = {
            "source": source,
            "message": message,
            "sender_id": sender_id,
            "timestamp": timestamp,
            "status_description": status_description,
        }
        response = requests.post(f"{API_BASE_URL}/messages/", json=payload)
        if response.status_code == 201:
            return "✅ Message created successfully!"
        return f"❌ Error: {response.text}"
    return ""

# Run the Dash server
if __name__ == "__main__":
    app.run_server(debug=True)
