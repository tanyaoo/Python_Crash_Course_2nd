def make_album(singer, album):
    album = {'singer_name': singer, 'album_name': album}
    return album


while True:
    print('\nplease enter the follow message:')
    print('(enter "q" at any time to quit.)')

    singer_name = input('singer_name:')
    if singer_name == 'q':
        break
    album_name = input('album_name:')
    if album_name == 'q':
        break

    your_album = make_album(singer_name, album_name)
    print(f'Your album is: {your_album}.')

        
