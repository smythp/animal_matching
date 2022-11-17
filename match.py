import random

def open_and_read(filename):
    with open(filename, 'r') as file:
        emojis = file.readlines()
        emojis = [emoji.strip() for emoji in emojis]

        return emojis


if __name__ == '__main__':
    animals = open_and_read('animals.txt')
    places = open_and_read('places.txt')

    animal = random.choice(animals)
    place = random.choice(places)    
    print(animal, place, sep='')
