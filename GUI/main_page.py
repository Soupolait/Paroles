import flet as ft
import os
import json
from flet_route import Params, Basket
from API.API import API

class MusicListView(ft.ListView):
    def __init__(self, music_files: list[str]):
        super().__init__(
            expand=True,
            spacing=10,
            padding=20,
            build_controls_on_demand=True
        )

        for name in music_files:
            self.controls.append(ft.Text('- ' + name))

def which_music():
    parameters_file = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(__file__)))), 'parameters.json')
    music_folder = None
    music_files = []

    if os.path.isfile(parameters_file) and os.access(parameters_file, os.R_OK):
        with open(parameters_file) as f:
            data = json.load(f)
            music_folder = data.get('selected_folder', None)
        if music_folder:
            for root, dirs, files in os.walk(music_folder):
                for file in files:
                    if file.endswith(('.mp3', '.flac', '.wav', '.ogg')):
                        music_files.append(file)
    return music_files

def get_LRC(e):
    global music_files, music_folder
    for fichier in music_files:
        print(fichier)
        full_path = os.path.join(music_folder, fichier)
        API(full_path)

def main_page(page: ft.Page, params: Params, basket: Basket):
    # Déplacer l'initialisation de music_files et music_list ici
    music_files = which_music()
    music_list = MusicListView(music_files)

    def update_music_list():
        nonlocal music_files, music_list
        music_files = which_music()
        music_list = MusicListView(music_files)
        container.content = music_list
        page.update()

    container = ft.Container(
        margin=10,
        padding=10,
        border_radius=10,
        alignment=ft.alignment.center,
        bgcolor="#FF69B4",
        width=500,
        height=600,
        content=music_list
    )

    return ft.View(
        "/",
        bgcolor='#FFFFFF',
        controls=[
            ft.Row(
                controls=[
                    ft.Container(expand=True),
                    ft.IconButton(
                        icon=ft.icons.SETTINGS,
                        icon_size=20,
                        on_click=lambda _: page.go('/parameters/')
                    ),
                ],
            ),
            ft.Row(
                expand=True,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.ElevatedButton(
                        "Rechercher des paroles",
                        on_click=get_LRC
                    ),
                    container
                ]
            )
        ]
    )

if __name__ == "__main__":
    ft.app(target=main_page)
