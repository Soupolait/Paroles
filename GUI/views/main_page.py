import flet as ft
import os
import json
from flet_route import Params, Basket

class MusicListView(ft.ListView):
    def __init__(self, music_files: list[str]):
        """
        Initializes the MusicListView.
        Args:
            music_files: A list of strings, where each string is a music file name.
        """ 
        super().__init__( # Call the constructor of the parent class (ft.ListView)
            expand=True,  # allows the ListView to fill available vertical space, enabling scrolling
            spacing=10, # vertical space between list items
            padding=20, # space around the entire list content
            build_controls_on_demand=True # keeps long lists performant
        )

        for name in music_files: 
            self.controls.append(ft.Text(name))

    def which_music(): # finding music files, adding them to the list
        current_dir = os.path.dirname(os.path.abspath(__file__))
        root_dir = os.path.dirname(current_dir)
        parameters_file = os.path.join(root_dir, 'parameters.json')
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

    music_files = which_music()

def main_page(page: ft.Page, params: Params, basket: Basket):

    return ft.View(
        "/",
        bgcolor='#FFFFFF',
        controls=[
            ft.Row(
                controls=[
                    ft.Container(expand=True),
                    ft.IconButton(
                        icon=ft.Icons.SETTINGS,
                        icon_size=20,
                        on_click=lambda _: page.go('/parameters/')
                    ),
                    ft.ElevatedButton(
                        "TEST",
                        on_click = MusicListView(music_files=music_files)
                    )   
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            )
        ]
    )

if __name__ == "__main__":
    ft.app(target=main_page)