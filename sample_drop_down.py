import flet as ft

def main(page: ft.Page):
    page.title = "Clear Dropdown Example"

    # Container to hold dropdown (so we can replace it)
    dropdown_container = ft.Container()

    def build_dropdown():
        return ft.Dropdown(
            label="Select a fruit",
            width=200,
            options=[
                ft.dropdown.Option("Apple"),
                ft.dropdown.Option("Orange"),
                ft.dropdown.Option("Banana"),
            ],
        )

    dropdown = build_dropdown()
    dropdown_container.content = dropdown

    def clear_dropdown(e):
        nonlocal dropdown
        dropdown = build_dropdown()  # create a new dropdown instance
        dropdown_container.content = dropdown
        page.update()

    clear_button = ft.ElevatedButton(
        text="Clear Selection",
        on_click=clear_dropdown
    )

    page.add(
        ft.Text("Dropdown Value:"),
        dropdown_container,
        clear_button
    )

ft.app(target=main)
