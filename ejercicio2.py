import flet as ft

def main(page: ft.Page):
    page.title = 'Distancia entre personas'
    page.scroll = 'adaptive'
    page.window_width = 500
    page.window_height = 800

    def btn_click(e):   
        p1 = 70
        p2 = 150
        velocidad = 1
        
        while p1 < p2:
            text1 = ft.Text(f'Distancia Persona 1: {p1} km')
            text2 = ft.Text(f'Distancia Persona 2: {p2} km')
            page.add(text1)
            page.add(text2)
            p1 += velocidad
            p2 -= velocidad

            page.update()

        result = ft.Text(f'Punto de encuentro: {p1} km', size=30, italic=False)
        page.add(result)

    page.add(ft.ElevatedButton('Mostrar Distancia', on_click=btn_click))

ft.app(target=main)
