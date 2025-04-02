import flet as ft
from flet_route import Params, Basket

def parameters(page: ft.Page, params: Params, basket: Basket):
    
    return ft.View(
        "/parameters/:my_id",

        controls = [
            ft.Text("Ice siègeront les paramètres"),
            ft.ElevatedButton('Retour', on_click= lambda _: page.go("/"))
        ]
    )