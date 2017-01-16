songs = {
    ('Nickelback', 'How You Remind Me'),
    ('Royksopp', 'Remind Me'),
    ('Pink Floyd', 'Dogs'),
    ('Nickelback', 'Animals')
}

newlist = {song for song in songs if song[0] != 'Nickelback'}
print(newlist);