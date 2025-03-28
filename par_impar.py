import flet as ft

def main(page: ft.Page):

    # Configuração da página
    page.title = "Minha Aplicação Flet"
    page.theme_mode = ft.ThemeMode.DARK # ou ft.ThemeMode.LIGHT
    page.window.width = 375
    page.window.height = 667
    page.fonts = {
        "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
    }
    page.theme = ft.Theme(font_family="Kanit")  # Default app font

    # Definição de funções
    def mostrar_par_impar(e):
        try:
            if int(input_num.value) % 2 == 0:
                txt_resultado.value = "Par"
            else:
                txt_resultado.value = "Impar"
        except ValueError:
            txt_resultado.value = "Valor incorreto, tente usar apenas números."
        page.update()


    # Criação de componentes
    text_num = ft.Text(value="Verifique se é par ou impar:")
    input_num = ft.TextField(label="Digite aqui", hint_text="Insira o número")
    txt_resultado = ft.Text(value="")
    submit_button = ft.FilledButton(
        text="Submit",
        width=page.window.width,
        on_click=mostrar_par_impar,
    )

    # Construir o layout
    page.add(
            ft.Column(
                [
                    text_num,
                    input_num,
                    submit_button,
                    txt_resultado,
                ]
        )
    )

ft.app(main)