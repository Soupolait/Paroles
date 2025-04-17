import flet as ft
from flet_route import Params, Basket
from flet import FilePicker, FilePickerResultEvent
import subprocess

selected_folder_path = None

def parameters(page: ft.Page, params: Params, basket: Basket):
    global selected_folder_path

    folder_text = ft.Text(value="Aucun dossier sélectionné.")

    file_picker = FilePicker(
        on_result=lambda e: handle_folder_selected(e, folder_text)
    )
    page.overlay.append(file_picker)

    def handle_folder_selected(e: FilePickerResultEvent, text_element: ft.Text):
        global selected_folder_path
        if e.path:
            selected_folder_path = e.path
            text_element.value = f"Dossier sélectionné : {selected_folder_path}"
            page.update()


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
                            on_click=lambda _: file_picker.get_directory_path()
                        ),
                        folder_text
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