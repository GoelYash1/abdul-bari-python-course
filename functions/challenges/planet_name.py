def planet(idx):
    planets = {
        1:'Mercury',
        2:'Venus',
        3:'Earth',
        4:'Mars',
        5:'Jupiter',
        6:'Saturn',
        7:'Uranus',
        8:'Neptune',
        9:'Pluto'
    }
    return planets[idx] if 0<idx<=9 else -1

n=int(input("Which number of planet you want to find: "))
planet_name = planet(n)
if 0<n<=9:
    print(f"The {n} planet in milky way galaxy is: {planet_name}",)
else:
    print(n, "Wrong input for the planet")