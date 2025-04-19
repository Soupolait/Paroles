import os
import json
import flet as ft

class MusicListView(ft.ListView):
    def __init__(self, music_files: list[str]):
        super().__init__(
            expand=True,
            spacing=10,
            padding=20,
            build_controls_on_demand=True
        )
        for name in music_files:
            self.controls.append(ft.Text(name))

def which_music(music_folder):
    music_files = []
    if os.path.isdir(music_folder) and os.access(music_folder, os.R_OK):
        for root, dirs, files in os.walk(music_folder):
            for file in files:
                if file.endswith(('.mp3', '.flac', '.wav', '.ogg')):
                    music_files.append(file)
    return music_files

def main(page: ft.Page):
    page.title = "Music File List"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    music_folder = "/home/loic/Musiques"
    music_files = which_music(music_folder)
    music_list_view = MusicListView(music_files=music_files)

    def show_music_list(e):
        page.controls.clear()
        page.controls.append(music_list_view)
        page.update()

    page.add(
        ft.ElevatedButton(
            text="Show Music Files",
            on_click=lambda _: music_list_view
        )
    )

# Lancer l'application
ft.app(target=main)
