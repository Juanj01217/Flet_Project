import flet as ft
import random
import features.pokemonData as pokemonData
import json
from features.pokemonEntity import pokemonEntity

collect_chance = 0.9


def load_collected(page: ft.Page):
    stored = page.client_storage.get('collected_pokemons')
    if stored:
        data = json.loads(stored)
        return [pokemonEntity.from_dict(p) for p in data]
    return []

def save_collected(page: ft.Page, collected):
    data = [p.to_dict() for p in collected]
    page.client_storage.set('collected_pokemons', json.dumps(data))

def pokemon_viewer(page: ft.Page, content_container: ft.Container):
    content_container.content = ft.Column()
    content_container.update()

    pokemon_name_input = ft.TextField(label="Enter Pokemon Name", width=300)
    result_text = ft.Text("", size=20)

    list_view = ft.ListView(expand=True, spacing=10)

    def fetch_pokemon(e):
        pokemon_name = pokemon_name_input.value.strip()
        result_text.value = ""
        if pokemon_name:
            pokemon = pokemonData.get_pokemon_data(pokemon_name)
            if pokemon:
                img = ft.Image(src=pokemon.image_url, width=100, height=100) if pokemon.image_url else ft.Container(width=100, height=100)
                info_text = ft.Text(f"Name: {pokemon.name}, Type: {pokemon.type_}, Level: {pokemon.level}")
                collect_button = ft.ElevatedButton(text="Collect", data=pokemon, on_click=collect_pokemon)
                row = ft.Row([img, info_text, collect_button], alignment=ft.MainAxisAlignment.START)
                list_view.controls.append(row)
                result_text.value = "Pokemon fetched successfully!"
            else:
                result_text.value = "Pokemon not found!"
        else:
            result_text.value = "Please enter a Pokemon name."
        content_container.update()

    def collect_pokemon(e):
        button = e.control
        pokemon = button.data
        if random.random() < collect_chance:
            collected = load_collected(page)
            collected.append(pokemon)
            save_collected(page, collected)
            button.text = "Collected!"
            button.disabled = True
            result_text.value = "Collected successfully!"
        else:
            result_text.value = "Failed to collect!"
        content_container.update()
    # Muestra una galería con los primeros 10 pokémons (IDs 1..10)
    def gallery_view(e):
        """Construye una cuadrícula simple con filas de hasta 5 tarjetas cada una."""
        result_text.value = "Loading gallery..."
        gallery_container.controls.clear()
        content_container.update()

        items_per_row = 5
        current_row = ft.Row(spacing=10)
        pokemons = pokemonData.get_pokemon_list(limit=10)
        for pokemon_name in pokemons:
            try:
                pokemon = pokemonData.get_pokemon_data(pokemon_name)
            except Exception as ex:
                pokemon = None
                print(f"Error fetching pokemon {pokemon_name}: {ex}")

            if pokemon:
                img = ft.Image(src=pokemon.image_url, width=96, height=96) if pokemon.image_url else ft.Container(width=96, height=96)
                name = ft.Text(pokemon.name.capitalize(), size=12)
                card = ft.Container(
                    content=ft.Column(
                        [
                        img,
                        name
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    padding=5,
                    border=ft.border.all(1),
                    width=110,
                    height=140
                )
            else:
                card = ft.Container(
                    content=ft.Text(f"#{pokemon_name}\nNot found", size=12),
                    width=110,
                    height=140,
                    alignment=ft.alignment.center
                )

            current_row.controls.append(card)
            # si la fila alcanzó el máximo, agregarla a la columna y crear nueva fila
            if len(current_row.controls) >= items_per_row:
                gallery_container.controls.append(current_row)
                current_row = ft.Row(spacing=10, wrap=True)

        # agregar la última fila si tiene elementos
        if current_row.controls:
            gallery_container.controls.append(current_row)

        result_text.value = "Gallery loaded."
        content_container.update()
    fetch_button = ft.ElevatedButton(text="Fetch Pokemon", on_click=fetch_pokemon)

    # Galería: usaremos una columna que contendrá filas (rows) de tarjetas
    gallery_container = ft.Column()
    show_gallery_button = ft.ElevatedButton(text="Show Gallery (first 10)", on_click=gallery_view)

    content_container.content = ft.Column(
        [
            pokemon_name_input,
            fetch_button,
            show_gallery_button,
            result_text,
            list_view,
            gallery_container
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.START,
        scroll=ft.ScrollMode.AUTO
    )
    content_container.update()