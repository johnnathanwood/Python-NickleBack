# Example set
# songs = {
#     ('Nickelback', 'How You Remind Me'), 
#     ('Will.i.am', 'That Power'),
#     ('Miles Davis', 'Stella by Starlight'),
#     ('Nickelback', 'Animals')
# }

# 1. Define a set that contains tuples. Each tuple should contain two strings:
songs = {
    ('Nickelback', 'How You Remind Me'),
    ('Will.i.am', 'That Power'),
    ('Miles Davis', 'Stella by Starlight'),
    ('Nickelback', 'Animals')
} 
# i.  The name of an artist
# ii. A song by that artist

# 2. Using a set comprehension, create a new set that contains all songs that were not performed by Nickelback.
new_songs = {band[1] for band in songs if band[0] != "Nickelback"}