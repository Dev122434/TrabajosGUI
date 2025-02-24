import flet as ft

trabajadores = ['Trabajador 1', 'Trabajador 2', 'Trabajador 3']
trabajador_seleccionado = {"Trabajador 1": 0, "Trabajador 2": 0, "Trabajador 3": 0}

def resultado(pago_value, horas_value):
    return pago_value * horas_value

def actualizar_grafica():
    return [
        ft.BarChartGroup(
            x=i,
            bar_rods=[ft.BarChartRod(
                from_y=0,
                to_y=trabajador_seleccionado[trabajador],
                width=40,
                color=color,
                tooltip=trabajador,
                border_radius=10
            )],
            text=ft.Text(trabajador, size=15)
        )
        for i, (trabajador, color) in enumerate([
            ("Trabajador 1", ft.colors.BLUE),
            ("Trabajador 2", ft.colors.RED),
            ("Trabajador 3", ft.colors.PURPLE),
        ])
    ]

def main(page: ft.Page):
    page.title = 'Nomina'
    page.scroll = 'adaptive'
    page.window_width = 500
    page.window_height = 800

    page.add(ft.Text('Seleccione un trabajador', size=30, italic=False))

    trabajador_dropdown = ft.RadioGroup(content=ft.Column([
        ft.Radio(value='Trabajador 1', label='Trabajador 1'),
        ft.Radio(value='Trabajador 2', label='Trabajador 2'),
        ft.Radio(value='Trabajador 3', label='Trabajador 3'),
    ]))
    page.add(trabajador_dropdown)

    horas_text = ft.Text('Ingrese el número de horas trabajadas', size=20, italic=False)
    horas = ft.TextField(label='Horas Trabajadas', keyboard_type=ft.KeyboardType.NUMBER)
    sueldo_text = ft.Text('Ingrese su pago por hora', size=20, italic=False)
    sueldo = ft.TextField(label='Pago Hora', keyboard_type=ft.KeyboardType.NUMBER)
    page.add(horas_text)
    page.add(horas)
    page.add(sueldo_text)
    page.add(sueldo)

    def btn_click(e):
        trabajador_value = trabajador_dropdown.value
        horas_value = int(horas.value)
        sueldo_value = int(sueldo.value)

        total = resultado(sueldo_value, horas_value)

        trabajador_seleccionado[trabajador_value] += total
        
        result_text = ft.Text('El pago semanal al '+ trabajador_value + ' es: ' + str(total), size=30, italic=False)
        page.add(result_text)
        
        chart.bar_groups = actualizar_grafica()
        page.update()

    page.add(ft.ElevatedButton('Calcular', on_click=btn_click))

    global chart
    chart = ft.BarChart(
        bar_groups=actualizar_grafica(),
        border=ft.border.all(1, ft.colors.BLUE),
        left_axis=ft.ChartAxis(
            labels_size=40, title=ft.Text("Nomina"), title_size=40
        ),
        bottom_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(value=0, label=ft.Container(ft.Text('Trabajador 1'), padding=40)),
                ft.ChartAxisLabel(value=1, label=ft.Container(ft.Text('Trabajador 2'), padding=40)),
                ft.ChartAxisLabel(value=2, label=ft.Container(ft.Text('Trabajador 3'), padding=40)),
            ],
            labels_size=40,
        ),
        horizontal_grid_lines=ft.ChartGridLines(
            color=ft.colors.GREY_300, width=1, dash_pattern=[3, 3]
        ),
        tooltip_bgcolor=ft.colors.with_opacity(0.5, ft.colors.GREY_300),
        max_y=5000,
        interactive=True,
        expand=True,
    )

    page.add(chart)

ft.app(target=main)
