import flet as ft
from flet_route import Params, Basket

def main_page(page: ft.Page, params: Params, basket: Basket):
    return ft.View(
        "/",
        controls=[
            ft.Row(
                controls=[ #Bouton paramètres
                    ft.Container(expand=True),
                    ft.IconButton(
                        icon=ft.Icons.SETTINGS, 
                        icon_size=20, 
                        on_click=lambda _: page.go('/parameters/')
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            ft.Text("La discothèque apparaîtra ici !"),
            ft.ElevatedButton("Kécecé", on_click=lambda _: page.go("/page2/")),
        ]
    )
