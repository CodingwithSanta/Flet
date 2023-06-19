import flet as f
from time import sleep
def main(page:f.Page):
    page.title ="Counter App"
    
    text = f.Text()
    page.add(text)
    
    for i in range(1,100):
        text.value = "Count " +": " + str(i)
        page.update()
        sleep(0.5)    
f.app(target = main)