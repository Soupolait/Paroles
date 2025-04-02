import flet
from flet import (Page, FilePicker, Text,
                  ElevatedButton, Row, FilePickerResultEvent)

def main(page: Page):
    # 2) CREATE THE EVENT FOR FILEPICKER (TO OPEN THE FILEPICKER DIR WINDOW)
    def select_folder(e):
        page.add(filepicker)
        filepicker.pick_files(dialog_title="Select a file to get the folder path...")

    # 3) CREATE THE FUNCTION OF EVENT
    def return_folder(e: FilePickerResultEvent):
        if e.files:
            # Extract the folder path from the file path
            folder_path.value = "/".join(e.files[0].path.split("/")[:-1])
            folder_path.update()

    row_filepicker = Row(vertical_alignment="center")
    folder_path = Text(value="Selected folder path", expand=1)

    # 1) CREATE A FILEPICKER:
    filepicker = FilePicker(on_result=return_folder)

    row_filepicker.controls.append(
        ElevatedButton(
            text="Select folder...", on_click=select_folder))
    # ADD THE PATH (if you will select it)
    row_filepicker.controls.append(
        folder_path)

    page.add(row_filepicker)

if __name__ == '__main__':
    flet.app(target=main)
