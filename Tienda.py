import flet as ft

def resultado(monto_value):
    aux1 = 0
    aux2 = 0
    aux3 = 0
    if monto_value > 1000:
        aux1 += 1
        categoria_seleccionada['Categoria 1'] += monto_value
    elif monto_value > 500 and monto_value <= 1000:
        aux2 += 1
        categoria_seleccionada['Categoria 2'] += monto_value
    else:
        aux3 += 1
        categoria_seleccionada['Categoria 3'] += monto_value

categoria_seleccionada = {"Categoria 1": 0, "Categoria 2": 0, "Categoria 3": 0}

def actualizar_grafica():
    return [
        ft.BarChartGroup(
            x=i,
            bar_rods=[ft.BarChartRod(
                from_y=0,
                to_y=categoria_seleccionada[categoria],
                width=40,
                color=color,
                tooltip=categoria,
                border_radius=10
            )]
        )
        for i, (categoria, color) in enumerate([
            ("Categoria 1", ft.colors.BLUE),
            ("Categoria 2", ft.colors.RED),
            ("Categoria 3", ft.colors.PURPLE),
        ])
    ]

def main(page: ft.Page):
    page.title = 'Tienda'
    page.scroll = 'adaptive'
    page.window_width = 500
    page.window_height = 800

    page.add(ft.Text('Seleccione una categoria', size=30, italic=False))

    escuela_dropdown = ft.RadioGroup(content=ft.Column([
        ft.Radio(value='Categoria 1', label='Categoria 1'),
        ft.Radio(value='Categoria 2', label='Categoria 2'),
        ft.Radio(value='Categoria 3', label='Categoria 3'),
    ]))
    page.add(escuela_dropdown)

    ventas_text = ft.Text('Ingrese el número de ventas', size=20, italic=False)
    ventas = ft.TextField(label='Ventas', keyboard_type=ft.KeyboardType.NUMBER)
    page.add(ventas_text)
    page.add(ventas)
    monto_text = ft.Text('1. Ingrese el monto de lo vendido', size=20, italic=False)
    monto = ft.TextField(label='Monto', keyboard_type=ft.KeyboardType.NUMBER)
    page.add(monto_text)
    page.add(monto)


    def btn_click(e):
        i = 1
        i += 1
        monto_value = float(monto.value)
        if (i <= monto_value):
            monto_text.value = f'{i}. Ingrese el monto de lo vendido'
            page.update()
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
