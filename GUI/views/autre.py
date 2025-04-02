import flet as ft
from flet_route import Params, Basket

def page2(page: ft.Page, params: Params, basket: Basket):
    return ft.View(
        "/page2/",

        controls = [
            ft.Text("Et voici une page test !"),
            ft.ElevatedButton('Retour', on_click= lambda _: page.go("/"))
        ]
    )