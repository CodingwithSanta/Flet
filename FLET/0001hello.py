import flet as f
def main(page: f.Page):
    page.title = "Hello World"
    text = f.Text(value="My First Flet App!",color = "blue")
    page.controls.append(text)
    page.update()
f.app(target=main)    