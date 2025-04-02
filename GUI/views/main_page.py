import flet as ft
from flet_route import Params, Basket

def main_page(page: ft.Page, params: Params, basket: Basket):

    return ft.View(
        '/',
        controls = [
            ft.Text("La discothèque apparaîtra ici !"),
            ft.ElevatedButton("Paramètres", on_click= lambda _: page.go("/parameters/10")),
            ft.ElevatedButton("Kécecé", on_click= lambda _: page.go("/page2/TEST")),
        ]
    )