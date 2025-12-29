import flet as ft

def main(page: ft.Page):
    def reset_dropdown_value(e):
        dropdown.value = "default"
        dropdown.update()

    dropdown = ft.Dropdown(
        label="Examples",
        options=[
            ft.DropdownOption(text="Select an option...", key="default", disabled=True),
            ft.DropdownOption(text="Option 1", key="opt1"),
            ft.DropdownOption(text="Option 2", key="opt2"),
        ],
    )

    page.add(
        dropdown,
        ft.ElevatedButton(text="Reset Dropdown", on_click=reset_dropdown_value)
    )

    reset_dropdown_value(None)

ft.app(target=main)
