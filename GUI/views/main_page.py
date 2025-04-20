import flet as ft
import os
import json
from flet_route import Params, Basket
  
def main_page(page: ft.Page, params: Params, basket: Basket):
  
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
    music_list = MusicListView(music_files)
  
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
                    ft.Container(
                        margin=10,
                        padding=10,
                        border_radius=10,
                        alignment=ft.alignment.center,
                        bgcolor="#FF69B4",  # Ici se trouve la modification rose flashy
                        width=500,
                        height=600,
                        content=music_list
                    )
                ]
            )
        ]
    )
  
if __name__ == "__main__":
    ft.app(target=main_page)