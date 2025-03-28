import flet as ft
import datetime

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
    def mostrar_idade(e):
        try:
            data = datetime.datetime.strptime(input_data.value, "%d/%m/%Y")
            agora = datetime.datetime.now()
            agora = agora.strftime("%d/%m/%Y")
            agora = datetime.datetime.strptime(agora, "%d/%m/%Y")

            # situação
            if data < agora:
                # diferença
                anos_diferenca = abs(data.year - agora.year)
                if (data.month >= agora.month and data.day > agora.day) or (data.month >= agora.month):
                    anos_diferenca -= 1
                txt_resultado.value = f"a idade é {anos_diferenca}"
            else:
                txt_resultado.value = f"Data inválida."
        except ValueError:
            txt_resultado.value = f"Erro ao calcular a idade"

        page.update()


    # Criação de componentes
    input_data = ft.TextField(label="Digite aqui", hint_text="Insira a data")
    txt_resultado = ft.Text(value="")
    submit_button = ft.FilledButton(
        text="Submit",
        width=page.window.width,
        on_click=mostrar_idade,
    )

    # Construir o layout
    page.add(
        # ft.SafeArea(
            ft.Column(
                [
                    input_data,
                    submit_button,
                    txt_resultado,
                ]
            # )
        )
    )

ft.app(main)