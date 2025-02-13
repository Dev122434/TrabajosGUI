import flet as ft

listResultado = []
indice = 1 

def resultado(ahorro_value=None):
    if ahorro_value is not None:
        listResultado.append(ahorro_value)

def main(page: ft.Page):
    page.title = 'Ahorro'
    page.scroll = 'adaptive'
    page.window_width = 500
    page.window_height = 800

    texto_mes = ft.Text('Ingrese la cantidad a ahorrar en el mes 1', size=20, italic=False)
    ahorro = ft.TextField(label='Ahorro')

    page.add(texto_mes)
    page.add(ahorro)

    def btn_click(e):
        global indice
        ahorro_value = float(ahorro.value)
        resultado(ahorro_value)
        
        ahorro.value = ''
        
        indice += 1

        if indice <= 12:
            texto_mes.value = f'Ingrese la cantidad a ahorrar en el mes {indice}'
            page.update()

    def btn_total(e):
        total = sum(listResultado)
        result_text = ft.Text('El resultado es: ' + str(total), size=30, italic=False)
        page.add(result_text)

    page.add(ft.ElevatedButton('Ahorrar Cantidad', on_click=btn_click))
    page.add(ft.ElevatedButton('Mostrar Total', on_click=btn_total))

ft.app(target=main)
