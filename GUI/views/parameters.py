import flet as ft
from flet_route import Params, Basket
from flet import (Page, FilePicker, Text,
                  ElevatedButton, Row, Column, FilePickerResultEvent)
import subprocess

def parameters(page: ft.Page, params: Params, basket: Basket):

    return ft.View(
        "/parameters/",
        bgcolor='#FFFFFF',
        controls=[
            ft.Row(
                controls=[
                    ft.IconButton(
                        icon=ft.icons.ARROW_BACK,
                        icon_size=20,
                        on_click=lambda _: page.go("/")
                    )
                ],
                alignment=ft.MainAxisAlignment.START
            ),
            ft.Container(  # Conteneur qui centre la colonne
                #bgcolor=ft.Colors.YELLOW, UTILE POUR VOIR LA ZONE DU CONTENEUR
                content=ft.Column(
                    controls=[
                        ft.ElevatedButton(
                            "Sélectionner un répertoire",
                            on_click=lambda _: select_folder
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                alignment=ft.alignment.center,  # Centre tout le contenu
                expand=True  # Fait en sorte que le container prenne tout l'espace
            )
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER  # Centre tout le contenu verticalement
    )