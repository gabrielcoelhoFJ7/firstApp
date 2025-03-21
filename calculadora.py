import flet as ft

def main(page: ft.Page):

    # Configuração da página
    page.title = "Minha Aplicação Flet"
    page.theme_mode = ft.ThemeMode.DARK # ou ft.ThemeMode.LIGHT
    page.window.width = 375
    page.window.height = 667
    page.theme = ft.Theme(font_family="Kanit")  # Default app font

    # Definição de funções
    def mostrar_nome(e):
        txt_resultado.value =
        page.update()


    # Criação de componentes
    text_num1 = ft.Text(value="Nome:")
    input_num1 = ft.TextField(label="Digite aqui", hint_text="Insira o nome")
    text_num2 = ft.Text(value="Sobrenome:")
    input_num2 = ft.TextField(label="Digite aqui", hint_text="Insira o sobrenome")
    txt_resultado = ft.Text(value="")
    submit_button = ft.FilledButton(
        text="Submit",
        width=page.window.width,
        on_click=mostrar_nome,
    )

    # Construir o layout
    page.add(
        # ft.SafeArea(
            ft.Column(
                [
                    text_num1,
                    input_num1,
                    text_num2,
                    input_num2,
                    submit_button,
                    txt_resultado,
                ]
            # )
        )
    )

ft.app(main)