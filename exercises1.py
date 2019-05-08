fav_colours = ['orange', 'purple', 'blue', 'pink']
ages = [35, 34, 27, 22]
coin_flip = ['tails', 'heads', 'tails', 'tails', 'tails']
music_artists = ['Owen Pallet', '2mello', 'Macross 1988']

words = {
    'blossom': "to flourish; develop",

    'heaven': "the abode of God, the angels, and the spirits of the righteous after death; the place or state of existence of the blessed after the mortal life",

    'proud': "feeling pleasure or satisfaction over something regarded as highly honorable or creditable to oneself"
}

fav_movies = {
    'The Thing': 1982,
    'Alien': 1979,
    'They Live!': 1988
}

cities = {
    'Toronto': '2.8 million',
    'Tokyo': '9.2 million',
    'Shanghai': '24 million'
}

family_ages = {
    'Jessica': 35,
    'Jennifer': 34,
    'Savanah': 14,
    'Gina': 61,
    'Brian': 59
}

ages.append(0)

print(coin_flip)

print(fav_colours[0])

print(sorted(ages))

print(fav_movies['Alien'])

print(fav_colours[-1])

cities['Beijing'] = '18.6 million'

coin_flip.reverse()

print(coin_flip)

print(cities['Beijing'])

for artist in music_artists:
    print(f"I think {artist} is great.")

