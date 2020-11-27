import re


def poke_name(filename):
    with open(filename, 'r') as file:
        pokeFile = file.read()
        pokeRe = re.compile(r'\w+')
        pokeList = pokeRe.findall(pokeFile) #list of pokemon names

    maxStreak, currentStreak = [], []

    def name_start(lastChar, pokeList):
        for index, name in enumerate(pokeList): #give index to the names
            if name.startswith(lastChar):
                return index
        return False

    for name in pokeList:
        currentName = name
        currentStreak.append(currentName)

        tempPokeList = pokeList[:]
        tempPokeList.pop(pokeList.index(currentName))

        index = name_start(currentName[-1], tempPokeList)

        while index is not False:
            currentName = tempPokeList[index]
            currentStreak.append(currentName)
            tempPokeList.pop(index)
            index = name_start(currentName[-1], tempPokeList)

        if len(currentStreak) > len(maxStreak):
            maxStreak = currentStreak

        currentStreak = []
    print(maxStreak)
    print(len(maxStreak))
poke_name('pokemonNames')