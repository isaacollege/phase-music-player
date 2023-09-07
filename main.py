import flet as ft
from controls import AudioControls


def main(page: ft.Page):
    page.title = "Phase" # Sets the app's window's title
    page.theme_mode = ft.ThemeMode.LIGHT
    # page.theme = ft.Theme(color_scheme_seed=ft.colors.TEAL)


    controls = AudioControls(page)


    navarea = ft.Container(
        bgcolor=ft.colors.SURFACE_VARIANT,
        expand=1,
        border_radius=ft.border_radius.all(15),
    )

    libraryarea = ft.Container(
        bgcolor=ft.colors.SURFACE_VARIANT,
        expand=3,
        border_radius=ft.border_radius.all(15),
    )

    mainarea = ft.Container(
        bgcolor=ft.colors.SURFACE_VARIANT,
        expand=True,
        border_radius=ft.border_radius.all(15),
    )

    controlsarea = ft.Container(
        content=controls.content,
        bgcolor=ft.colors.SURFACE_VARIANT,
        expand=True,
        border_radius=ft.border_radius.all(15),
    )

    container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Column(
                            controls=[
                                navarea,
                                libraryarea,
                            ],
                            expand=1,
                            spacing=15,
                        ),
                        ft.Column(
                            controls=[mainarea],
                            expand=4,
                        ),
                    ],
                    expand=5,
                    spacing=15,
                ),
                ft.Row(
                    controls=[controlsarea],
                    expand=1,
                ),
            ],
            spacing=15,
        ),
        expand=True,
    )

    page.add(container)

ft.app(target=main, name="Phase")
