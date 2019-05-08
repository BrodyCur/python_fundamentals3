# Exercise 0

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
    'Toronto': 2.8,
    'Tokyo': 9.2,
    'Shanghai': 24
}

family_ages = {
    'Jessica': 35,
    'Jennifer': 34,
    'Savanah': 14,
    'Gina': 61,
    'Brian': 59
}

# Exercise 1

ages.append(0)

print(coin_flip)

print(fav_colours[0])

print(sorted(ages))

print(fav_movies['Alien'])

# Exercise 2

print(fav_colours[-1])

cities['Beijing'] = 18.6

coin_flip.reverse()

print(coin_flip)

print(cities['Beijing'])

for artist in music_artists:
    print(f"I think {artist} is great.")

# Exercise 3

print(music_artists[0:2])

for movie, date in fav_movies.items():
    print(f"{movie} came out in {date}.")

print(sorted(family_ages.values(), reverse=True))

fav_movies['Beauty and the Beast'] = [1991, 2017]

print(fav_movies)

# Exercise 4

for age in ages:
    if age > 30:
        print(age)

print(max(ages))

coin_flip.count('heads')

music_artists.pop(2)

cities['Toronto'] = 5.7

# Exercise 5

print(sum(cities.values()))

for name, age in family_ages.items():
    if age >= 35:
        print(f"{name} is old.")
    else:
        print(f"{name} is young.")

print(fav_colours[-2:])

for index, age in enumerate(ages):
    ages[index] = age + 1

print(ages)

fav_colours.append('lime')
fav_colours.append('aqua')

# Exercise 6

movie_list = {
    '1999': ['The Matrix', 'Star Wars: The Phantom Menace', 'The Mummy'],
    '2009': ['Avatar', 'Star Trek', 'District 9'],
    '2019': ['How to Train Your Dragon 3', 'Toy Story 4', 'Star Wars: Ep 9']
}

phone = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ['*', 0, '#']
]

countries  = [
    {
        'name': 'Canada',
        'continent': 'North America',
        'island': False
    },
    {
        'name': 'Japan',
        'continent': 'Asian',
        'island': True
    },
    {
        'name': 'Germany',
        'continent': 'Europe',
        'island': False
    }
]

# Exercise 7

skate_list = []

def skate_msg():
    msg = 0
    while msg < 20:
        print("I will not skateboard in the halls")
        msg += 1
        skate_list.append("I will not skateboard in the halls")

skate_msg()
print(skate_list)

numbers = list(range(0, 51))
print(numbers)

def adder():
    total = 0
    for num in numbers:
        total += num
    return total

adder()

triple_numbers = []
for num in range(0, 51):
    triple_numbers.append(num)
    triple_numbers.append(num)
    triple_numbers.append(num)

print(triple_numbers)

not_islands = []
for i in countries:
    if i['island'] == False:
        not_islands.append(i)

print(not_islands)

# Exercise 8

expenses1 = [250, 7.95, 30.95, 16.50]
expenses2 = [543, 6.84, 20.65, 467, 4, 35.74]

def expense_calc(i):
    return sum(i)

print(expense_calc(expenses1))
print(expense_calc(expenses2))