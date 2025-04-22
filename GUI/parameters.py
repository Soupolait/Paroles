import flet as ft
import json
import os
from flet_route import Params, Basket
from flet import FilePicker, FilePickerResultEvent
import subprocess

selected_folder_path = None
current_dir = os.path.dirname(os.path.abspath(__file__))
parameters_file = os.path.join(current_dir, 'parameters.json')

def parameters(page: ft.Page, params: Params, basket: Basket):
    global parameters_file
    global selected_folder_path
    
    music_folder = ft.Text()

    if os.path.isfile(parameters_file) and os.access(parameters_file, os.R_OK):
        with open(parameters_file) as f:
            data = json.load(f)
            selected_folder_path = data.get('selected_folder', None)
            if selected_folder_path:
                music_folder.value = f"Dossier sélectionné : {selected_folder_path}"
            else:
                music_folder.value = "Aucun dossier sélectionné..."

    file_picker = FilePicker(
        on_result=lambda e: handle_folder_selected(e, music_folder)
    )
    page.overlay.append(file_picker)

    def handle_folder_selected(e: FilePickerResultEvent, text_element: ft.Text):
        global selected_folder_path
        if e.path:
            selected_folder_path = e.path
            text_element.value = f"Dossier sélectionné : {selected_folder_path}"
            with open(parameters_file, 'w') as f:
                json.dump({'selected_folder': selected_folder_path}, f)
            page.update()

    #basket['music_folder'] = music_folder

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
                        music_folder
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