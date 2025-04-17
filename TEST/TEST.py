import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Directory_Holder:
    def __init__(self):
        dialog = Gtk.FileChooserDialog(
        title="Select folder", parent=None, action=Gtk.FileChooserAction.SELECT_FOLDER
    )
        dialog.add_button("Cancel", Gtk.ResponseType.CANCEL)
        dialog.add_button("Select", Gtk.ResponseType.OK)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            self.directory = dialog.get_filename()

        dialog.destroy()
            
get_directory = Directory_Holder()
print(get_directory.directory)


#CODE AVEC CLASS
import flet as ft
from flet_route import Params, Basket
import subprocess
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

def parameters(page: ft.Page, params: Params, basket: Basket):

    class Directory_Holder:
        def __init__(self):
            dialog = Gtk.FileChooserDialog(
            title="Select folder", parent=None, action=Gtk.FileChooserAction.SELECT_FOLDER
        )
            dialog.add_button("Cancel", Gtk.ResponseType.CANCEL)
            dialog.add_button("Select", Gtk.ResponseType.OK)

            response = dialog.run()
            if response == Gtk.ResponseType.OK:
                self.directory = dialog.get_filename()

            dialog.destroy()
            
    get_directory = Directory_Holder()

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
                            on_click=get_directory
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
