import fleet as ft
from time import sleep

def main(page: ft.Page):
    page.add(
        ft.Row(controls=[
            ft.Text("LIST OF FRUITS:\n")
        ]),
        ft.Row(controls=[
            ft.Text("Apple"),
            ft.Text("Banana"),
            ft.Text('Mango')
        ]),
        ft.Column(controls=[
            ft.Text("LIST OF cricket:\n")
        ]),
        ft.Column(controls=[
            ft.Text("Sachin"),
            ft.Text("Dhoni"),
            ft.Text('Virat')
        ])
    )

ft.app(target=main)