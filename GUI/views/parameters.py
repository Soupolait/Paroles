import flet as ft
from flet_route import Params, Basket
from flet import FilePicker, FilePickerResultEvent, Row, Text, ElevatedButton, IconButton, Icons

def parameters(page: ft.Page, params: Params, basket: Basket):
    def select_folder(e):
        page.add(filepicker)
        filepicker.pick_files(dialog_title="Select a file to get the folder path...")

    def return_folder(e: FilePickerResultEvent):
        if e.files:
            folder_path.value = "/".join(e.files[0].path.split("/")[:-1])
            folder_path.update()

    filepicker = FilePicker(on_result=return_folder)
    page.overlay.append(filepicker)
    page.update()
    folder_path = Text(value="Selected folder path", expand=1)

    row_filepicker = Row(
        controls=[
            ElevatedButton(text="Select folder...", on_click=select_folder),
            folder_path
        ],
        vertical_alignment="center"
    )

    return ft.View(
        "/parameters/",
        controls=[
            ft.Row(
                controls=[
                    IconButton(
                        icon=Icons.ARROW_BACK,
                        icon_size=20,
                        on_click=lambda _: page.go("/")
                    )
                ]
            ),
            row_filepicker
        ]
    )

if __name__ == '__main__':
    ft.app(target=parameters)
