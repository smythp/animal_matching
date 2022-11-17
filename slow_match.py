import pandas

animals = pandas.read_csv('animals.csv')
places = pandas.read_csv('places.csv')

def select(df):
    """Select a random emoji from the data frame."""

    emoji = df.emoji.sample(1).iloc[0]

    return emoji


if __name__ == '__main__':
    animal = select(animals)
    place = select(places)
    print(animal, place)
