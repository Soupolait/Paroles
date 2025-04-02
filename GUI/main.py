import flet as ft
from flet_route import Routing, path
from views.main_page import main_page
from views.parameters import parameters
from views.autre import page2

def main(page: ft.Page):
    
    app_routes = [
        path(url='/', view=main_page, clear=True),
        path(url='/parameters/:my_id', view=parameters, clear=True),
        path(url='/page2/:name', view=page2, clear=True)
    ]

    Routing(page=page, 
            app_routes=app_routes)

    page.go(page.route)

ft.app(target=main)