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
        data = str(input_data.value)
        data_formatada = datetime.strptime(data, "%d/%m/%Y")
        agora = datetime.datetime.now()

        # situação
        if data == agora:
            situacao = "presente"
        elif data < agora:
            situacao = "passado"
        else:
            situacao = "futuro"

        # diferença
        if situacao == "passado" or situacao == "futuro":
            dias_diferenca = int(abs(data - agora).days)
            meses_diferenca = abs(((data.year - agora.year) * 12) + data.month - agora.month)
            anos_diferenca = abs(data.year - agora.year)
            if meses_diferenca % 12 == 0 and data.day - agora.day > 0:
                anos_diferenca = anos_diferenca - 1


        txt_resultado.value = input_nome.value+" "+input_sobrenome.value
        page.update()


    # Criação de componentes
    text_data = ft.Text(value="Nome:")
    input_data = ft.TextField(label="Digite aqui", hint_text="Insira o nome")
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
                    text_nome,
                    input_nome,
                    text_sobrenome,
                    input_sobrenome,
                    submit_button,
                    txt_resultado,
                ]
            # )
        )
    )

ft.app(main)