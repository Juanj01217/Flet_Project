import flet as ft

import features.pokemonData as pokemonData

def pokemon_viewer(page: ft.Page):
    page.title = "Pokemon Viewer"

    pokemon_name_input = ft.TextField(label="Enter Pokemon Name", width=300)
    result_text = ft.Text("", size=20)

    def fetch_pokemon(e):
        pokemon_name = pokemon_name_input.value.strip()
        if pokemon_name:
            pokemon = pokemonData.get_pokemon_data(pokemon_name)
            if pokemon:
                if pokemon.image_url:
                    img = ft.Image(src=pokemon.image_url, width=100, height=100)
                    page.add(img)
                result_text.value = f"Name: {pokemon.name}, Type: {pokemon.type_}, Level: {pokemon.level}"
            else:
                result_text.value = "Pokemon not found!"
        else:
            result_text.value = "Please enter a Pokemon name."
        result_text.update()


    fetch_button = ft.ElevatedButton(text="Fetch Pokemon", on_click=fetch_pokemon)

    
    
    page.add(
        ft.Column(
            [
                pokemon_name_input,
                fetch_button,
                result_text
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.START,
        )
    )