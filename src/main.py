import flet as ft
import pokemonViewer as pv
import pokemonCollected as pc

def main(page: ft.Page):
    page.title = "Pokemon App"
    
    content_container = ft.Container(expand=True)
    
    def show_viewer(e):
        pv.pokemon_viewer(page, content_container)
    
    def show_collected(e):
        pc.pokemon_collected(page, content_container)
    
    viewer_button = ft.ElevatedButton(text="Pokémon Viewer", on_click=show_viewer)
    collected_button = ft.ElevatedButton(text="Collected Pokémon", on_click=show_collected)
    
    page.add(
        ft.Row([viewer_button, collected_button]),
        content_container
    )

    show_viewer(None)

ft.app(main)