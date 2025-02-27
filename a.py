import flet as ft

listResultado = []
indice = 1

def horasLista(ahorro_value=None):
    if ahorro_value is not None:
        listResultado.append(ahorro_value)

def actualizar_grafica():
    return [
        ft.BarChartGroup(
            x=i,
            bar_rods=[ft.BarChartRod(
                from_y=0,
                to_y=6,
                width=40,
                color=color,
                tooltip=empleado,
                border_radius=10
            )],
            text=ft.Text(empleado, size=15)
        )
        for i, (empleado, color) in enumerate([
            ("Dia 1", ft.colors.PURPLE),
            ("Dia 2", ft.colors.RED),
            ("Dia 3", ft.colors.GREEN),
            ("Dia 4", ft.colors.BLUE),
            ("Dia 5", ft.colors.ORANGE),
            ("Dia 6", ft.colors.DEEP_ORANGE),
        ])
    ]

def main(page: ft.Page):
    page.title = 'Empleado'
    page.scroll = 'adaptive'
    page.window_width = 500
    page.window_height = 800

    texto_mes = ft.Text('1. Ingrese la cantidad de horas trabajadas', size=20, italic=False)
    horas = ft.TextField(label='Horas')

    page.add(texto_mes)
    page.add(horas)

    sueldo = None  # Inicializa sueldo en None fuera de la función
    sueldo_mes = None  # Inicializa sueldo_mes en None fuera de la función

    def btn_click(e):
        global indice
        horas_value = int(horas.value)
        horasLista(horas_value)

        horas.value = ''

        indice += 1

        if indice < 7:
            texto_mes.value = f'{indice}. Ingrese la cantidad de horas trabajadas'
            page.update()
        
        # Solo mostrar el campo de sueldo cuando sea el sexto índice
        if indice == 6 and sueldo is None:
            sueldo_mes = ft.Text('1. Ingrese el sueldo del trabajador', size=20, italic=False)
            page.add(sueldo_mes)
            sueldo = ft.TextField(label='Sueldo')
            page.add(sueldo)

        page.update()

    def btn_total(e):
        if sueldo is not None:
            sueldo_value = float(sueldo.value)  # Convertir a float
            total = sum(listResultado) * sueldo_value
            result_text = ft.Text('El sueldo es: ' + str(total), size=30, italic=False)
            page.add(result_text)
        else:
            result_text = ft.Text('Por favor ingrese el sueldo', size=30, italic=False)
            page.add(result_text)
        
        page.update()

    chart = ft.BarChart(
        bar_groups=actualizar_grafica(),
        border=ft.border.all(1, ft.colors.BLUE),
        left_axis=ft.ChartAxis(
            labels_size=40, title=ft.Text("Empleado"), title_size=40
        ),
        bottom_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(value=0, label=ft.Container(ft.Text('Dia 1'), padding=40)),
                ft.ChartAxisLabel(value=1, label=ft.Container(ft.Text('Dia 2'), padding=40)),
                ft.ChartAxisLabel(value=2, label=ft.Container(ft.Text('Dia 3'), padding=40)),
                ft.ChartAxisLabel(value=3, label=ft.Container(ft.Text('Dia 4'), padding=40)),
                ft.ChartAxisLabel(value=4, label=ft.Container(ft.Text('Dia 5'), padding=40)),
                ft.ChartAxisLabel(value=5, label=ft.Container(ft.Text('Dia 6'), padding=40)),
            ],
            labels_size=40,
        ),
        horizontal_grid_lines=ft.ChartGridLines(
            color=ft.colors.GREY_300, width=1, dash_pattern=[3, 3]
        ),
        tooltip_bgcolor=ft.colors.with_opacity(0.5, ft.colors.GREY_300),
        max_y=20,
        interactive=True,
        expand=True,
    )

    page.add(chart)

    page.add(ft.ElevatedButton('Ingresar Horas', on_click=btn_click))
    page.add(ft.ElevatedButton('Mostrar sueldo', on_click=btn_total))

ft.app(target=main)
