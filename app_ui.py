import flet as ft

def main(page: ft.Page):
    page.title = "Xeque - Gestão de checklists"
    page.bgcolor = "#1A121F"

    header = ft.Container(
        ft.Text("Meus Checklists"),
        margin=0,
        padding=10,
        alignment=ft.Alignment.CENTER,
        bgcolor=ft.Colors.BLUE_GREY_400
    )
   
    page.add(header)
    page.update()
  



ft.run(main)