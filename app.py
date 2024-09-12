from dash import Dash, html
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.COSMO])

IMAGE = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"
search_bar = dbc.Row(
    [
        dbc.Col(dbc.Input(type="search", placeholder="Search")),
        dbc.Col(
            dbc.Button(
                "Search", color="primary", className="ms-2", n_clicks=0
            ),
            width="auto",
        ),
    ],
    className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)
navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="assets/451420850_6680095385448679_336018023308555072_n.jpg", height="30px")),
                        dbc.Col(dbc.NavbarBrand("Navbar", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="https://plotly.com",
                style={"textDecoration": "none"},
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                search_bar,
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
)

app.layout = html.Div(
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

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050, debug=False)
