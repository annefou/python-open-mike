def my_enumerate(iterable):
    for i in range(len(iterable)):
        yield i, iterable[i]

geom = [
    ['C', '42.244746', '18.570778', '59.319684'],
    ['C', '41.657924', '17.195400', '58.967458'],
    ['O', '41.269264', '16.953033', '57.823006'],
    ['C', '41.154273', '19.649457', '59.114748'],
    ['C', '39.931188', '19.394465', '59.970710'],
]

for i, e in my_enumerate(geom):
    print(i, e)
