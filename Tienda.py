import flet as ft

categoria_seleccionada = {"Categoria 1": 0, "Categoria 2": 0, "Categoria 3": 0}
ventas_count = 0
processed_sale = 0

def resultado(monto_value):
    if monto_value > 1000:
        categoria_seleccionada['Categoria 1'] += monto_value
    elif monto_value > 500:
        categoria_seleccionada['Categoria 2'] += monto_value
    else:
        categoria_seleccionada['Categoria 3'] += monto_value

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
    global ventas_count, processed_sale
    page.title = 'Tienda'
    page.scroll = 'adaptive'
    page.window_width = 500
    page.window_height = 800

    ventas_text = ft.Text('Ingrese el número de ventas', size=20, italic=False)
    ventas_input = ft.TextField(label='Ventas', keyboard_type=ft.KeyboardType.NUMBER)
    btn_ventas = ft.ElevatedButton('Ingresar Ventas')
    page.add(ventas_text)
    page.add(ventas_input)
    page.add(btn_ventas)

    monto_text = ft.Text('', size=20, italic=False)
    monto_input = ft.TextField(label='Monto', keyboard_type=ft.KeyboardType.NUMBER)
    btn_registrar = ft.ElevatedButton('Registrar Venta')
    monto_text.visible = False
    monto_input.visible = False
    btn_registrar.visible = False
    page.add(monto_text)
    page.add(monto_input)
    page.add(btn_registrar)

    global chart
    chart = ft.BarChart(
        bar_groups=actualizar_grafica(),
        border=ft.border.all(1, ft.colors.BLUE),
        left_axis=ft.ChartAxis(
            labels_size=40, title=ft.Text("Tienda"), title_size=40
        ),
        bottom_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(value=0, label=ft.Container(ft.Text('Categoria 1'), padding=40)),
                ft.ChartAxisLabel(value=1, label=ft.Container(ft.Text('Categoria 2'), padding=40)),
                ft.ChartAxisLabel(value=2, label=ft.Container(ft.Text('Categoria 3'), padding=40)),
            ],
            labels_size=40,
        ),
        horizontal_grid_lines=ft.ChartGridLines(
            color=ft.colors.GREY_300, width=1, dash_pattern=[3, 3]
        ),
        tooltip_bgcolor=ft.colors.with_opacity(0.5, ft.colors.GREY_300),
        max_y=2000,
        interactive=True,
        expand=True,
    )
    page.add(chart)

    def btn_ventas_click(e):
        nonlocal ventas_text, ventas_input
        ventas = int(ventas_input.value)

        global ventas_count, processed_sale
        ventas_count = ventas
        processed_sale = 0

        ventas_text.visible = False
        ventas_input.visible = False
        btn_ventas.visible = False

        monto_text.value = f'Ingrese el monto de la venta 1'
        monto_text.visible = True
        monto_input.visible = True
        btn_registrar.visible = True
        page.update()

    btn_ventas.on_click = btn_ventas_click

    def btn_registrar_click(e):
        nonlocal monto_text, monto_input
        global processed_sale, ventas_count
        monto_value = float(monto_input.value)
        resultado(monto_value)
        processed_sale += 1
        monto_input.value = ""
        chart.bar_groups = actualizar_grafica()

        if processed_sale < ventas_count:
            monto_text.value = f'Ingrese el monto de la venta {processed_sale+1}'
        else:
            monto_text.value = "Todas las ventas han sido registradas."
            monto_input.visible = False
            btn_registrar.visible = False
        page.update()

    btn_registrar.on_click = btn_registrar_click

ft.app(target=main)
