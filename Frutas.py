import flet as ft

mapFrutas = {"Platano": 1.35, "Manzana": 0.80, "Pera": 0.85, "Naranja": 0.70}
frutas_seleccionadas = {"Platano": 0, "Manzana": 0, "Pera": 0, "Naranja": 0}

def resultado(kilo_value, fruta_value):
    return kilo_value * mapFrutas[fruta_value]

def actualizar_grafica():
    return [
        ft.BarChartGroup(
            x=i,
            bar_rods=[ft.BarChartRod(
                from_y=0,
                to_y=frutas_seleccionadas[fruta],
                width=40,
                color=color,
                tooltip=fruta,
                border_radius=10
            )]
        )
        for i, (fruta, color) in enumerate([
            ("Manzana", ft.colors.RED),
            ("Platano", ft.colors.YELLOW),
            ("Pera", ft.colors.GREEN),
            ("Naranja", ft.colors.ORANGE),
        ])
    ]

def main(page: ft.Page):
    page.title = 'Frutas'
    page.scroll = 'adaptive'
    page.window_width = 500
    page.window_height = 800

    page.add(ft.Text('Seleccione una fruta', size=30, italic=False))

    fruta_dropdown = ft.RadioGroup(content=ft.Column([
        ft.Radio(value='Platano', label='Platano'),
        ft.Radio(value='Manzana', label='Manzana'),
        ft.Radio(value='Pera', label='Pera'),
        ft.Radio(value='Naranja', label='Naranja'),
    ]))
    page.add(fruta_dropdown)

    kilos_fruta = ft.Text('Ingrese el número de kilos que desea', size=20, italic=False)
    kilo = ft.TextField(label='Kilos', keyboard_type=ft.KeyboardType.NUMBER)
    page.add(kilos_fruta)
    page.add(kilo)

    def btn_click(e):
        fruta_value = fruta_dropdown.value
        kilo_value = float(kilo.value)
        
        frutas_seleccionadas[fruta_value] += kilo_value
        
        total = resultado(kilo_value, fruta_value)
        
        result_text = ft.Text('El precio final es: ' + str(total), size=30, italic=False)
        page.add(result_text)
        
        chart.bar_groups = actualizar_grafica()
        page.update()

    page.add(ft.ElevatedButton('Calcular', on_click=btn_click))

    global chart
    chart = ft.BarChart(
        bar_groups=actualizar_grafica(),
        border=ft.border.all(1, ft.colors.BLUE),
        left_axis=ft.ChartAxis(
            labels_size=40, title=ft.Text("Frutas"), title_size=40
        ),
        bottom_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(value=0, label=ft.Container(ft.Text('Manzanas'), padding=40)),
                ft.ChartAxisLabel(value=1, label=ft.Container(ft.Text('Plátanos'), padding=40)),
                ft.ChartAxisLabel(value=2, label=ft.Container(ft.Text('Peras'), padding=40)),
                ft.ChartAxisLabel(value=3, label=ft.Container(ft.Text('Naranjas'), padding=40)),
            ],
            labels_size=40,
        ),
        horizontal_grid_lines=ft.ChartGridLines(
            color=ft.colors.GREY_300, width=1, dash_pattern=[3, 3]
        ),
        tooltip_bgcolor=ft.colors.with_opacity(0.5, ft.colors.GREY_300),
        max_y=10,
        interactive=True,
        expand=True,
    )


    page.add(chart)

ft.app(target=main)
