def make_album(title, artist, number_of_songs=None):
    """function for making music albums"""
    album = {}
    album['title'] = title
    album['artist'] = artist
    if number_of_songs:
        album['number_of_songs'] = number_of_songs
    return album


print(make_album('American Idiot', 'Green Day',))
print(make_album(artist='Rise Against', title='Endgame'))
print(make_album('Egzotyka', 'Quebonafide', 14))
