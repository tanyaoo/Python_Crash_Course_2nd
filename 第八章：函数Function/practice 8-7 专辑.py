def make_album(singer_name, album_name, number=None):
    if number:
        album = {'singer_name': singer_name, 'album_name': album_name, 'number': number}
    else:
        album = {'singer_name': singer_name, 'album_name': album_name}

    return album


album_1 = make_album('jaychou', '十一月的肖邦')
print(album_1)

album_2 = make_album('jaychou', '叶惠美', 10)
print(album_2)





