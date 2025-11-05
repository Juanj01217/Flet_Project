class pokemonEntity:
    def __init__(self, name, type_, level, image_url=None):
        self.name = name
        self.type_ = type_
        self.level = level
        self.image_url = image_url
        
    def level_up(self):
        self.level += 1
        print(f"{self.name} leveled up to {self.level}!")

    def get_info(self):
        return f"Name: {self.name}, Type: {self.type_}, Level: {self.level}"