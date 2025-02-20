import flet as ft

escuela_seleccionada = {"Escuela 1": 0, "Escuela 2": 0, "Escuela 3": 0, "Escuela 4": 0}

def resultado(alumnos_value, escuela_value):
    if (alumnos_value >= 100):
        return alumnos_value * 65
    elif (alumnos_value >= 50 and alumnos_value < 100):
        return alumnos_value * 70
    elif (alumnos_value >= 30 and alumnos_value < 50):
        return alumnos_value * 95
    elif (alumnos_value < 30):
        return 4000;

def actualizar_grafica():
    return [
        ft.BarChartGroup(
            x=i,
            bar_rods=[ft.BarChartRod(
                from_y=0,
                to_y=escuela_seleccionada[escuela],
                width=40,
                color=color,
                tooltip=escuela,
                border_radius=10
            )]
        )
        for i, (escuela, color) in enumerate([
            ("Escuela 1", ft.colors.BLUE),
            ("Escuela 2", ft.colors.RED),
            ("Escuela 3", ft.colors.PURPLE),
            ("Escuela 4", ft.colors.YELLOW),
        ])
    ]

def main(page: ft.Page):
    page.title = 'Viaje Alumnos'
    page.scroll = 'adaptive'
    page.window_width = 500
    page.window_height = 800

    page.add(ft.Text('Seleccione una escuela', size=30, italic=False))

    escuela_dropdown = ft.RadioGroup(content=ft.Column([
        ft.Radio(value='Escuela 1', label='Escuela 1'),
        ft.Radio(value='Escuela 2', label='Escuela 2'),
        ft.Radio(value='Escuela 3', label='Escuela 3'),
        ft.Radio(value='Escuela 4', label='Escuela 4'),
    ]))
    page.add(escuela_dropdown)

    alumnos_text = ft.Text('Ingrese el número de alumnos', size=20, italic=False)
    alumnos = ft.TextField(label='alumnos', keyboard_type=ft.KeyboardType.NUMBER)
    page.add(alumnos_text)
    page.add(alumnos)

    def btn_click(e):
        escuela_value = escuela_dropdown.value
        alumnos_value = float(alumnos.value)
        
        escuela_seleccionada[escuela_value] += alumnos_value
        
        total = resultado(alumnos_value, escuela_value)
        
        result_text = ft.Text('El pago final a la compañia de la '+ escuela_value + ' es: ' + str(total), size=30, italic=False)
        page.add(result_text)
        
        chart.bar_groups = actualizar_grafica()
        page.update()

    page.add(ft.ElevatedButton('Calcular', on_click=btn_click))

    global chart
    chart = ft.BarChart(
        bar_groups=actualizar_grafica(),
        border=ft.border.all(1, ft.colors.BLUE),
        left_axis=ft.ChartAxis(
            labels_size=40, title=ft.Text("Viaje"), title_size=40
        ),
        bottom_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(value=0, label=ft.Container(ft.Text('Escuela 1'), padding=40)),
                ft.ChartAxisLabel(value=1, label=ft.Container(ft.Text('Escuela 2'), padding=40)),
                ft.ChartAxisLabel(value=2, label=ft.Container(ft.Text('Escuela 3'), padding=40)),
                ft.ChartAxisLabel(value=3, label=ft.Container(ft.Text('Escuela 4'), padding=40)),
            ],
            labels_size=40,
        ),
        horizontal_grid_lines=ft.ChartGridLines(
            color=ft.colors.GREY_300, width=1, dash_pattern=[3, 3]
        ),
        tooltip_bgcolor=ft.colors.with_opacity(0.5, ft.colors.GREY_300),
        max_y=200,
        interactive=True,
        expand=True,
    )


    page.add(chart)

ft.app(target=main)
