from dash import Dash, html, Input, Output, State
import dash_bootstrap_components as dbc
from utilities import LLM
from dash import dcc

app = Dash(__name__, external_stylesheets=[dbc.themes.COSMO], suppress_callback_exceptions=True)

search_bar = dbc.Row(
    [
        dbc.Col(
            dbc.Input(id="ask-input", type="text", placeholder="Ask a question"),
            width=12,
        ),
        dbc.Col(
            dbc.Button(
                "Ask", color="primary", className="ms-2", n_clicks=0, id="ask-button"
            ),
            width=2,
        ),
    ],
    className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
    align="center",
    style={"width": "100%"},
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        html.A(
                            dbc.Row(
                                [
                                    dbc.Col(html.Img(src="assets/451420850_6680095385448679_336018023308555072_n.jpg", height="30px")),
                                    dbc.Col(dbc.NavbarBrand("Try out the search bar!", className="ms-2")),
                                ],
                                align="center",
                                className="g-0",
                            ),
                            href="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                            style={"textDecoration": "none"},
                        ),
                        width="auto",
                    ),
                    dbc.Col(width=True),  # This empty column will push the search bar to the right
                    dbc.Col(
                        search_bar,
                        width=True,
                        style={"marginRight": "100px"},  # Add right margin
                    ),
                ],
                align="center",
                className="g-0 w-100",
            ),
        ],
        fluid=True,
    ),
    color="dark",
    dark=True,
)

homepage_layout = html.Div(
    [
        navbar,
        html.H1("Welcome home.", style={"margin": "50px"}),
        html.P("This is the home page of 119 Pine Street #1. 很高兴认识你!", style={"marginLeft": "50px"}),
        dbc.Accordion(start_collapsed=True, style={"marginLeft": "50px", "width": "50%"}, children=[
            dbc.AccordionItem(title = "RCO Speedwagon (Ruben)", children = [
                html.Div(
                    children = [
                        dbc.Row(
                            children = [
                                dbc.Col(width = 3,
                                    children = [
                                        html.Img(src="assets/Screenshot 2024-09-12.png", height = "100px"),
                                    ]
                                ),
                                dbc.Col(
                                    children = [
                                        """Resident CEO and captain of indecision.""",
                                        html.Br(),
                                        html.Br(),
                                        """Core strengths:
                                        Domino's at 12 am, saving money in unexpected places, motivating trips to
                                        new bars."""
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]),
            dbc.AccordionItem(title = "warcher (Will)", children = [
                html.Div(
                    children = [
                        dbc.Row(
                            children = [
                                dbc.Col(width = 3,
                                    children = [
                                        html.Img(src="assets/1CE4703E-4FDD-4552-A168-D0B9407C48CA_1_201_a.jpeg", height = "100px"),
                                    ]
                                ),
                                dbc.Col(
                                    children = [
                                        """
                                        Most alive in an election year and when OKC are in the playoffs.
                                        Both at the same time might result in a dopamine regulation disorder.""",
                                        html.Br(),
                                        html.Br(),
                                        """Core strengths:
                                        concert connoisseur, maintaining Duolingo presence, being Oklahoman.
                                        """
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]),
            dbc.AccordionItem(title = "Kenneth Sucks Cox (Kenny)", children = [
                html.Div(
                    children = [
                        dbc.Row(
                            children = [
                                dbc.Col(width = 3,
                                    children = [
                                        html.Img(src="assets/Screenshot 2024-09-12-kenny.png", height = "100px"),
                                    ]
                                ),
                                dbc.Col(
                                    children = [
                                        "'What a waste of a habitable planet!'",
                                        html.Br(),
                                        html.Br(),
                                        """Core strengths:
                                        metaphysics, strategic nuclear response options, time-consuming ideas.
                                        """
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ])
        ])
    ]
)

app.layout = html.Div([
    dcc.Location(id="url", refresh=False),
    html.Div(id="page-content")
])

# Results page layout
def results_layout(search_query):
    response = LLM("EleutherAI/gpt-neo-125m").generate(search_query)
    return html.Div([
        html.H2('Search Results'),
        dcc.Input(id='search-bar-results', type='text', value=search_query, placeholder='Enter a new search query...'),
        html.Button('Search', id='search-button-results', n_clicks=0),
        html.Div(f'Search Results for: {search_query}'),
        # Display search results here (this can be populated with dynamic data)
        html.Div(id='search-results-content', children = [
            html.Div(children = [
                html.P(response)
            ])
        ])
    ])

# Callback to control the page content
@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'),
              Input('url', 'search'))
def display_page(pathname, search):
    if pathname == '/results':
        search_query = search.split('=')[1] if search else ''
        return results_layout(search_query)
    else:
        return homepage_layout

# Callback to handle the search button click on the homepage
@app.callback(
    Output('url', 'pathname'),
    Output('url', 'search'),
    Input('ask-button', 'n_clicks'),
    State('ask-input', 'value'),
    prevent_initial_call=True
)
def redirect_to_results(n_clicks, search_query):
    if n_clicks > 0 and search_query:
        return '/results', f'?query={search_query}'
    return '/', ''  # If there's no valid search query, return to the homepage

# Callback to handle the search button click on the results page
@app.callback(
    Output('search-results-content', 'children'),
    Input('search-button-results', 'n_clicks'),
    State('search-bar-results', 'value'),
    prevent_initial_call=True
)
def update_search_results(n_clicks, search_query):
    if n_clicks > 0 and search_query:
        # You can add logic to fetch and display search results based on the query
        return f'Displaying search results for: {search_query}'
    return 'No search results.'

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050, debug=True)
