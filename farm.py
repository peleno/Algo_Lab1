class Farm:
    def __init__(self, location, animals_count, power):
        self.location = location
        self.animals_count = animals_count
        self.power = power

    def __str__(self):
        return f'Farm at {self.location}. Animals_count: {self.animals_count}, power: {self.power}'