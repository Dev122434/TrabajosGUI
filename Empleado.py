import flet as ft

listResultado = []
indice = 1
sueldo = None

def horasLista(valor_horas=None):
    if valor_horas is not None:
        listResultado.append(valor_horas)

def actualizar_grafica():
    return [
        ft.BarChartGroup(
            x=i,
            bar_rods=[ft.BarChartRod(
                from_y=0,
                to_y=(listResultado[i] if i < len(listResultado) else 0),
                width=40,
                color=color,
                tooltip=f"{empleado}: {(listResultado[i] if i < len(listResultado) else 0)} horas",
                border_radius=10
            )],
        )
        for i, (empleado, color) in enumerate([
            ("Dia 1", ft.colors.BLUE),
            ("Dia 2", ft.colors.RED),
            ("Dia 3", ft.colors.PURPLE),
            ("Dia 4", ft.colors.GREEN),
            ("Dia 5", ft.colors.YELLOW),
            ("Dia 6", ft.colors.ORANGE),
        ])
    ]

def main(page: ft.Page):
    global sueldo, indice

    page.title = 'Empleado'
    page.scroll = 'adaptive'
    page.window_width = 500
    page.window_height = 800

    texto_mes = ft.Text('1. Ingrese la cantidad de horas trabajadas', size=20, italic=False)
    horas = ft.TextField(label='Horas')

    page.add(texto_mes)
    page.add(horas)

    global chart
    chart = ft.BarChart(
        bar_groups=actualizar_grafica(),
        border=ft.border.all(1, ft.colors.BLUE),
        left_axis=ft.ChartAxis(
            labels_size=40, title=ft.Text("Horas"), title_size=40
        ),
        bottom_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(value=1, label=ft.Container(ft.Text('Dia 1'), padding=40)),
                ft.ChartAxisLabel(value=2, label=ft.Container(ft.Text('Dia 2'), padding=40)),
                ft.ChartAxisLabel(value=3, label=ft.Container(ft.Text('Dia 3'), padding=40)),
                ft.ChartAxisLabel(value=4, label=ft.Container(ft.Text('Dia 4'), padding=40)),
                ft.ChartAxisLabel(value=5, label=ft.Container(ft.Text('Dia 5'), padding=40)),
                ft.ChartAxisLabel(value=6, label=ft.Container(ft.Text('Dia 6'), padding=40)),
            ],
            labels_size=40,
        ),
        horizontal_grid_lines=ft.ChartGridLines(
            color=ft.colors.GREY_300, width=1, dash_pattern=[3, 3]
        ),
        tooltip_bgcolor=ft.colors.with_opacity(0.5, ft.colors.GREY_300),
        max_y=30, 
        interactive=True,
        expand=True,
    )
    page.add(chart)

    def btn_click(e):
        global indice, sueldo
        horas_value = int(horas.value)

        horasLista(horas_value)
        horas.value = ''

        indice += 1
        chart.bar_groups = actualizar_grafica()

        if indice <= 6:
            texto_mes.value = f'{indice}. Ingrese la cantidad de horas trabajadas'
        elif indice == 7:
            sueldo_mes = ft.Text('Ingrese el sueldo del trabajador', size=20, italic=False)
            page.add(sueldo_mes)
            sueldo = ft.TextField(label='Sueldo')
            page.add(sueldo)
        page.update()

    def btn_total(e):
        sueldo_value = float(sueldo.value)

        total = sum(listResultado) * sueldo_value
        result_text = ft.Text('El sueldo es: ' + str(total), size=30, italic=False)
        page.add(result_text)
        page.update()

    btnIngresar = ft.ElevatedButton('Ingresar Horas', on_click=btn_click)
    btnSueldo = ft.ElevatedButton('Mostrar sueldo', on_click=btn_total)
    page.add(btnIngresar)
    page.add(btnSueldo)

ft.app(target=main)