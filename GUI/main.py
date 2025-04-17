import flet as ft
import json
import os
from flet_route import Routing, path
from views.main_page import main_page
from views.parameters import parameters

def main(page: ft.Page):

    def parameters_check():
        PATH = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(PATH, 'parameters.json')

        if os.path.isfile(file_path) and os.access(file_path, os.R_OK):
            pass
        else:
            with open(os.path.join(PATH, 'parameters.json'), 'w') as db_file:
                db_file.write(json.dumps({}))

    parameters_check()

    page.title = "Paroles"

    app_routes = [
        path(url='/', view=main_page, clear=True),
        path(url='/parameters/', view=parameters, clear=True)
    ]
    
    Routing(page=page, 
            app_routes=app_routes)

    page.go(page.route)

ft.app(main)