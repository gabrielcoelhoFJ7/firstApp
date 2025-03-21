import flet as ft
from flet.core.textfield import TextField


def main(page: ft.Page):
    # Configuração da página
    page.title = "Minha Aplicação Flet"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.LIGHT
    page.window.width = 375
    page.window.height = 667
    page.theme = ft.Theme(font_family="Kanit")  # Default app font

    # Definição de funções
    def mostrar_multi(e):
        try:
            result.value = (int(input_num1.value) * int(input_num2.value))
        except ValueError:
            result.value = 0
        page.update()

    def mostrar_div(e):
        try:
            result.value = int(input_num1.value) / int(input_num2.value)
        except ValueError:
            result.value = 0
        page.update()

    def mostrar_adi(e):
        try:
            result.value = int(input_num1.value) + int(input_num2.value)
        except ValueError:
            result.value = 0
        page.update()

    def mostrar_sub(e):
        try:
            result.value = int(input_num1.value) - int(input_num2.value)
        except ValueError:
            result.value = 0
        page.update()

    # Criação de componentes
    text_num1 = ft.Text(value="Nome:")
    input_num1 = ft.TextField(label="Digite aqui", hint_text="Insira o nome")
    text_num2 = ft.Text(value="Sobrenome:")
    input_num2 = ft.TextField(label="Digite aqui", hint_text="Insira o sobrenome")
    result = ft.Text(value="0", color=ft.colors.WHITE, size=20)
    submit_adi = ft.FilledButton(
        text="Adição",
        width=page.window.width,
        on_click=mostrar_adi,
    )
    submit_multi = ft.FilledButton(
        text="Multiplicação",
        width=page.window.width,
        on_click=mostrar_multi,
    )
    submit_div = ft.FilledButton(
        text="Divisão",
        width=page.window.width,
        on_click=mostrar_div,
    )
    submit_sub = ft.FilledButton(
        text="Subtração",
        width=page.window.width,
        on_click=mostrar_sub,
    )

    # Construir o layout
    page.add(
        ft.Container(
            width=350,
            bgcolor=ft.colors.BLACK,
            border_radius=ft.border_radius.all(20),
            padding=20,
            content=ft.Column(
                controls=[
                    ft.Row(controls=[result]),
                    ft.Row(controls=[input_num1]),
                    ft.Row(controls=[input_num2]),
                    ft.Column(
                        controls=[
                            submit_adi,
                            submit_sub,
                            submit_multi,
                            submit_div,
                        ]
                    ),
                ]
            ),
        )
    )

ft.app(main)
