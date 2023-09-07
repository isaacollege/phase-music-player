import typing
import flet as ft


class AudioControls:
    def __init__(self, page: ft.Page):
        self.page = page
        self.audio: typing.Optional[ft.Audio] = None

        self.shuffle_button = ft.IconButton(ft.icons.SHUFFLE_ROUNDED, on_click=self._shuffle)
        self.repeat_button = ft.IconButton(ft.icons.REPEAT_ROUNDED)

        self.shuffled = False

        self.content = ft.Row(
            controls=[
                ft.Container(expand=1, bgcolor="red"),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Container(expand=1),
                            ft.Container(
                                content=ft.Row(
                                    controls=[
                                        ft.Container(expand=True),
                                        ft.Container(
                                            content=ft.Row(
                                                controls=[
                                                    self.shuffle_button,
                                                    ft.IconButton(
                                                        ft.icons.FAST_REWIND_ROUNDED
                                                    ),
                                                    ft.IconButton(
                                                        ft.icons.PLAY_ARROW_ROUNDED,
                                                        icon_size=30,
                                                    ),
                                                    ft.IconButton(
                                                        ft.icons.FAST_FORWARD_ROUNDED
                                                    ),
                                                    self.repeat_button,
                                                ],
                                            ),
                                            border_radius=ft.border_radius.all(15),
                                        ),
                                        ft.Container(expand=True),
                                    ],
                                ),
                                expand=4,
                            ),
                            ft.Container(
                                content=ft.Row(
                                    controls=[
                                        ft.Text(
                                            "00:00",
                                            expand=1,
                                            text_align=ft.TextAlign.RIGHT,
                                        ),
                                        ft.Slider(
                                            expand=4,
                                            inactive_color=ft.colors.OUTLINE_VARIANT,
                                        ),
                                        ft.Text("03:22", expand=1),
                                    ]
                                ),
                                expand=3,
                            ),
                        ],
                        spacing=0,
                    ),
                    expand=2,
                ),
                ft.Container(expand=1, bgcolor="blue"),
            ],
            expand=True,
            spacing=15,
        )

    def _shuffle(self, e: ft.ControlEvent):
        if self.shuffled:
            self.shuffled = False
            self.shuffle_button.icon = ft.icons.SHUFFLE_ROUNDED
        else:
            self.shuffled = True
            self.shuffle_button.icon = ft.icons.SHUFFLE_ON_ROUNDED

        self.page.update(self.shuffle_button)