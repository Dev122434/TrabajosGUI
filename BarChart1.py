import flet as ft

def main(page: ft.Page):

    chart = ft.BarChart(

        bar_groups=[
            ft.BarChartGroup(
                x=0, # Se define primer elemento a graficar, indice 0, en eje x
                bar_rods=[
                    ft.BarChartRod(
                        from_y=0, # Valor inicial
                        to_y=40, # Valor final
                        width=40, # Ancho de la barra
                        color=ft.colors.RED, # Color de la barra
                        tooltip="Manzanas", # Texto que aparece cuando se pasa el mouse sobre la barra
                        border_radius=10, # Barra redonda
                    ),
                ],
            ),
            ft.BarChartGroup(
                x=1,
                bar_rods=[
                    ft.BarChartRod(
                        from_y=0,
                        to_y=100,
                        width=40,
                        color=ft.colors.BLUE,
                        tooltip="Arándanos",
                        border_radius=10,
                    ),
                ],
            ),

            ft.BarChartGroup(
                x=2,
                bar_rods=[
                    ft.BarChartRod(
                        from_y=0,
                        to_y=30,
                        width=40,
                        color=ft.colors.YELLOW,
                        tooltip="Cerezas",
                        border_radius=10,
                    ),
                ],
            ),
            ft.BarChartGroup(
                x=3,
                bar_rods=[
                    ft.BarChartRod(
                        from_y=0,
                        to_y=60,
                        width=40,
                        color=ft.colors.ORANGE,
                        tooltip="Naranjas",
                        border_radius=10,
                    ),
                ],
            ),
        ],
        border=ft.border.all(1, ft.colors.BLUE), # Borde del área de graficacion (recuadro)

        # eje izquierdo (y)
        left_axis=ft.ChartAxis(
            labels_size=40, title=ft.Text("Frutas"), title_size=40 # Label_size tamaño de los valores eje izquierdo
        ),

        bottom_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(
                    value=0, label=ft.Container(ft.Text('Manzanas'), padding=40)
                ),
                ft.ChartAxisLabel(
                    value=1, label=ft.Container(ft.Text('Arándanos'), padding=40)
                ),
                ft.ChartAxisLabel(
                    value=2, label=ft.Container(ft.Text('Cerezas'), padding=40)
                ),
                ft.ChartAxisLabel(
                    value=3, label=ft.Container(ft.Text('Naranjas'), padding=40)
                ),
            ],
            labels_size=40,
        ),
        #Lineas dentro del area de graficacion - horizontales
        horizontal_grid_lines=ft.ChartGridLines(
            color=ft.colors.GREY_300, width=1,dash_pattern=[3,3]
            # Por ejemplo, la lista [5, 10] daría como resultado guiones de 5 pixeles de largo
            # seguidos de espacios en blanco de 10 pixeles de largo
        ),
        # Area que se muestra cuando se pasa el mouse sobre las barras
        tooltip_bgcolor=ft.colors.with_opacity(0.5, ft.colors.GREY_300),
        max_y=110, # Valor maximo del eje y
        # Habilita el tooltip_boolean
        interactive=True,
        # Ajusta el area de graficación al tamaño de la ventana
        expand=True,
    )
    page.add(chart)

ft.app(main)