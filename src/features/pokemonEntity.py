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
    
    def to_dict(self):
        return {
            'name': self.name,
            'type_': self.type_,
            'level': self.level,
            'image_url': self.image_url
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data['name'],
            type_=data['type_'],
            level=data['level'],
            image_url=data.get('image_url')
        )