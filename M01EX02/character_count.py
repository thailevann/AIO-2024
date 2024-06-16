def character_count(word):
    character_statistic = {}
    for i in word:
        if i in character_statistic:
            character_statistic[i] = character_statistic["i"] + 1
        else:
            character_statistic[i] = 1

    return character_statistic


assert character_count("Baby") == {'B': 1, 'a': 1, 'b': 1, 'y': 1}
print(character_count('smiles'))
