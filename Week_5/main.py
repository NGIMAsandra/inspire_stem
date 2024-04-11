import flet as ft

def main(page: ft.page) :
    page.title = "Learning Flet"
    content = ft.Column(
        spacing=20,
        controls= [          
            ft.Text("This is a sample Flet application" , size= 21, weight = "w600"),
            ft.Text("Welcome to learning FLET", size = 16),
            ft.Row(
                spacing= 20,
                controls =[
                    ft.Text("this is a row in flet"),
                    ft.ElevatedButton("Click me")
                ]
                
                
            )w  
        ]
            
    )

    #DISPLAY OUR SCREEN
    page.add()

ft.app(target=main)