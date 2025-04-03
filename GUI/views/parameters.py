import flet as ft
from flet_route import Params, Basket
import subprocess


def parameters(page: ft.Page, params: Params, basket: Basket):
    selected_folder_text = ft.Text("")

    def select_folder(e):
        folder = subprocess.run(['zenity', '--file-selection', '--directory'], capture_output=True, text=True).stdout.strip()
        if folder:
            selected_folder_text.value = f"Répertoire sélectionné : {folder}"
            page.update()

    return ft.View(
        "/parameters/",
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
                content=ft.Column(
                    controls=[
                        ft.ElevatedButton(
                            "Sélectionner un répertoire",
                            on_click=select_folder
                        ),
                        selected_folder_text
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
