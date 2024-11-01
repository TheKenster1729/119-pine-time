from dash import Dash, html, Input, Output, State
import dash_bootstrap_components as dbc
from utilities import LLM, PersonalityComparison
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

picture_carousel = dbc.Carousel(
    items = [
        {
            "key": "1",
            "src": "static/PXL_20241010_231937688.jpg",
            "caption": "10/10/24 \"He's not here anymore. But he is!\"",
            "captionClassName": "custom-caption"
        },
        {
            "key": "2",
            "src": "static/1000002126.jpg",
            "caption": "10/8/24 FORTNITE WITH THE BOIS",
            "captionClassName": "custom-caption"
        },
        {
            "key": "3",
            "src": "static/PXL_20241005_192516555.MP.jpg",
            "caption": "10/5/24 \"You guys make me feel like I'm in middle school again, but in the best way possible.\"",
            "captionClassName": "custom-caption"
        },
        {
            "key": "4",
            "src": "static/461782042_535447332535753_319487368229332895_n (1).jpeg",
            "caption": "10/8/24 \"unpacking\"",
            "captionClassName": "custom-caption"
        },
        {
            "key": "5",
            "src": "static/PXL_20240904_020345160.MP.jpeg",
            "caption": "9/10/24 \"Will, you're a genius\"",
            "captionClassName": "custom-caption"
        },
        {
            "key": "6",
            "src": "static/462535596_401185803041877_6676071688399128015_n.jpg",
            "caption": "10/8/24 \"Kamala Harris would be 2x\"",
            "captionClassName": "custom-caption"
        },
        {
            "key": "7",
            "src": "static/462539491_1251023609433769_6766252311625364834_n.jpg",
            "caption": "10/24/24 \"For two seconds I thought he was dead\"",
            "captionClassName": "custom-caption"
        },
        {
            "key": "8",
            "src": "static/451420850_6680095385448679_336018023308555072_n.jpg",
            "caption": "7/23/24 \"This is a pretty significant cultural representation for Oklahoma\"",
            "captionClassName": "custom-caption"
        },
        {
            "key": "9",
            "src": "static/e0470955-7233-4106-9a43-7221fda68b45.jpeg",
            "caption": "5/17/24 🤓",
            "captionClassName": "custom-caption"
        },
        {
            "key": "10",
            "src": "static/394235035_844388500670304_7945824688703275233_n.jpg",
            "caption": "10/19/23 Homeless man off his meds celebrates The Eras Tour, 2023 colorized",
            "captionClassName": "custom-caption"
        }
    ],
    interval = 10000
)

homepage_layout = html.Div(
    [
        navbar,
        dbc.Row(
            children = [
                dbc.Col(width = 6,
                    children = [
                        html.H1("Welcome home.", style={"margin": "50px"}),
                    ]
                ),
                dbc.Col(width = 6,
                    style = {"display": "flex", "justifyContent": "flex-end"},
                    children = [
                        html.Img(src="static/Flag_of_Mexico.svg.png", height = "100px"),
                        html.Img(src="static/Flag_of_the_United_States.svg.png", height = "100px")
                    ]
                )
            ]
        ),
        html.P("This is the home page of 119 Pine Street #1. 很高兴认识你!", style={"marginLeft": "50px"}),
        dbc.Row(
            children = [
                dbc.Col(
                    children = [
                        html.H4("Meet the crew", style={"marginLeft": "50px"}),
                        dbc.Accordion(start_collapsed=True, style={"marginLeft": "50px"}, children=[
                        dbc.AccordionItem(title = "RCO Speedwagon (Ruben)", children = [
                            html.Div(
                                children = [
                                    dbc.Row(
                                        children = [
                                            dbc.Col(width = 4,
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
                                            dbc.Col(width = 4,
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
                                            dbc.Col(width = 4,
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
                    ],
                    width = 5
                ),
                dbc.Col(
                    children = [
                        html.H4("adventuring"),
                        picture_carousel
                    ],
                    width = 4
                )
                    
            ]
        ),
        dbc.Row(
            children = [
                html.Div(style = {"margin": "50px"},
                    children = [
                        html.H4("Find your bestie"),
                        html.A("Take this test to find which of us you are most similar to", href="https://bigfive-test.com/"),
                        dbc.Row(
                            children = [
                                dbc.Col(width = 3,
                                    children = [
                                        dbc.Input(id="neuroticism-input", type="number", placeholder="Enter neuroticism score")
                                    ]
                                )
                            ]
                        ),
                        dbc.Row(
                            children = [
                                dbc.Col(width = 3,
                                    children = [
                                        dbc.Input(id="extraversion-input", type="number", placeholder="Enter extraversion score")
                                    ]
                                )
                            ]
                        ),
                        dbc.Row(
                            children = [
                                dbc.Col(width = 3,
                                    children = [
                                        dbc.Input(id="openness-input", type="number", placeholder="Enter openness score")
                                    ]
                                )
                            ]
                        ),
                        dbc.Row(
                            children = [
                                dbc.Col(width = 3,
                                    children = [
                                        dbc.Input(id="agreeableness-input", type="number", placeholder="Enter agreeableness score")
                                    ]
                                )
                            ]
                        ),
                        dbc.Row(
                            children = [
                                dbc.Col(width = 3,
                                    children = [
                                        dbc.Input(id="conscientiousness-input", type="number", placeholder="Enter conscientiousness score")
                                    ]
                                )
                            ]
                        ),
                        dbc.Button("Find your bestie", id="find-button", n_clicks=0, color="primary", style={"marginTop": "20px"}),
                        html.Div(id="bestie-result")
                    ]
                )
            ]
        )
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

@app.callback(
    Output('bestie-result', 'children'),
    Input('find-button', 'n_clicks'),
    State('neuroticism-input', 'value'),
    State('extraversion-input', 'value'),
    State('openness-input', 'value'),
    State('agreeableness-input', 'value'),
    State('conscientiousness-input', 'value'),
)
def find_bestie(n_clicks, neuroticism, extraversion, openness, agreeableness, conscientiousness):
    if n_clicks > 0:
        bestie = PersonalityComparison(1).find_nearest_neighbors([neuroticism, extraversion, openness, agreeableness, conscientiousness])
        return html.H3(bestie)
    return ''

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050)