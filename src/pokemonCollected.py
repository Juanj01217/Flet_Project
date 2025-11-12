import flet as ft
import json
from pokemonViewer import load_collected 

def pokemon_collected(page: ft.Page, content_container: ft.Container):
    content_container.content = ft.Column()
    content_container.update()

    collected = load_collected(page)
    if not collected:
        content_container.content = ft.Text("No Pokémon collected yet.", size=20)
        content_container.update()
        return

    list_view = ft.ListView(expand=True, spacing=10)
    for pokemon in collected:
        row = ft.Row(
            [
                ft.Image(src=pokemon.image_url, width=50, height=50) if pokemon.image_url else ft.Container(),
                ft.Text(pokemon.get_info(), size=16)
            ]
        )
        list_view.controls.append(row)

    content_container.content = ft.Column([ft.Text("Collected Pokémon:", size=24), list_view])
    content_container.update()