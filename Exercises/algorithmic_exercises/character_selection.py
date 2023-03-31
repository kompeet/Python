def street_fighter_selection(fighters, initial_position, moves):
    x = initial_position[0]
    y = initial_position[1]
    result = []

    for i in moves:
        if i == 'up':
            if x == 0:
                result.append(fighters[x][y])
            else:
                x -= 1
                result.append(fighters[x][y])
        elif i == 'down':
            if x == 1:
                result.append(fighters[x][y])
            else:
                x += 1
                result.append(fighters[x][y])
        elif i == 'right':
            if y == 5:
                y -= 5
                result.append(fighters[x][y])
            else:
                y += 1
                result.append(fighters[x][y])
        elif i == 'left':
            if y == 0:
                y += 5
                result.append(fighters[x][y])
            else:
                y -= 1
                result.append(fighters[x][y])

    return result


fighters = [
    ["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
    ["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
]
initial_position = (0, 0)
moves = ['down', 'left', 'left', 'left', 'left']

print(street_fighter_selection(fighters, initial_position, moves))