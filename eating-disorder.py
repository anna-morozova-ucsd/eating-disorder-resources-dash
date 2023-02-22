import dash
import dash_bootstrap_components as dbc
from dash import html

# Create app instance
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SUPERHERO])

# Define the links to be displayed
links = [
    {'name': 'Free Eating Disorder Support Groups & Services', 'url': 'https://anad.org/'},
    {'name': 'Mental Health Chat Rooms - Peer Support Social Networking', 'url': 'https://www.healthfulchat.org/'},
    {'name': 'Virtual & In-Person Eating Disorder Support Groups', 'url': 'https://centerfordiscovery.com/groups/'},
    {'name': 'How to Help Someone With an Eating Disorder ', 'url': 'https://www.verywellmind.com/how-to-help-someone-with-an-eating-disorder-5088664'},
    {'name': 'Do you have an eating disorder? Questionnaire', 'url': 'https://eatingdisorderfoundation.org/learn-more/about-eating-disorders/questionnaire/'},
    {'name': 'North Carolina Premier Eating Disorder Treatment Center', 'url': 'https://www.carolinaeatingdisorders.com/lp/ed-s-04/?utm_medium=cpc&sf_shortname=digitaledch&utm_campaign=Eating+Disorder+T2&utm_term=eating%20disorder%20services&k_clickid=_k_EAIaIQobChMIlMmk1Z6T_QIV3hbUAR0iVQtnEAAYASAAEgLFlfD_BwE_k_&utm_content=9009970-c-e-444468772021&kpid=go_cmp-9513076302_adg-102285430052_ad-444468772021_kwd-879946643446_dev-c_ext-_sig-EAIaIQobChMIlMmk1Z6T_QIV3hbUAR0iVQtnEAAYASAAEgLFlfD_BwE&utm_source=google-g&utm_id=go_cmp-9513076302_adg-102285430052_ad-444468772021_kwd-879946643446_dev-c_ext-_prd-_mca-_sig-EAIaIQobChMIlMmk1Z6T_QIV3hbUAR0iVQtnEAAYASAAEgLFlfD_BwE&gclid=EAIaIQobChMIlMmk1Z6T_QIV3hbUAR0iVQtnEAAYASAAEgLFlfD_BwE'},
    {'name': 'Diet Culture & Body Liberation Book Collection', 'url': 'https://sfpl.bibliocommons.com/list/share/1528969039/2031115099'},
]

##
list_group = dbc.ListGroup(
    [dbc.ListGroupItem(html.A(link['name'], href=link['url']), action=True) for link in links],
    flush=True,
    style={'margin-bottom': '20px'} 
)
##

# Create layout
app.layout = html.Div(
    dbc.Container(
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            [
                                html.H1('Eating Disorder Resources', className='display-4'),
                                html.Hr(),
                                html.Div(list_group), 
                                html.H5('YOU ARE NOT ALONE.'), 
                                html.H5('There are people who struggle with eating disorders.') ,
                                html.H5('There are people who are willing to help.'),
                                html.H5('Support is vital for recovery.') ,
                                html.H5('There is no shame in seeking for help.') ,
                                html.H5('There is shame in shaming others for doing so.') 
                                        
                            ],
                            className='p-5 bg-light rounded-3',
                            style={'margin': '1px'}, 
                        ),
                    ],
                ),
            ],
            className='mt-5',
            style={'margin': '1px'}, 
        ),
        fluid=True
    
    ), 
)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

