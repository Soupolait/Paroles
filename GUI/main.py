import flet as ft
from flet_route import Routing, path
from views.main_page import main_page
from views.parameters import parameters

def main(page: ft.Page):
    page.title = "Paroles"

    app_routes = [
        path(url='/', view=main_page, clear=True),
        path(url='/parameters/', view=parameters, clear=True)
    ]
    
    Routing(page=page, 
            app_routes=app_routes)

    page.go(page.route)

ft.app(main)